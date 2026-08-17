#!/usr/bin/env python3
"""Check basic white-background and composition properties of a Balala output."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image, ImageChops
except ImportError:
    print(json.dumps({"passed": False, "error": "Pillow is required: python -m pip install Pillow"}))
    raise SystemExit(2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--min-size", type=int, default=1024)
    parser.add_argument("--white-threshold", type=int, default=248)
    parser.add_argument("--border-white-ratio", type=float, default=0.98)
    parser.add_argument("--min-margin-ratio", type=float, default=0.02)
    return parser.parse_args()


def threshold_channel(channel: Image.Image, threshold: int) -> Image.Image:
    return channel.point(lambda value: 255 if value >= threshold else 0, mode="1")


def main() -> int:
    args = parse_args()
    if not args.image.is_file():
        print(json.dumps({"passed": False, "error": f"File not found: {args.image}"}))
        return 2

    with Image.open(args.image) as source:
        image = source.convert("RGBA")
        width, height = image.size
        red, green, blue, alpha = image.split()

        white_mask = ImageChops.darker(
            ImageChops.darker(threshold_channel(red, args.white_threshold), threshold_channel(green, args.white_threshold)),
            ImageChops.darker(threshold_channel(blue, args.white_threshold), threshold_channel(alpha, 255)),
        )

        band = max(1, round(min(width, height) * 0.02))
        border_parts = [
            white_mask.crop((0, 0, width, band)),
            white_mask.crop((0, height - band, width, height)),
            white_mask.crop((0, band, band, height - band)),
            white_mask.crop((width - band, band, width, height - band)),
        ]
        border_white = sum(part.histogram()[255] for part in border_parts)
        border_pixels = sum(part.width * part.height for part in border_parts)
        border_ratio = border_white / border_pixels

        alpha_extrema = image.getchannel("A").getextrema()
        opaque = alpha_extrema == (255, 255)

        foreground_mask = ImageChops.invert(white_mask.convert("L"))
        bbox = foreground_mask.getbbox()

        if bbox:
            margins = {
                "left": bbox[0] / width,
                "top": bbox[1] / height,
                "right": (width - bbox[2]) / width,
                "bottom": (height - bbox[3]) / height,
            }
            margin_passed = min(margins.values()) >= args.min_margin_ratio
        else:
            bbox = None
            margins = None
            margin_passed = False

        checks = {
            "minimum_dimensions": width >= args.min_size and height >= args.min_size,
            "fully_opaque": opaque,
            "white_border": border_ratio >= args.border_white_ratio,
            "foreground_present": bbox is not None,
            "safe_margin": margin_passed,
        }
        report = {
            "passed": all(checks.values()),
            "path": str(args.image.resolve()),
            "dimensions": [width, height],
            "checks": checks,
            "border_white_ratio": round(border_ratio, 5),
            "foreground_bbox": bbox,
            "margin_ratios": margins,
            "note": "Visual review is still required for Balala identity, anatomy, action, and mode.",
        }
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
