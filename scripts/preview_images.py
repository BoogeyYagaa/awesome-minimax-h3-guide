#!/usr/bin/env python3
"""Create lightweight homepage previews; requires Pillow only when regenerating."""
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ['assets/flyne-h3-cover.png', 'assets/flyne/fy-001-lamp.png',
           'assets/flyne/fy-002-bag.png', 'assets/flyne/fy-009-backdrop.png',
           'assets/gallery/midnight-observatory-tea.webp',
           'assets/gallery/clay-repair-robot.webp', 'assets/gallery/rain-washed-canal-morning.webp']


def main():
    rows = []
    for source in SOURCES:
        path = ROOT / source
        dest = ROOT / 'assets/previews' / (path.stem + '.webp')
        dest.parent.mkdir(exist_ok=True)
        with Image.open(path) as image:
            original_size = list(image.size)
            preview = ImageOps.exif_transpose(image).convert('RGB')
            limit = 1600 if 'cover' in path.name else 640
            preview.thumbnail((limit, limit), Image.Resampling.LANCZOS)
            preview.save(dest, 'WEBP', quality=82, method=6)
            size = list(preview.size)
        rows.append(dict(source=source, preview=dest.relative_to(ROOT).as_posix(),
                         source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                         preview_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),
                         source_bytes=path.stat().st_size, preview_bytes=dest.stat().st_size,
                         source_size=original_size, preview_size=size))
    (ROOT / 'data/image-previews.json').write_text(json.dumps(rows, indent=2) + '\n')
    print(f"Homepage images: {sum(r['source_bytes'] for r in rows)} -> {sum(r['preview_bytes'] for r in rows)} bytes")


if __name__ == '__main__':
    main()
