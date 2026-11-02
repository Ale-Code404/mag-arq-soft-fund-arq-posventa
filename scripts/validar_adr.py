"""Valida que cada ADR en docs/adr tenga los campos y secciones obligatorios de MADR.

Uso: python scripts/validar_adr.py
Sale con código 1 y lista los problemas si algún ADR está incompleto.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ADR_DIR = Path(__file__).resolve().parent.parent / "docs" / "adr"
NOMBRE = re.compile(r"^(\d{4})-[a-z0-9-]+\.md$")
CAMPOS = ("status", "date")
SECCIONES = (
    "## Contexto y planteamiento del problema",
    "## Opciones consideradas",
    "## Resultado de la decisión",
    "### Consecuencias",
)
ESTADOS = ("propuesta", "aceptada", "rechazada", "reemplazada")


def front_matter(texto: str) -> dict[str, str]:
    if not texto.startswith("---\n"):
        return {}
    fin = texto.find("\n---", 4)
    if fin == -1:
        return {}
    campos = {}
    for linea in texto[4:fin].splitlines():
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            campos[clave.strip()] = valor.split("#", 1)[0].strip()
    return campos


def validar(archivo: Path, indice: str) -> list[str]:
    problemas = []
    texto = archivo.read_text(encoding="utf-8")
    meta = front_matter(texto)
    for campo in CAMPOS:
        if not meta.get(campo):
            problemas.append(f"falta el campo '{campo}' en el encabezado")
    estado = meta.get("status", "")
    if estado and not estado.startswith(ESTADOS):
        problemas.append(f"estado '{estado}' no reconocido")
    if meta.get("date") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", meta["date"]):
        problemas.append("la fecha debe tener formato AAAA-MM-DD")
    numero = NOMBRE.match(archivo.name).group(1)
    if not re.search(rf"^# ADR-{numero}: ", texto, re.MULTILINE):
        problemas.append(f"el título debe empezar con '# ADR-{numero}: '")
    for seccion in SECCIONES:
        if not re.search(rf"^{re.escape(seccion)}\s*$", texto, re.MULTILINE):
            problemas.append(f"falta la sección '{seccion}'")
    if f"({archivo.name})" not in indice:
        problemas.append("no aparece en la tabla de adr/index.md")
    return problemas


def main() -> int:
    indice = (ADR_DIR / "index.md").read_text(encoding="utf-8")
    adrs = sorted(p for p in ADR_DIR.glob("*.md") if NOMBRE.match(p.name))
    if not adrs:
        print("No se encontraron ADR en docs/adr.")
        return 1
    errores = 0
    for adr in adrs:
        problemas = validar(adr, indice)
        if problemas:
            errores += len(problemas)
            print(f"✗ {adr.name}")
            for problema in problemas:
                print(f"    - {problema}")
        else:
            print(f"✓ {adr.name}")
    numeros = [int(NOMBRE.match(p.name).group(1)) for p in adrs]
    if numeros != list(range(numeros[0], numeros[0] + len(numeros))):
        print("✗ La numeración de los ADR tiene saltos o duplicados.")
        errores += 1
    print(f"\n{len(adrs)} ADR revisados, {errores} problema(s).")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
