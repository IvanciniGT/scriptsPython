                   # Funcion
from sinput import sinput
    # Archivo
import sinput as sp
                # Alias

#Gracias al primer import
nombre=sinput("Como se llama el servidor que quieres reiniciar", 
                    valor_por_defecto="localhost",
                    patron_validacion="^[a-z0-9.-]+$",
                    intentos=5
             )
print(nombre)

# Gracias al segundo import
servicio=sp.sinput("Que servicio desea reiniciar", 
                    intentos=3 
                )
print(servicio)

reinicio=sinput("Estás seguro que quieres reiniciar el servidor", 
                    intentos=3,
                    valor_por_defecto="si", 
                    respuestas_posibles=('si','no') 
                )
print(reinicio)


