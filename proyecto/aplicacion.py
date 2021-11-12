from utilidades import cargarServidores, crearPruebasDePing, ejecutarPruebasDePing, imprimirResultadosPruebasPing, cargarParametros
import os

# python3 aplicacion.py --servers-file FICHERO --ping-timeout 1000 --ping-retries 5
# python3 aplicacion.py -f FICHERO -t 1000 -r 5
# python3 aplicacion.py  -t 1000 -r 5 -f FICHERO
#            0             1   2   3  4 5  6        N=7

import sys

parametros=cargarParametros()
servidores = cargarServidores(parametros["FICHERO"])
pruebas_ping = crearPruebasDePing(list(servidores.values()),parametros["PING_RETRIES"],parametros["PING_TIMEOUT"])
ejecutarPruebasDePing(list(pruebas_ping.values()))
imprimirResultadosPruebasPing(list(pruebas_ping.values()))