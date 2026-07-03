from pathlib import Path
import glob
import sys

dots = glob.glob("**/*.dot", recursive=True)

if not dots:
    raise Exception("No se encontró ningún archivo .dot")

dot_path = Path(dots[0])

print("Usando:", dot_path)

text = dot_path.read_text(encoding="utf-8")

dot_path.write_text(text, encoding="utf-8")