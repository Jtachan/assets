"""Script to encode icons as base 64 (useful for Shields.io)"""
import base64
from pathlib import Path
import json

BLACK_HEX = "#000000"
WHITE_HEX = "#ffffff"


if __name__ == "__main__":
    icons_db = {}

    for icon_path in Path(".").glob("**/*.svg"):
        icon_data = icon_path.read_text(encoding="utf-8")
        icons_db[icon_path.name] = {"link": str(icon_path).replace("\\", "/")}

        for color_key, color_hex in [("white", WHITE_HEX), ("black", BLACK_HEX)]:
            icon_bin = icon_data.replace("currentColor", color_hex).encode("utf-8")
            encoded64_data = base64.b64encode(icon_bin).decode("ascii")
            icons_db[icon_path.name][color_key] = encoded64_data

    with open("icons_base64.json", "w", encoding="utf-8") as fh:
        json.dump(icons_db, fh, indent=2)
