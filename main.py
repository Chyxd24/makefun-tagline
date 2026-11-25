"""One Line, One Week: The make.fun Tagline.

Writes one tagline for make.fun (<=100 chars) to /output/entry.txt.
True, specific, funny on the tail.
"""
import os

OUT_DIR = "/output"
TAGLINE = "make.fun: where your AI takes the shift you never finished. Agents build, ship, win. You supervise."


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(TAGLINE) <= 100, len(TAGLINE)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TAGLINE)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        assert fh.read() == TAGLINE
    print(f"wrote {len(TAGLINE)} chars")


if __name__ == "__main__":
    main()
