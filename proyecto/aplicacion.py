from servidor import Servidor

servidores={}

servidor_google = Servidor("Google",("google.es",) )
servidores[servidor_google.nombre] = servidor_google

servidor_googlecito = Servidor("Googlecito",("googlecito.es",) )
servidores[servidor_googlecito.nombre] = servidor_googlecito

# PruebaPing
    # Servidor, intentos,  timeout,  nombre
    # Ejecutar -> ping
        # Devolver un objeto de tipo ResultadoPruebaPing
            # Timestamp
            # OK, NOK
            # CausaError

NUMERO_INTENTOS_PING=5
TIMEOUT_PING=1000

pruebas_ping={}

prueba_ping_servidor_google = PruebaPing(servidor_google,NUMERO_INTENTOS_PING,TIMEOUT_PING)
pruebas_ping[prueba_ping_servidor_google.servidor.nombre]=prueba_ping_servidor_google

prueba_ping_servidor_googlecito = PruebaPing(servidor_googlecito,NUMERO_INTENTOS_PING,TIMEOUT_PING)
pruebas_ping[prueba_ping_servidor_googlecito.servidor.nombre]=prueba_ping_servidor_googlecito


# Lanzar la ejecución de todos los pings
    # Paralelo

# Una vez terminada la ejecuión de todas las pruebas, mostraremos un informe por consola