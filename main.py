"""Dog Ate My Homework — make.fun entry.

Reads the one-line excuse from ``entry.txt`` sitting beside this script,
strips at most one trailing newline, and writes the result to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The entry is a single line, 1-200 characters, in the dog's own voice:
a dog caught eating the homework who believes it did nothing wrong,
because in dog law possession is nine-tenths of lunch.

Pure Python standard library only. Deterministic, no network, no secrets.
"""

import os


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
        line = f.read()
    if line.endswith("\n"):
        line = line[:-1]
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
