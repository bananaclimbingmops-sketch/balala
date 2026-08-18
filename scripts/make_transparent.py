#!/usr/bin/env python3
"""Convert a clean white-background Balala image into a true transparent PNG.

Only near-white pixels connected to the canvas border are removed. This avoids
erasing interior light details such as teeth, shorts, highlights, and white props.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageDraw
except ImportError:
    print(json.dumps({"passed": False, "error": "Pillow is required: python -m pip install Pillow"}))
    raise SystemExit(2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--threshold",
        type=int,
        default=18,
        help="Maximum per-channel distance from the detected background for fully transparent pixels.",
    )
    parser.add_argument(
        "--feather",
        type=int,
        default=22,
        help="Additional distance band converted to partial alpha for antialiased edges.",
    )
    parser.add_argument(
        "--minimum-background",
        type=int,
        default=225,
        help="Refuse conversion when any detected background RGB channel is below this value.",
    )
    return parser.parse_args()


def border_samples(image: Image.Image) -> tuple[list[int], list[int], list[int]]:
    width, height = image.size
    inset = max(1, round(min(width, height) * 0.005))
    pixels = image.load()
    samples = [[], [], []]

    for x in range(0, width, inset):
        for y in (0, height - 1):
            value = pixels[x, y]
            for channel in range(3):
                samples[channel].append(value[channel])
    for y in range(0, height, inset):
        for x in (0, width - 1):
            value = pixels[x, y]
            for channel in range(3):
                samples[channel].append(value[channel])

    return samples[0], samples[1], samples[2]


def detected_background(image: Image.Image) -> tuple[int, int, int]:
    channels = border_samples(image)
    return tuple(round(statistics.median(channel)) for channel in channels)  # type: ignore[return-value]


def connected_background(candidate: Image.Image) -> Image.Image:
    """Return an L mask for candidate pixels connected to at least one corner."""

    connected = candidate.copy()
    width, height = connected.size
    corners = ((0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1))

    for point in corners:
        if connected.getpixel(point) == 255:
            ImageDraw.floodfill(connected, point, 128, thresh=0)

    return connected.point(lambda value: 255 if value == 128 else 0)


def main() -> int:
    args = parse_args()
    if not args.input.is_file():
        print(json.dumps({"passed": False, "error": f"File not found: {args.input}"}))
        return 2
    if args.threshold < 0 or args.feather < 0:
        print(json.dumps({"passed": False, "error": "threshold and feather must be non-negative"}))
        return 2
    if args.input.resolve() == args.output.resolve():
        print(json.dumps({"passed": False, "error": "Input and output paths must differ"}))
        return 2

    with Image.open(args.input) as source:
        rgba = source.convert("RGBA")
        rgb = rgba.convert("RGB")
        background = detected_background(rgb)

        if min(background) < args.minimum_background:
            print(
                json.dumps(
                    {
                        "passed": False,
                        "error": "Detected border is not a clean near-white background; regenerate a white master first.",
                        "detected_background_rgb": background,
                    },
                    ensure_ascii=False,
                )
            )
            return 1

        flat = Image.new("RGB", rgb.size, background)
        difference = ImageChops.difference(rgb, flat)
        red, green, blue = difference.split()
        max_difference = ImageChops.lighter(red, ImageChops.lighter(green, blue))
        transition_end = min(255, args.threshold + args.feather)

        candidate = max_difference.point(
            lambda value: 255 if value <= transition_end else 0,
            mode="L",
        )
        connected = connected_background(candidate)

        if args.feather == 0:
            edge_alpha = max_difference.point(
                lambda value: 0 if value <= args.threshold else 255,
                mode="L",
            )
        else:
            edge_alpha = max_difference.point(
                lambda value: 0
                if value <= args.threshold
                else 255
                if value >= transition_end
                else round(255 * (value - args.threshold) / args.feather),
                mode="L",
            )

        alpha = Image.composite(edge_alpha, Image.new("L", rgba.size, 255), connected)
        alpha = ImageChops.darker(alpha, rgba.getchannel("A"))
        output = rgba.copy()
        output.putalpha(alpha)

        args.output.parent.mkdir(parents=True, exist_ok=True)
        output.save(args.output, format="PNG", optimize=True)

        histogram = alpha.histogram()
        total = output.width * output.height
        report = {
            "passed": True,
            "input": str(args.input.resolve()),
            "output": str(args.output.resolve()),
            "dimensions": [output.width, output.height],
            "detected_background_rgb": background,
            "transparent_pixel_ratio": round(histogram[0] / total, 5),
            "partially_transparent_pixel_ratio": round(sum(histogram[1:255]) / total, 5),
            "note": "Visually inspect edges and regenerate without floor/cast shadows when needed.",
        }
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0


if __name__ == "__main__":
    sys.exit(main())
