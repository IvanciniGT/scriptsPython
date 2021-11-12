from utilidades import crearPruebasDePing, ejecutarPruebasDePing, imprimirResultadosPruebasPing, cargarParametros
from servidor import Servidor

# python3 aplicacion.py --servers-file FICHERO --ping-timeout 1000 --ping-retries 5
# python3 aplicacion.py -f FICHERO -t 1000 -r 5
# python3 aplicacion.py  -t 1000 -r 5 -f FICHERO
#            0             1   2   3  4 5  6        N=7

parametros=cargarParametros()
Servidor.cargarServidores(parametros["FICHERO"])
pruebas_ping = crearPruebasDePing(list(Servidor.servidores.values()),parametros["PING_RETRIES"],parametros["PING_TIMEOUT"])
ejecutarPruebasDePing(list(pruebas_ping.values()))
imprimirResultadosPruebasPing(list(pruebas_ping.values()))