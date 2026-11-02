# Portal de Consulta de Posventa UAN · HLD y ADR

Documentación de arquitectura del Portal de Consulta de Posventa de la Constructora UAN, escrita como código y publicada con MkDocs en GitHub Pages.

- **Sitio:** https://ale-code404.github.io/mag-arq-soft-fund-arq-posventa/
- **PDF de cada versión:** en [Releases](https://github.com/Ale-Code404/mag-arq-soft-fund-arq-posventa/releases)

Maestría en Arquitectura de Software · Universidad Antonio Nariño · Fundamentos de Arquitectura de Software · Módulo 4, Actividad 3 · 2026-2.

## Contenido

| Ruta | Qué contiene |
|---|---|
| `docs/hld/` | Arquitectura de alto nivel: necesidad, alcance, requerimientos, diagramas y conclusiones. |
| `docs/adr/` | Registro de decisiones de arquitectura en formato MADR. |
| `docs/diagramas/posventa.drawio` | Fuente de los diagramas. Actions la exporta a SVG en cada publicación. |
| `scripts/validar_adr.py` | Revisa que cada ADR tenga los campos y secciones obligatorios. |
| `scripts/generar_pdf.py` | Genera el documento completo en PDF a partir del sitio. |
| `.github/workflows/` | `pages.yml` publica el sitio; `release.yml` adjunta el PDF a cada release. |

## Uso local

```bash
pip install -r requirements.txt
python scripts/validar_adr.py
mkdocs serve
```

Para generar el PDF en local:

```bash
pip install -r requirements-pdf.txt && python -m playwright install chromium
mkdocs build && python scripts/generar_pdf.py --version local
```
