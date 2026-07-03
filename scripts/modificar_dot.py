import sys
from pathlib import Path

dot_path = Path(sys.argv[1])

text = dot_path.read_text(encoding="utf-8")

print(text[:500])

dot_path.write_text(text, encoding="utf-8")