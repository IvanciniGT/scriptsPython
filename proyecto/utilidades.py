from servidor import Servidor
from pruebas import PruebaPing
from ejecutores import PoolDeEjecutores
from parametros import Parametros 
import yaml

def crearPruebasDePing(servidores):
    NUMERO_INTENTOS_PING=Parametros.parametros["PING_RETRIES"]
    TIMEOUT_PING=Parametros.parametros["PING_TIMEOUT"]
    pruebas_ping={}
    for servidor in servidores:
        prueba_ping = PruebaPing(servidor,NUMERO_INTENTOS_PING,TIMEOUT_PING)
        pruebas_ping[prueba_ping.servidor.nombre]=prueba_ping
    return pruebas_ping

def ejecutarPruebasDePing(listado_pruebas):
    pool_ejecutor= PoolDeEjecutores(5, listado_pruebas, "ejecutar")
    pool_ejecutor.comenzarTrabajos()
    pool_ejecutor.avisaCuandoAcabes()

def imprimirResultadosPruebasPing(listado_pruebas):
    for prueba in listado_pruebas:
        print(prueba.resultados_ejecuciones[-1])
        