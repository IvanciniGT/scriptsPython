# Pregunta al usuario por 2 numeros
# Vais a llamar a una funcion que os vais a definir llamada identificarMaximo(2 numeros)
# La funcion debe imprimir por pantalla el maximo valor

def identificarMaximo(numero1, numero2):
    return numero1 if numero1>numero2 else numero2
    #maximo=numero2
    #if numero1 > numero2:
    #    maximo= numero1 
    #return maximo


def identificarMaximoDeTres(numero1, numero2, numero3):
    return identificarMaximo(numero1, identificarMaximo(numero2, numero3))

print("Bienvenido al calculador del mayor numero")

numero1=int(  input("Dame un número: ")  )
numero2=input("Dame otro número: ")

maximo = identificarMaximo( numero1 , int(numero2) )
print("El máximo es: " + str(maximo) )

numero3=input("Dame otro número más: ")
maximo = identificarMaximoDeTres( numero1 , int(numero2), int(numero3) )
print("El máximo es: " + str(maximo) )
