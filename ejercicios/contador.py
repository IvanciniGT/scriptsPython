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

class Contador:
    
    def __init__(self, hasta_que_numero, pausa):
        self.hasta_que_numero=hasta_que_numero
        self.pausa=pausa
    
    def contar(self):
        for num in range(1,self.hasta_que_numero+1):
            print(num)
            time.sleep(self.pausa)

# Cuenta hasta 10 con 1 seg delay
contador1=Contador(10,1)
contador1.contar()
# Cuenta hasta  5 con 2 seg delay
contador2=Contador(5,2)
contador2.contar()
# Cuenta hasta 20 con 0.5 seg delay
contador3=Contador(20,0.5)
contador3.contar()

# Python interpreta el codigo (lo convierte a algo que entienda el SO que hay por debajo - Linux)
# Nosotros solicitamos al SO que inicie la ejecución del programa
# Para arrancar ese programa el SO crea un Proceso a nivel de SO
# Quien ejecuta el código: Un hilo del proceso creado por el SO
