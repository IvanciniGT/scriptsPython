import time
"""
############################################################################################################
# Programación imperativa:

## Cuenta hasta 10 con 1 seg delay
for num in range(1,11):
    print(num)
    time.sleep(1)
## Cuenta hasta  5 con 2 seg delay
for num in range(1,6):
    print(num)
    time.sleep(2)
## Cuenta hasta 20 con 0.5 seg delay
for num in range(1,21):
    print(num)
    time.sleep(0.5)

############################################################################################################
# Programación procedural:

def contar(hasta_cual, pausa):
    for num in range(1,hasta_cual+1):
        print(num)
        time.sleep(pausa)

# Cuenta hasta 10 con 1 seg delay
contar(10,1)
# Cuenta hasta  5 con 2 seg delay
contar(5,2)
# Cuenta hasta 20 con 0.5 seg delay
contar(20,0.5)
"""

############################################################################################################
# Programación Orientada a Objetos:

from threading import Thread

class Contador(Thread):
    
    @classmethod
    def queParenTodos(cls):
        # A quien aplicaría? A un Contador
    
    def __init__(self, nombre,hasta_que_numero, pausa):
        super().__init__()
        self.nombre=nombre
        self.hasta_que_numero=hasta_que_numero
        self.pausa=pausa
        self.conteo_cancelado=False
    
    def contar(self):
        self.start()
    
    def dejaDeContar(self):
        self.conteo_cancelado=True
        print("Me detengo.. A sus ordenes comandante! Soy el contador: "+ self.nombre)
    
    def run(self):
        for num in range(1,self.hasta_que_numero+1):
            if self.conteo_cancelado:
#           if self.conteo_cancelado == True:
                break
            print("Soy el contador "+self.nombre+" voy por el número:" + str(num) )
            time.sleep(self.pausa)

print("HOLA soy el hilo principal")
# Cuenta hasta 10 con 1 seg delay
contador1=Contador("A",10,1)
contador1.contar()
# Cuenta hasta  5 con 2 seg delay
contador2=Contador("B",5,2)
contador2.contar()
# Cuenta hasta 20 con 0.5 seg delay
contador3=Contador("C",20,0.5)
contador3.contar()
# A los 5 segundos de empezar la cuenta, quiero que el hilo
# principal le pida por las buenas al hilo contador1, que deje de contar

time.sleep(5)
contador1.dejaDeContar()
time.sleep(2)
# Quiero que TODO EL MUNDO deje de contar ( no el contador2 y el contador3)
Contador.queParenTodos()

print("Yo aqui... que me tienen olvidao... Que no me cuenta... siendo el principal")
contador1.join() ## Hilo principal!, esperate a que acabe el contador1, para seguir
contador2.join() ## Hilo principal!, esperate a que acabe el contador2, para seguir
contador3.join() ## Hilo principal!, esperate a que acabe el contador3, para seguir
print("Este mensaje le quiero una vez los hilos hayan terminado")
# Python interpreta el codigo (lo convierte a algo que entienda el SO que hay por debajo - Linux)
# Nosotros solicitamos al SO que inicie la ejecución del programa
# Para arrancar ese programa el SO crea un Proceso a nivel de SO
# Quien ejecuta el código: Un hilo del proceso creado por el SO
