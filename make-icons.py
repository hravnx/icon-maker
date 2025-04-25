import argparse
import sys
from pathlib import Path
from typing import List
from PIL import Image


# Icon sizes for multi-resolution Windows icon files (.ico)
ICON_SIZES_ICO = [256, 128, 96, 64, 48, 32, 16]


def get_base_image(image_path: Path) -> Image.Image:
    """Open a given image file and validate it for icon use"""
    # first we make sure the image has the correct dimensions...
    img = Image.open(image_path)

    w, h = img.size
    if w != h and w != 1024:
        sys.stderr.write(f"Input image must be exactly 1024x1024, is {w}x{h}\n")
        exit(1)
    return img


def generate_alternate_images(
    source: Image.Image, sizes: List[int]
) -> List[Image.Image]:
    """Generate alternate images"""
    result = []
    for size in sorted(sizes, reverse=True):
        new_img = source.resize((size, size), resample=Image.Resampling.BICUBIC)
        result.append(new_img)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate icons for macOS (icns) and Windows (ico)"
    )

    parser.add_argument(
        "-n", "--name", type=str, default="icon", help="Base name for the icon"
    )

    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="Path to the input PNG file.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=True,
        help="Path to the output directory.",
    )
    args = parser.parse_args()

    input_file = Path(args.input)

    source = get_base_image(input_file)

    dest_dir = Path(args.output)
    dest_dir.mkdir(parents=True, exist_ok=True)

    source.save(
        dest_dir / (args.name + ".ico"),
        sizes=[(sz, sz) for sz in ICON_SIZES_ICO],
        format="ICO",
    )
    source.save(
        dest_dir / (args.name + ".icns"),
        format="ICNS",
    )
