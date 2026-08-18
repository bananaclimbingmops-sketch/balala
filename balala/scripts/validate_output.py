#!/usr/bin/env python3
"""Check white-background or transparent Balala PNG output properties."""

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
    parser.add_argument("--mode", choices=("auto", "white", "transparent"), default="auto")
    parser.add_argument("--min-size", type=int, default=1024)
    parser.add_argument("--white-threshold", type=int, default=248)
    parser.add_argument("--alpha-threshold", type=int, default=8)
    parser.add_argument("--border-ratio", type=float, default=0.98)
    parser.add_argument("--min-margin-ratio", type=float, default=0.02)
    return parser.parse_args()


def threshold_at_least(channel: Image.Image, threshold: int) -> Image.Image:
    return channel.point(lambda value: 255 if value >= threshold else 0, mode="L")


def threshold_at_most(channel: Image.Image, threshold: int) -> Image.Image:
    return channel.point(lambda value: 255 if value <= threshold else 0, mode="L")


def border_ratio(mask: Image.Image) -> float:
    width, height = mask.size
    band = max(1, round(min(width, height) * 0.02))
    parts = [
        mask.crop((0, 0, width, band)),
        mask.crop((0, height - band, width, height)),
        mask.crop((0, band, band, height - band)),
        mask.crop((width - band, band, width, height - band)),
    ]
    matched = sum(part.histogram()[255] for part in parts)
    pixels = sum(part.width * part.height for part in parts)
    return matched / pixels


def bbox_and_margins(mask: Image.Image) -> tuple[object, object, bool]:
    width, height = mask.size
    bbox = mask.getbbox()
    if not bbox:
        return None, None, False

    margins = {
        "left": bbox[0] / width,
        "top": bbox[1] / height,
        "right": (width - bbox[2]) / width,
        "bottom": (height - bbox[3]) / height,
    }
    return bbox, margins, min(margins.values())


def main() -> int:
    args = parse_args()
    if not args.image.is_file():
        print(json.dumps({"passed": False, "error": f"File not found: {args.image}"}))
        return 2

    with Image.open(args.image) as source:
        source_has_alpha = source.mode in ("RGBA", "LA", "PA") or "transparency" in source.info
        image = source.convert("RGBA")
        width, height = image.size
        red, green, blue, alpha = image.split()
        alpha_extrema = alpha.getextrema()
        mode = args.mode
        if mode == "auto":
            mode = "transparent" if source_has_alpha and alpha_extrema[0] < 255 else "white"

        if mode == "white":
            white_mask = ImageChops.darker(
                ImageChops.darker(
                    threshold_at_least(red, args.white_threshold),
                    threshold_at_least(green, args.white_threshold),
                ),
                ImageChops.darker(
                    threshold_at_least(blue, args.white_threshold),
                    threshold_at_least(alpha, 255),
                ),
            )
            measured_border_ratio = border_ratio(white_mask)
            foreground_mask = ImageChops.invert(white_mask)
            bbox, margins, minimum_margin = bbox_and_margins(foreground_mask)
            checks = {
                "png_format": source.format == "PNG",
                "minimum_dimensions": width >= args.min_size and height >= args.min_size,
                "fully_opaque": alpha_extrema == (255, 255),
                "white_border": measured_border_ratio >= args.border_ratio,
                "foreground_present": bbox is not None,
                "safe_margin": bool(bbox) and minimum_margin >= args.min_margin_ratio,
            }
            ratio_name = "border_white_ratio"
        else:
            transparent_mask = threshold_at_most(alpha, args.alpha_threshold)
            visible_mask = threshold_at_least(alpha, args.alpha_threshold + 1)
            measured_border_ratio = border_ratio(transparent_mask)
            bbox, margins, minimum_margin = bbox_and_margins(visible_mask)
            checks = {
                "png_format": source.format == "PNG",
                "minimum_dimensions": width >= args.min_size and height >= args.min_size,
                "alpha_channel": source_has_alpha,
                "transparent_pixels_present": alpha_extrema[0] == 0,
                "visible_foreground_present": alpha_extrema[1] > args.alpha_threshold and bbox is not None,
                "transparent_border": measured_border_ratio >= args.border_ratio,
                "safe_margin": bool(bbox) and minimum_margin >= args.min_margin_ratio,
            }
            ratio_name = "border_transparent_ratio"

        report = {
            "passed": all(checks.values()),
            "path": str(args.image.resolve()),
            "mode": mode,
            "dimensions": [width, height],
            "checks": checks,
            ratio_name: round(measured_border_ratio, 5),
            "alpha_extrema": alpha_extrema,
            "foreground_bbox": bbox,
            "margin_ratios": margins,
            "note": "Visual review is still required for Balala identity, anatomy, action, edge quality, and selected mode.",
        }
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
