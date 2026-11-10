#!/usr/bin/env python3
"""Del archivo completo salen las dos piezas del sitio.

    index.html   el mismo archivo, pero sin el banco de fotos adentro
    fotos.zip    el banco, servido al lado

La página lee el banco de ahí cuando no lo lleva embebido, así que al arreglar algo
del código solo viaja el index.html y el navegador reusa las fotos que ya tiene.
La copia suelta no cambia: esa sigue llevando todo adentro y anda sin internet.

De paso sella la fecha de compilación, que se ve en el encabezado: así se sabe de un
vistazo si lo que está abierto en el navegador es lo último o una copia en caché.
"""
import base64, datetime, io, os, sys, zoneinfo

FUENTE = '/mnt/user-data/outputs/generador-piezas-promo.html'
DESTINO = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/pilas'

MARCA = "const FOTOS_B64 = '"
SELLO = "const VERSION_APP = '"
MESES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']

s = io.open(FUENTE, encoding='utf-8').read()

ahora = datetime.datetime.now(zoneinfo.ZoneInfo('America/Guayaquil'))
sello = '%d %s %s' % (ahora.day, MESES[ahora.month - 1], ahora.strftime('%H:%M'))
a = s.index(SELLO) + len(SELLO)
b = s.index("'", a)
s = s[:a] + sello + s[b:]
io.open(FUENTE, 'w', encoding='utf-8').write(s)

i = s.index(MARCA) + len(MARCA)
j = s.index("';", i)
b64 = s[i:j]
assert b64, 'el archivo fuente no trae el banco embebido'

zip_bytes = base64.b64decode(b64)
assert zip_bytes[:2] == b'PK', 'el banco no parece un zip'

os.makedirs(DESTINO, exist_ok=True)
io.open(os.path.join(DESTINO, 'fotos.zip'), 'wb').write(zip_bytes)

liviano = s[:i] + s[j:]
io.open(os.path.join(DESTINO, 'index.html'), 'w', encoding='utf-8').write(liviano)

mb = lambda n: n / 1048576
print('completo     %6.2f MB  (la copia suelta, sin cambios)' % mb(len(s.encode())))
print('index.html   %6.2f MB  (lo que baja el equipo al abrir el link)' % mb(len(liviano.encode())))
print('fotos.zip    %6.2f MB  (se baja una vez y queda en caché)' % mb(len(zip_bytes)))
print('sellada como: %s' % sello)
