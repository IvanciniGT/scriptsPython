from servidor import Servidor
from pruebas import PruebaPing
from ejecutores import PoolDeEjecutores
import yaml

def cargarServidores(fichero):
    servidores={}
    with open (fichero,"r") as fichero_yaml:
        contenido=yaml.load(fichero_yaml, Loader=yaml.FullLoader)
    for diccionario_servidor in contenido["servers"]:
        nuevo_servidor = Servidor( diccionario_servidor["name"]  , diccionario_servidor["ips"] )
        servidores[nuevo_servidor.nombre] = nuevo_servidor
    return servidores

def crearPruebasDePing(servidores,NUMERO_INTENTOS_PING,TIMEOUT_PING):
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
        
