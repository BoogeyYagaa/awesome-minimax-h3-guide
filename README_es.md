# Awesome MiniMax H3 Guide · Flyne AI

![Flyne AI MiniMax H3 field guide](assets/flyne-h3-banner.svg)

[English](README.md) · [简体中文](README_zh.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md)

## Guía práctica de MiniMax H3 para producción audiovisual

Un recurso comunitario de Flyne AI con 100 prompts, flujos de producción, selección de modelos y evaluación de calidad y costes. 84 recetas se reutilizan bajo MIT con atribución; 16 son propuestas nuevas de Flyne AI. Este proyecto no ha verificado sus resultados mediante generación.

[Todos los prompts](prompts/README.md) · [Probar en Flyne AI](https://flyne.ai/model/minimax-h3/) · [Guía de modelos](docs/model-guide.md)

## Primeros pasos

Elige una receta según el entregable y asigna una función a cada referencia. Usa solo entradas admitidas por la interfaz elegida. Empieza con un sujeto y una acción; revisa forma, movimiento y sonido. Corrige un tipo de fallo por intento y guarda el registro de ejecución.

[Run record](templates/run-record.json) · [Prompt template](templates/prompt.md)

## Escenarios de trabajo

| ID | Escenarios de trabajo |
|---|---|
| FY-002 | [Variantes de producto](prompts/flyne/fy-002.md) |
| FY-003 | [Atención al cliente](prompts/flyne/fy-003.md) |
| FY-006 | [Localización](prompts/flyne/fy-006.md) |
| FY-009 | [Fondos para subtítulos](prompts/flyne/fy-009.md) |
| FY-016 | [Evaluación de referencias](prompts/flyne/fy-016.md) |

## Modelos y disponibilidad

A fecha de 2026-09-17, H3-Base ofrece pesos descargables. H3 Max es una variante alojada y posentrenada por fal; no se encontraron pesos públicos en las fuentes primarias consultadas. El flujo oficial completo de 2K también incluye componentes alojados. La licencia MIT del repositorio es distinta de la Community License del modelo.

[Guía de modelos](docs/model-guide.md) · [Fuentes](docs/sources.md)

## Documentación y búsqueda

- [Flujos de trabajo](docs/workflows.md)
- [Calidad y costes](docs/evaluation.md)
- [Hipótesis de valor futuro](docs/opportunities.md)
- [Fuentes](docs/sources.md)

Python 3.9+:

```sh
python3 scripts/catalog.py search "product"
python3 scripts/catalog.py search "FY-002" --show-prompt
python3 scripts/catalog.py build
python3 scripts/validate.py
```

[JSON catalog](data/catalog.json)

## Atribución y participación

Las 84 recetas importadas conservan el aviso de copyright de Flaq AI y su licencia MIT. Una reformulación ligera no se presenta como autoría propia. Las nuevas propuestas no están probadas. Hay README en ocho idiomas; las guías detalladas están en inglés con resúmenes en chino y los prompts canónicos en inglés. Consulta precios, modos y acceso vigentes en Flyne AI.

[Avisos de terceros](THIRD_PARTY_NOTICES.md) · [Cómo contribuir](CONTRIBUTING.md) · [MIT](LICENSE) · [Flaq AI MIT](licenses/Flaq-AI-MIT.txt)

## Colabora con Flyne AI como afiliado

¡Invitamos a creadores, educadores, reseñadores y equipos creativos a colaborar con nosotros! Comparte Flyne AI mediante tu enlace de referido y recibe comisiones por pedidos de pago válidos que cumplan los requisitos:

- **20%** por el primer pedido de pago válido del usuario referido.
- **10%** por los pedidos de pago válidos posteriores realizados durante los **60 días siguientes al registro de ese usuario**.

[Únete al programa de afiliados de Flyne AI](https://flyne.ai/affiliate-program/). La elegibilidad, atribución y liquidación están sujetas al acuerdo vigente y al proceso de revisión.

Para preguntas o propuestas de colaboración: [contact@flyne.ai](mailto:contact@flyne.ai).
