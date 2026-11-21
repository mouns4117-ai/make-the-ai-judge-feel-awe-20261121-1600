"""Write the entry text to the make.fun output path.

The text itself lives in entry.txt beside this program. This program reads
that file as raw bytes, checks it against the competition gate (UTF-8 text
of 1 to 280 Unicode code points, not only white space), and writes the
exact same bytes to entry.txt under the output directory. Nothing else is
written, and the output directory itself is never removed — it is only
created if it does not exist yet.
"""

from pathlib import Path
import os
import sys

GATE_MIN = 1
GATE_MAX = 280


def load_text(source_path: Path) -> bytes:
    raw = source_path.read_bytes()
    decoded = raw.decode("utf-8")
    if not GATE_MIN <= len(decoded) <= GATE_MAX:
        raise SystemExit(
            f"entry text is {len(decoded)} code points, outside the "
            f"{GATE_MIN}-{GATE_MAX} gate"
        )
    if not decoded.strip():
        raise SystemExit("entry text is only white space")
    return raw


def run() -> int:
    here = Path(__file__).resolve().parent
    payload = load_text(here / "entry.txt")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(payload)
    print(f"wrote entry.txt ({len(payload.decode('utf-8'))} code points)")
    return 0


if __name__ == "__main__":
    sys.exit(run())
