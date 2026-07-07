"""Script to encode icons as base 64 (useful for Shields.io)"""

import argparse
import base64
from pathlib import Path

HEX_COLOR_MAP = {
    "black": "#000000",
    "white": "#ffffff"
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Icon encoder",
        description=(
            "Encodes an icon to base64 encoding. This encoding is useful for "
            "using icons in `Shields.io` that are not registered in their database."
        ),
    )
    parser.add_argument(
        "icon_name",
        help=(
            "Name (case insensitive) of the SVG icon in this repository. The "
            "extension is not required. E.G.: Provide 'Rust' to refer to 'rust.svg'."
        ),
    )
    parser.add_argument(
        "-c", "--color", choices=["white", "black"], default="white", help="Main color to fill the icon."
    )
    parser.add_argument(
        "-o",
        "--output",
        action="store_true",
        help=(
            "Creates the file 'encoded_icon.txt' with the Base64 code. If provided,"
            " the code won't be shown on the terminal."
        )
    )
    args = parser.parse_args()

    icons_db = {}
    icon_name = args.icon_name.split(".")[0].lower()
    try:
        icon_path = next(Path(".").glob(f"**/{icon_name}.svg"))
    except StopIteration:
        raise RuntimeError(f"Icon '{args.icon_name}' not found")

    color_hex = HEX_COLOR_MAP[args.color]

    icon_bin = icon_path.read_text(encoding="utf-8").replace("currentColor", color_hex).encode("utf-8")
    encoded64_data = base64.b64encode(icon_bin).decode("ascii")

    if args.output:
        with open("encoded_icon.txt", "w", encoding="utf-8") as fh:
            fh.write(encoded64_data)
        print("Base64 data saved at 'encoded_icon.txt'")
    else:
        print(
            f'Icon "{icon_path}"\n{"="*100}\n'
            f"Base64 Code:\n{encoded64_data}"
        )
