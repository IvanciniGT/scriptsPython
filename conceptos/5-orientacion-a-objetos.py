# Servicio WEB
    # Características
        # Nombre
        # Dirección: URL : http://miservicio:puerto/ruta
        # Argumentos
        # Metodo http: get post delete head put
        
#servicio_facebook=("Facebook","https://facebook.com/","get",())
# Definit nuestro propio TIPO de variable
class ServicioWeb:
    # Le explica a python cómo se crean Servicios
                    #    "Google","https://google.es/"
                    #        V       V
    def __init__(self, un_nombre, una_url, metodos=("get",)  ):
        self.nombre=un_nombre
        self.url=una_url
        self.metodos=metodos
        

class PruebaServicioWeb:
    def __init__(self, servicio, metodo="get", codigos_respuesta_aceptables=(200,), timeout=1000  ):
        self.servicio=servicio
        self.metodo=metodo
        self.codigos_respuesta_aceptables=codigos_respuesta_aceptables
        self.timeout=timeout
    
    def ejecutar(self):
        # Llamar a la URL del servicio con el metodo definido
        # Esperar como mucho el timeout que me digan
        # Capturar la salida
        # capturar el codigo de respuesta
        # Ver si el codigo de respuesta es valido
        # Generar un objeto de tipo RespuestaPruebaServicioWeb
        # que incluya toda la infromacion obtenida
        # Ese objeto devolverlo
        print("Hago una llamada, capturo la salida y devuelvo un objeto de tipo RespuestaPruebaServicioWeb")

class ResultadoPruebaServicioWeb:
    def __init__(self,resultado ,respuesta , tiempo_de_respuesta, codigo_devuelto, timestamp):
        self.resultado=resultado
        self.respuesta=respuesta
        self.tiempo_de_respuesta=tiempo_de_respuesta
        self.codigo_devuelto=codigo_devuelto
        self.timestamp=timestamp

############################################        
        

servicio_de_google=ServicioWeb("Google","https://google.es/") # Por detrás PYTHON llama a la función 
                                                           # INIT con os args que se estén pasando
print( servicio_de_google.nombre )
print( servicio_de_google.url )
print( servicio_de_google.metodos )

#servicio_google=("Google","https://google.es/")
#print(servicio_google[0])
#print(servicio_google[1])

#prueba_servicio_google=PruebaServicioWeb(servicio_de_google, "get", (200,) , 2000)
prueba_servicio_google=PruebaServicioWeb(servicio_de_google, timeout=2000)

print( prueba_servicio_google.servicio.nombre )
print( prueba_servicio_google.servicio.url )
print( prueba_servicio_google.servicio.metodos )
print( prueba_servicio_google.metodo   )
print( prueba_servicio_google.timeout  )

prueba_servicio_google.ejecutar()