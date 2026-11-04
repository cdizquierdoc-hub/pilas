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

Sin servidor y sin instalación. El sitio son dos archivos:

- **`index.html`** (1,3 MB comprimido): el programa, los logos de las marcas, el
  maestro de productos y TV Wall Studio.
- **`fotos.zip`** (9,2 MB): el banco de fotos de producto, en WebP con fondo
  transparente. Se baja una vez y queda en caché, así que arreglar algo del
  código no obliga a nadie a bajarlo de nuevo.

Para usarlo **sin internet**, el menú **Fotos → «Descargar copia para usar sin
internet»** arma un único HTML con todo adentro, que se abre con doble clic.

## Cómo agregar fotos

Las fotos que faltan no necesitan una versión nueva de la herramienta:

1. En el menú **Fotos**, sube las imágenes nombradas por código
   (`SHN-150IRON-QVV-W.png`), mejor en PNG con fondo transparente.
2. Elige **«Guardar estas fotos en el banco»**.
3. Se descarga un `fotos.zip` nuevo. Súbelo al repositorio reemplazando el que
   está: el `index.html` no cambia, así que nadie vuelve a bajarlo.

PILAS las deja como las del banco: recortadas al producto, a 560 px por el lado
mayor y comprimidas en WebP.

## Cómo se actualiza el link

GitHub Pages republica el sitio en cada push a `main`. No hay nada que hacer a
mano.

La primera visita descarga unos 10,5 MB entre las dos piezas; de ahí en adelante
abre al instante, y una corrección del código son 1,3 MB.
