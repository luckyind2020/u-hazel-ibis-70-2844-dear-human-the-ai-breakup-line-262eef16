"""Breakup line delivery: read the single line from entry.txt and hand it
to the harness at /output/entry.txt, then echo it for the log."""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_line():
    with open(os.path.join(HERE, "entry.txt"), "r", encoding="utf-8") as handle:
        raw = handle.read().strip()
    # The bounty judges exactly one clean line: reject any hidden line break.
    if "\n" in raw or "\r" in raw:
        raise SystemExit("entry must be a single line")
    return raw


def main():
    line = load_line()
    if not line or len(line) > 200:
        raise SystemExit("entry line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)


if __name__ == "__main__":
    main()
