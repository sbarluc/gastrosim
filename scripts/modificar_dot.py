from pathlib import Path

archivo = Path("classes_Modelos.dot")

texto = archivo.read_text(encoding="utf-8")

print(texto)

archivo.write_text(texto, encoding="utf-8")