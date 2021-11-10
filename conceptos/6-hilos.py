from threading import Thread 
import time

class Saludador(Thread):
    
    def __init__(self, nombre):
        super().__init__()
        self.nombre=nombre
    
    def run(self):
        print("Hola :"+self.nombre)

hilo1=Saludador("Ivan")
hilo1.start()    

print(hilo1.is_alive())
# Esto que es lo que hace? 
# Ejecutar en paralelo (en un nuevo hilo) lo que está definido en el método run() del hilo

hilo2=Saludador("Javier")
hilo2.start()

hilo3=Saludador("Jorge")
hilo3.start()

hilo4=Saludador("Liliana")
hilo4.start()

time.sleep(4)

print(hilo1.is_alive())
