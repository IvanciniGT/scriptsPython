Programación imperativa
    Es la capacidad de escribir código (secuencia de sentencias) que se iban ejecutando de forma secuencial.
    Tenemos algunas palabras que nos permiten ir modificando la forma en la que se ejecutan las sentencias:
        Condicionales: if
        Bucles: while, for
        
Programación procedural
    Empezamos a ser capaces de crear nuestras nuestras propias funciones
    Esto nos permitía reutilizar código
    
Programación funcional
    La capacidad de referirnos a funciones desde variables.
        -> usar funciones como argumentos de otras funciones
        -> que una funcion devuelva una funcion

Programación Orientada a Objetos
    Posibilidad de crear nuestros propios tipos de datos más avanzados


Tipos de datos hasta ahora hemos podido crear en python:
- enteros
- decimales
- logicos
- texto
- listas
- tuplas
- diccionarios

Cada tipo de dato, permitían hacer unas cosas diferentes:
    lista: 
        append, insert, remove, sort, reverse
    texto   
        lower, split, strip
    numeros 
        + - * /

Servicio
    caracteristicas:
        nombre
        ubicación
        configuracion
        estado
        tipo
    operacion:
        iniciar
        parar
        consultarSuEstado
------------------- CLASES
Vamos a trabajar con Servicios WEB
    NOMBRE????
        URL: ????
        metodos: ????
Vamos a atrabajr con Pruebas sobre Servicios WEB
    Servicio: ????
    Metodo: ???
    Timeout: ????
    codigo: ???
Resultado
    resultado: OK KO  ?????
    Respuesta   ?????
    Tiempo de respuesta ?????
    Código que ha devuelto  ???
    Timestamp   ????
-------------------  INSTANCIAS CONCRETAS        
Tengo un servicio web
    Servicio GOOGLE:
        URL: https://google.es
        metodos: GET, POST, PUT

Quiero probar un servicio:
    Prueba 177:
        Servicio GOOGLE
        metodo:  get
        timeout: 2000
        codigo:  200

Quiero probar un servicio:
    Prueba 178:
        Servicio: GOOGLE
        metodo:  post
        timeout: 4000
        codigo: 405
        
        ---> ejecutar -> Resultado
                            OK KO
                            Respuesta
                            Tiempo de respuesta
                            Código que ha devuelto
                            Timestamp

CASTELLANO: Que url tiene el servicio que se prueba en la prueba 178?
PYTHON:     Prueba 178.Servicio.url

