"""The Dog Reviews the Mailman — one-line review entry for make.fun.

Writes the dog's review of the mailman to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output), then reads it back
and checks it against the gate: exact line, 1-200 characters, not
whitespace only.
"""

import os

REVIEW_LINE = "Brave enough to cross my yard daily, smart enough to flee my bark, rude enough to bring paper instead of chicken."


def write_entry(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW_LINE)
    return path


def main():
    path = write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == REVIEW_LINE, "entry.txt does not match the review line"
    assert 1 <= len(written) <= 200, "entry.txt must be 1-200 characters"
    assert written.strip(), "entry.txt must not be whitespace only"


if __name__ == "__main__":
    main()
