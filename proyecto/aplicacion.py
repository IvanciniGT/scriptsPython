from utilidades import crearPruebasDePing, ejecutarPruebasDePing, imprimirResultadosPruebasPing
from servidor import Servidor
from parametros import Parametros
# python3 aplicacion.py --servers-file FICHERO --ping-timeout 1000 --ping-retries 5
# python3 aplicacion.py -f FICHERO -t 1000 -r 5
# python3 aplicacion.py  -t 1000 -r 5 -f FICHERO
#            0             1   2   3  4 5  6        N=7

Parametros.cargarParametros()
Servidor.cargarServidores()
pruebas_ping = crearPruebasDePing(list(Servidor.servidores.values()))
ejecutarPruebasDePing(list(pruebas_ping.values()))
imprimirResultadosPruebasPing(list(pruebas_ping.values()))