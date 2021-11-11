from utilidades import cargarServidores, crearPruebasDePing, ejecutarPruebasDePing, imprimirResultadosPruebasPing

# python3 aplicacion.py --servers-file FICHERO --ping-timeout 1000 --ping-retries 5
# python3 aplicacion.py -f FICHERO -t 1000 -r 5
# python3 aplicacion.py  -t 1000 -r 5 -f FICHERO

import sys

print(sys.argv)

FICHERO=None

posicion_argumento=1
while posicion_argumento< len(sys.argv):
    if sys.argv[posicion_argumento] == "-f" or  sys.argv[posicion_argumento] == "--servers-file":
        FICHERO=sys.argv[posicion_argumento+1]
        posicion_argumento+=1
    posicion_argumento+=1

servidores = cargarServidores(FICHERO)
pruebas_ping = crearPruebasDePing(list(servidores.values()),5,1000)
ejecutarPruebasDePing(list(pruebas_ping.values()))
imprimirResultadosPruebasPing(list(pruebas_ping.values()))