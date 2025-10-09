#!/usr/bin/env python3

import nbformat
import base64
import re
from pathlib import Path
import sys

if len(sys.argv) != 2:
    print("Usage: embed_images.py <notebook_directory>")
    sys.exit(1)

notebook_dir = Path(sys.argv[1])

if not notebook_dir.is_dir():
    print(f"Error: {notebook_dir} is not a directory.")
    sys.exit(1)

for nb_path in notebook_dir.glob("*.ipynb"):
    print(f"Processing {nb_path}")
    nb = nbformat.read(nb_path, as_version=4)

    for cell in nb.cells:
        if cell.cell_type != 'markdown':
            continue

        def replace_image(match):
            alt_text, img_path = match.group(1), match.group(2)
            full_path = (notebook_dir / img_path).resolve()
            if not full_path.exists():
                print(f"  Warning: {img_path} not found")
                return match.group(0)
            ext = full_path.suffix[1:]
            b64 = base64.b64encode(full_path.read_bytes()).decode()
            datauri = f"data:image/{ext};base64,{b64}"
            print(f"  Embedded {img_path}")
            return f"![{alt_text}]({datauri})"

        cell.source = re.sub(r'!\[(.*?)\]\((.*?)\)', replace_image, cell.source)

    nbformat.write(nb, nb_path)
