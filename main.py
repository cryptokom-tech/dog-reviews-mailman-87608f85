import os
from pathlib import Path

LINE = "Brave enough to cross my yard daily, smart enough to flee my bark, rude enough to bring paper instead of chicken."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")

    written = entry_path.read_text(encoding="utf-8")
    assert written == LINE
    assert 1 <= len(written) <= 200
    assert written.strip()
    assert "\n" not in written
    assert "\r" not in written


if __name__ == "__main__":
    main()
