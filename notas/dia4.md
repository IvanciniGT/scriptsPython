    
                                    Hilos
Tareas                          Pool de Ejecutores
    Tarea1         <                Ejecutor 1
    Tarea2         <                Ejecutor 2
    Tarea3         <                Ejecutor 3
    Tarea4         <                Ejecutor 2
    Tarea5
    ...
    Tarea N
    

Que clases concretas tenemos implementadas en nuestro codigo:
    Servidor
    Prueba
        Historico de todas las ejecuciones que he hecho de esta prueba
    PruebaPing - Prueba
    PruebaServicioWeb - Prueba
    ResultadoPrueba
    ResultadoPruebaPing
    
    
    --------------------------------------
    Ejecutor
    PoolDeEjecutores
    
    --------------------------------------
    ResultadoPruebaPing - ResultadoPrueba
    --------------------------------------
        servidor: Google
        ip: google.es
        fecha: 18-2-2022
        resultado: NOK
        razones: Ese serv no existe
    --------------------------------------
    
    
    
    --------------------------------------
    PruebaPing 
    --------------------------------------
        servidor: Google
        timeout: 1 seg
        intentos: 3
        
        Historico de ejecuciones:
            Ejecucion 1 de la prueba
            Ejecucion 2 de la prueba
            Ejecucion 3 de la prueba
            Ejecucion 4 de la prueba
    --------------------------------------
    
    
    Cuando dentro de un mes ( 3 segundos despues de haber ejecutado las pruebas en otro sitio de mi codigo)
        vayas a la habitacion donde tienes los archivadores
    Puedas encontrar facilmente el resultado de las pruebas que has hecho en un momento dado
    
    
    
    
# Abro un fichero de log para dejar constancia de lo que voy haciendo
# Escribir en mi fichero que voy a abrir la conexion con la BBDD
try:
    # Abro conexion con una base de datos para escibir unas cositas
    Escribo mas cosas de que todo ha ido bien en el log
except Exception:
    !!! OSTION !!!! La base de datos no está dispionible
    Escribir en el log que tengo un problema
    levanto la execption para el que me haya llamado se entere del problema que ha ocurrido
finally:
    cierro el fichero de log 
    
------------------------------------------------------------------------------------------------
YAML
    Lenguaje para marcar informacion: Esto tiene pinta de que dentro va a tener Etiquetas.
    ¿Cuantas etiquetas tiene un archivo YAML? Ninguna
        YAML aint markup language
 XML
HTML
  ML: Markup Language     TAGS: <html><body></body></html>       <curso><alumno></alumno></curso>

No todos los lenguajes informaticos son lenguajes de programación
    - Lenguajes de marcado de información: YAML, JSON, XML, HTML, CSV
    - Lenguajes de consulta a BBDD: SQL
    - Lenguajes de modelado: UML
-------------------------------------
Aplicaciones YAML: 
    Puppet, Docker, Ansible, Kubernetes, Openshift. Conf red ubuntu