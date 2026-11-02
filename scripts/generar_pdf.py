"""Genera el documento completo en PDF a partir del sitio compilado por MkDocs.

Recorre las páginas en el orden de `nav` de mkdocs.yml, une su contenido en un solo
documento con portada e índice, y lo imprime con Chromium (Playwright).

Uso:
    mkdocs build
    python scripts/generar_pdf.py --version v1.0.0 --out dist/HLD-ADR-Posventa-v1.0.0.pdf
"""

from __future__ import annotations

import argparse
import datetime as dt
import functools
import html
import http.server
import threading
from pathlib import Path

import yaml
from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent.parent

EXTRAER = """
(sitio) => {
  const a = document.querySelector('article.md-content__inner');
  a.querySelectorAll('a.headerlink, a.md-content__button').forEach(e => e.remove());
  a.querySelectorAll('img').forEach(i => i.setAttribute('src', i.src));
  a.querySelectorAll('a[href]').forEach(l => {
    if (l.href.startsWith(location.origin)) {
      l.setAttribute('href', l.href.replace(location.origin + '/', sitio));
    }
  });
  return a.innerHTML;
}
"""

ESTILO = """
<style>
  .pdf-portada { min-height: 230mm; display: flex; flex-direction: column; justify-content: center; }
  .pdf-portada h1 { font-size: 2.2em; margin-bottom: .2em; }
  .pdf-portada .sub { font-size: 1.2em; color: #546e7a; margin-bottom: 2em; }
  .pdf-salto { break-before: page; }
  .pdf-indice li { margin: .2em 0; }
  @media print { .md-typeset table:not([class]) { font-size: .62rem; } }
</style>
"""


def paginas(nav: list) -> list[tuple[str, str]]:
    """Aplana la navegación de MkDocs en una lista (título, archivo .md)."""
    salida: list[tuple[str, str]] = []
    for item in nav:
        if isinstance(item, str):
            salida.append(("", item))
        elif isinstance(item, dict):
            for titulo, valor in item.items():
                if isinstance(valor, str):
                    salida.append((titulo, valor))
                else:
                    salida.extend(paginas(valor))
    return salida


def url_de(md: str) -> str:
    ruta = md.removesuffix(".md")
    if ruta == "index":
        return ""
    if ruta.endswith("/index"):
        return ruta.removesuffix("index")
    return ruta + "/"


class Silencioso(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args) -> None:  # noqa: D102
        pass


def servir(directorio: Path) -> tuple[http.server.ThreadingHTTPServer, str]:
    manejador = functools.partial(Silencioso, directory=str(directorio))
    servidor = http.server.ThreadingHTTPServer(("127.0.0.1", 0), manejador)
    threading.Thread(target=servidor.serve_forever, daemon=True).start()
    return servidor, f"http://127.0.0.1:{servidor.server_port}/"


def portada(config: dict, version: str) -> str:
    filas = [
        ("Versión", version),
        ("Fecha", dt.date.today().isoformat()),
        ("Autor", config.get("site_author", "")),
        ("Sitio", config.get("site_url", "")),
        ("Repositorio", config.get("repo_url", "")),
    ]
    tabla = "".join(f"<tr><th>{k}</th><td>{html.escape(v)}</td></tr>" for k, v in filas)
    return (
        '<section class="pdf-portada">'
        f"<h1>{html.escape(config['site_name'])}</h1>"
        '<div class="sub">Arquitectura de alto nivel (HLD) y registro de decisiones (ADR)</div>'
        f"<table>{tabla}</table>"
        f"<p>{html.escape(config.get('copyright', ''))}</p>"
        "</section>"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", default=str(RAIZ / "site"))
    parser.add_argument("--config", default=str(RAIZ / "mkdocs.yml"))
    parser.add_argument("--version", default="borrador")
    parser.add_argument("--out", default=str(RAIZ / "dist" / "documento.pdf"))
    args = parser.parse_args()

    config = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    sitio = config.get("site_url", "/")
    lista = paginas(config["nav"])
    salida = Path(args.out)
    salida.parent.mkdir(parents=True, exist_ok=True)

    servidor, base = servir(Path(args.site))
    try:
        with sync_playwright() as p:
            navegador = p.chromium.launch()
            lector = navegador.new_page()
            secciones, indice = [], []
            for i, (_, md) in enumerate(lista):
                lector.goto(base + url_de(md), wait_until="networkidle")
                titulo = lector.locator("article.md-content__inner h1").first.inner_text().replace("¶", "").strip()
                indice.append(f'<li><a href="#pdf-{i}">{html.escape(titulo)}</a></li>')
                contenido = lector.evaluate(EXTRAER, sitio)
                secciones.append(f'<section id="pdf-{i}" class="pdf-salto">{contenido}</section>')

            documento = (
                ESTILO
                + portada(config, args.version)
                + '<section class="pdf-salto pdf-indice"><h1>Contenido</h1><ol>'
                + "".join(indice)
                + "</ol></section>"
                + "".join(secciones)
            )

            pagina = navegador.new_page()
            pagina.goto(base, wait_until="networkidle")
            pagina.evaluate(
                "(h) => { document.querySelector('article.md-content__inner').innerHTML = h; }",
                documento,
            )
            pagina.wait_for_function("Array.from(document.images).every(i => i.complete)")
            pagina.emulate_media(media="print")
            pie = (
                '<div style="font-size:8px;width:100%;padding:0 12mm;color:#78909c;'
                'display:flex;justify-content:space-between">'
                f"<span>{html.escape(config['site_name'])} · {html.escape(args.version)}</span>"
                '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>'
            )
            pagina.pdf(
                path=str(salida),
                format="A4",
                print_background=True,
                margin={"top": "16mm", "bottom": "18mm", "left": "14mm", "right": "14mm"},
                display_header_footer=True,
                header_template="<div></div>",
                footer_template=pie,
            )
            navegador.close()
    finally:
        servidor.shutdown()
    print(f"PDF generado: {salida} ({len(lista)} páginas del sitio)")


if __name__ == "__main__":
    main()
