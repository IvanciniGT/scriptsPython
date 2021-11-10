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
        
        

servicio_de_google=ServicioWeb("Google","https://google.es/") # Por detrás PYTHON llama a la función 
                                                           # INIT con os args que se estén pasando
print( servicio_de_google.nombre )
print( servicio_de_google.url )
print( servicio_de_google.metodos )

#servicio_google=("Google","https://google.es/")
#print(servicio_google[0])
#print(servicio_google[1])

# Prueba de un servicio WEB
    # Carecteristicas
        # ServicioWeb
        # Metodo A Probar: GET , POST, DELETE 
        # CodigosRespuestaAceptable: (200, 201)
        # Timeout: 300ms