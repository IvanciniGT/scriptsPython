numero1=int( input("Dame un numero: ")  )
numero2=int( input("Dame otro numero: ")  )

# Muy mala practica: Por que en este caso, me es muy facil evitar que se produzca el error
try:
    resultado=numero1/numero2
    print("El restultado de dividir "+ str(numero1)+" entre "+ str(numero2)+" es: "+ str(resultado))
except ZeroDivisionException as la_excepcion:
    print(la_excepcion)
    print("Ojo... hemos tenido un problema al dividir entre cero.. ten mas cuidado amiguete la proxima vez !!!")
    raise la_excepcion
else:   # Lo vais a ver/utilizar con poca frecuencia
    print("Codigo que ejecutaria si todo fue bien")
finally:
    print("Codigo que ejecuta en cualquier escenario")

print("El programa sigue su curso")

resultado=numero1*numero2
print("El restultado de multiplicar "+ str(numero1)+" por "+ str(numero2)+" es: "+ str(resultado))




#################
# Buena practica 
numero1=int( input("Dame un numero: ")  )
numero2=int( input("Dame otro numero: ")  )

if numero2 != 0:
    resultado=numero1/numero2
    print("El restultado de dividir "+ str(numero1)+" entre "+ str(numero2)+" es: "+ str(resultado))
else:
    print("Ojo... hemos tenido un problema al dividir entre cero.. ten mas cuidado amiguete la proxima vez !!!")

resultado=numero1*numero2
print("El restultado de multiplicar "+ str(numero1)+" por "+ str(numero2)+" es: "+ str(resultado))

# No siempre puedo evitar que se produzca un error y entonces uso excepciones