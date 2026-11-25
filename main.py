"""Writes the front page for Wednesday 25 November 2026 to /output/entry.png.

The picture is built ahead of time by tools/build.py and kept in this
repository as entry.png; this program only copies its exact bytes, so every
run writes the same file and needs no network.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
TARGET = os.path.join(OUT_DIR, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576


def main() -> int:
    with open(SOURCE, "rb") as f:
        data = f.read()
    if not data.startswith(PNG_MAGIC):
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"entry.png is {len(data)} bytes, over 1 MiB", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp = TARGET + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, TARGET)
    try:
        os.chmod(TARGET, 0o644)
    except OSError:
        pass
    print(f"wrote {TARGET} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
