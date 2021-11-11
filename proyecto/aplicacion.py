from servidor import Servidor
from pruebas import PruebaPing
from ejecutores import PoolDeEjecutores
servidores={}

servidor_google = Servidor("Google",("google.es",) )
servidores[servidor_google.nombre] = servidor_google

servidor_googlecito = Servidor("Googlecito",("googlecito.es",) )
servidores[servidor_googlecito.nombre] = servidor_googlecito

NUMERO_INTENTOS_PING=5
TIMEOUT_PING=1000

pruebas_ping={}

prueba_ping_servidor_google = PruebaPing(servidor_google,NUMERO_INTENTOS_PING,TIMEOUT_PING)
pruebas_ping[prueba_ping_servidor_google.servidor.nombre]=prueba_ping_servidor_google

prueba_ping_servidor_googlecito = PruebaPing(servidor_googlecito,NUMERO_INTENTOS_PING,TIMEOUT_PING)
pruebas_ping[prueba_ping_servidor_googlecito.servidor.nombre]=prueba_ping_servidor_googlecito

pool_ejecutor= PoolDeEjecutores(5, list(pruebas_ping.values()), "ejecutar")
pool_ejecutor.comenzarTrabajos()

# Cuando termine el resto de hilos
pool_ejecutor.avisaCuandoAcabes()
print("Pruebas finalizadas")

# Imprimir los resultados
for prueba in pruebas_ping.values():
    print(prueba.resultados_ejecuciones[-1])