# PILAS

**Plataforma Inteligente de Lotes de Artes Semanales.**

Convierte la presentación comercial de la semana en una matriz de promociones y
arma con ella las piezas gráficas de las cadenas del grupo: Crecos, Orve Hogar,
Japón, MultiNOVA, Motozone y Pagamenos.

👉 **[Abrir PILAS](https://cdizquierdoc-hub.github.io/pilas/)**

## Qué hace

- Lee el PPTX comercial y saca la matriz de promociones en Excel, con código,
  marca, descripción, forma de pago, cuota y regalo.
- Arma las piezas en tres formatos: **stories** (1080×1350), **TV Wall**
  (1920×1080) y **post** (1080×1080), en crédito, contado y combo.
- Descarga todo en un ZIP, con una carpeta por formato.
- Trae **TV Wall Studio** adentro, para pasar los reels de Instagram al TV wall
  de las tiendas.

## Qué lleva adentro

Es **un solo archivo HTML**, sin servidor y sin instalación. Todo va embebido:

- 490 códigos con foto de producto, en WebP con fondo transparente.
- Los logos de las marcas del grupo.
- El maestro de productos, para completar lo que la lámina no imprime.

Por eso también funciona sin internet: basta con descargar `index.html` y
abrirlo con doble clic.

## Cómo agregar fotos

Las fotos que faltan no necesitan una versión nueva de la herramienta:

1. En el menú **Fotos**, sube las imágenes nombradas por código
   (`SHN-150IRON-QVV-W.png`), mejor en PNG con fondo transparente.
2. Elige **«Guardar estas fotos dentro de la herramienta»**.
3. Se descarga una copia de PILAS con esas fotos ya adentro.

PILAS las deja como las del banco: recortadas al producto, a 560 px por el lado
mayor y comprimidas en WebP.

## Cómo se actualiza el link

Cada push de `index.html` a `main` dispara el workflow de
[`.github/workflows/publicar.yml`](.github/workflows/publicar.yml), que vuelve a
publicar el sitio. No hay nada que hacer a mano.

La primera visita descarga unos 15 MB; después queda en caché del navegador.
