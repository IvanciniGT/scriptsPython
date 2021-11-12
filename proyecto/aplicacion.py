from utilidades import cargarServidores, crearPruebasDePing, ejecutarPruebasDePing, imprimirResultadosPruebasPing
import os

# python3 aplicacion.py --servers-file FICHERO --ping-timeout 1000 --ping-retries 5
# python3 aplicacion.py -f FICHERO -t 1000 -r 5
# python3 aplicacion.py  -t 1000 -r 5 -f FICHERO
#            0             1   2   3  4 5  6        N=7

import sys


FICHERO=None
PING_RETRIES=5
PING_TIMEOUT=1000

posicion_argumento=1
while posicion_argumento< len(sys.argv):
    if sys.argv[posicion_argumento] == "-f" or  sys.argv[posicion_argumento] == "--servers-file":
        if len(sys.argv) > posicion_argumento+1:
            FICHERO=sys.argv[posicion_argumento+1]
        else:
            print("Argumento incompleto '"+sys.argv[posicion_argumento]+"'. Falta el nombre del fichero")
            exit(1)
        posicion_argumento+=1

    elif sys.argv[posicion_argumento] == "-r" or  sys.argv[posicion_argumento] == "--ping-retries":
        if len(sys.argv) > posicion_argumento+1:
            PING_RETRIES=int(sys.argv[posicion_argumento+1])
        else:
            print("Argumento incompleto '"+sys.argv[posicion_argumento]+"'. Falta el numero de reintentos")
            exit(1)
        posicion_argumento+=1

    elif sys.argv[posicion_argumento] == "-t" or  sys.argv[posicion_argumento] == "--ping-timeout":
        if len(sys.argv) > posicion_argumento+1:
            PING_TIMEOUT=int(sys.argv[posicion_argumento+1])
        else:
            print("Argumento incompleto '"+sys.argv[posicion_argumento]+"'. Falta el timeout")
            exit(1)
        posicion_argumento+=1
    posicion_argumento+=1


# Asegurarnos que el fichero existe
if not os.path.exists(FICHERO):
    print("El fichero de servidores no existe. Reviselo!")
    exit(2)
servidores = cargarServidores(FICHERO)
pruebas_ping = crearPruebasDePing(list(servidores.values()),PING_RETRIES,PING_TIMEOUT)
ejecutarPruebasDePing(list(pruebas_ping.values()))
imprimirResultadosPruebasPing(list(pruebas_ping.values()))