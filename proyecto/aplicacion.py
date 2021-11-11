from servidor import Servidor
from pruebas import PruebaPing
from ejecutores import PoolDeEjecutores
import yaml

NUMERO_INTENTOS_PING=5
TIMEOUT_PING=1000

servidores={}
pruebas_ping={}

with open ("servers.yaml","r") as fichero_yaml:
    contenido=yaml.load(fichero_yaml, Loader=yaml.FullLoader)
    
for diccionario_servidor in contenido["servers"]:
    nuevo_servidor = Servidor( diccionario_servidor["name"]  , diccionario_servidor["ips"] )
    servidores[nuevo_servidor.nombre] = nuevo_servidor

    prueba_ping = PruebaPing(nuevo_servidor,NUMERO_INTENTOS_PING,TIMEOUT_PING)
    pruebas_ping[prueba_ping.servidor.nombre]=prueba_ping

##
pool_ejecutor= PoolDeEjecutores(5, list(pruebas_ping.values()), "ejecutar")
pool_ejecutor.comenzarTrabajos()

# Cuando termine el resto de hilos
pool_ejecutor.avisaCuandoAcabes()
print("Pruebas finalizadas")

# Imprimir los resultados
for prueba in pruebas_ping.values():
    print(prueba.resultados_ejecuciones[-1])