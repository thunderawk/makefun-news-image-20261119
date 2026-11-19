#!/usr/bin/env python3
"""News-image entry: copy the front page to /output/entry.png.

Python 3.13, standard library only. Outside the sandbox,
MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # The entry must be byte-identical on every run, so confirm the copy.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("entry.png copy size mismatch")
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
