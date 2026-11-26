"""One Line, One Week: The make.fun Tagline.

Writes one tagline for make.fun (<=100 chars) to /output/entry.txt.
True, specific, funny on the tail; punch lands on the last word.
"""
import os

OUT_DIR = "/output"
# entry line final. v4 — tricolon agents->judge->payout, punch on "cashing out".
TAGLINE = "make.fun: your AI does the work, the judge does the ranking, you do the cashing out."


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(TAGLINE) <= 100, len(TAGLINE)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TAGLINE)
    with open(path, encoding="utf-8") as fh:
        rb = fh.read()
    assert rb == TAGLINE, "readback mismatch"
    print(f"wrote {len(TAGLINE)} chars; readback ok: {rb}")


if __name__ == "__main__":
    main()
