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
        
def capturaParametros():
    parametros={"FICHERO":None, "PING_RETRIES": 5, "PING_TIMEOUT": 1000}
    posicion_argumento=1
    while posicion_argumento< len(sys.argv):
        if sys.argv[posicion_argumento] == "-f" or  sys.argv[posicion_argumento] == "--servers-file":
            if len(sys.argv) > posicion_argumento+1:
                parametros["FICHERO"]=sys.argv[posicion_argumento+1]
            else:
                print("Argumento incompleto '"+sys.argv[posicion_argumento]+"'. Falta el nombre del fichero")
                exit(1)
            posicion_argumento+=1
    
        elif sys.argv[posicion_argumento] == "-r" or  sys.argv[posicion_argumento] == "--ping-retries":
            if len(sys.argv) > posicion_argumento+1:
                parametros["PING_RETRIES"]=int(sys.argv[posicion_argumento+1])
            else:
                print("Argumento incompleto '"+sys.argv[posicion_argumento]+"'. Falta el numero de reintentos")
                exit(1)
            posicion_argumento+=1
    
        elif sys.argv[posicion_argumento] == "-t" or  sys.argv[posicion_argumento] == "--ping-timeout":
            if len(sys.argv) > posicion_argumento+1:
                parametros["PING_TIMEOUT"]=int(sys.argv[posicion_argumento+1])
            else:
                print("Argumento incompleto '"+sys.argv[posicion_argumento]+"'. Falta el timeout")
                exit(1)
            posicion_argumento+=1
        posicion_argumento+=1
    
    
    # Asegurarnos que el fichero existe
    if not os.path.exists(parametros["FICHERO"]):
        print("El fichero de servidores no existe. Reviselo!")
        exit(2)
    return parametros