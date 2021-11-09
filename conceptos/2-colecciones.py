# Textos: Una tupla de caracteres
# Tuplas
# Indices   0 1 2 3 4     
tuplaA=    (1,2,3,4,5)

print("Mi tupla tiene en TOTAL:                            "  +  str(     len(tuplaA)       ))
print("Quiero el primer elemento:                          "  +  str(       tuplaA[0]       ))
print("Quiero el tercer elemento:                          "  +  str(       tuplaA[2]       ))
print("Quiero el último elemento:                          "  +  str(       tuplaA[-1]      ))
print("Quiero el penúltimo elemento:                       "  +  str(       tuplaA[-2]      ))

print("Quiero los elementos segundo, tercero y cuarto      "  +  str(       tuplaA[1:4]     )) # El hasta no se incluye
print("Quiero los tres primeros elementos                  "  +  str(       tuplaA[:3]      )) # El hasta no se incluye
print("Quiero los tres últimos elementos                   "  +  str(       tuplaA[2:]      )) # El hasta no se incluye
print("Quiero los tres últimos elementos                   "  +  str(       tuplaA[-3:]      )) # El hasta no se incluye

print(   2 in tuplaA  )  # Operador lógico   TRUE
print(   7 in tuplaA  )  # Operador lógico   FALSE

print( tuplaA * 5 )

texto="HOLA AMIGO"

print( len(texto) )
print( texto[0] )
print( texto[-2] )
print( texto[5:] )


# Listas
listaA=    [1,4,4,4,5]
# Todo lo mismo de antes, y además:
listaA[0]=6
print(listaA)

listaA.append(7)
print(listaA)

listaA.insert(3,11)
print(listaA)

listaA.remove(4)
print(listaA)


# STACK: PILA : Estructura LIFO
# pop: Recuperar y eliminar el ultimo elemento de la lista   /  append

retornado=listaA.pop()
print(retornado)
print(listaA)
retornado=listaA.pop()
print(retornado)
print(listaA)

listaA.sort()
print(listaA)

listaA.reverse()
print(listaA)


lista_tuplaA=list(tuplaA)
lista_tuplaA.reverse()
tuplaA=tuple(lista_tuplaA)

print(lista_tuplaA)
print(tuplaA)

# Recuperar uno a uno los distintos valores que tengo en una lista o tupla y hacer algo con ellos
tuplaA=    (1,2,3,4,5)

for numero in tuplaA :
    print(numero)

for numero in range(0,100) :
    print(numero)

for numero in range(0,100,2) :
    print(numero)

for numero in range(100,-100,-2) :
    print(numero)

for letra in "HOLA AMIGO":
    print(letra)
    

def maximo(numero1, numero2):    #   4,6      -> 6 es el valor maximo, y que es el numero2 el que tiene ese valor.
                                # 1, si el primer numero es el maximo. 2, si es el segundo el maximo. Un 0 si son iguales
                                # Pero ademas quiero el valor maximo
    if numero1 > numero2:
        return (1,numero1)
    elif numero1 == numero2:
        return (0,numero1)
    else:
        return (2,numero2)

cual_de_los_dos_es_el_mayor, es_valor_mayor=maximo(5,5)
print("El maximo es: "+ str( es_valor_mayor ))
print("Y lo contiene el número: "+ ( "ambos son iguales" if cual_de_los_dos_es_el_mayor==0 else str(cual_de_los_dos_es_el_mayor) ))

# Desectructuración de una tupla
a,b,c=(1,2,3)
print(a)
print(b)
print(c)

# VALOR SI CONDICION SINO OTRO_VALOR
# Diccionarios
midiccionario={"clave1":"Valor1", "clave2": "Valor2"}

print(    midiccionario["clave1"]        )
print(    midiccionario.get("clave3")    )

#midiccionario={0:"Valor1", 1: "Valor2"}

#print(    midiccionario[0]    )
#print("Hasta luego")

midiccionario['clave1']= "NUEVO VALOR"
midiccionario['clave3']= "OTRO NUEVO VALOR"
print(midiccionario)


for clave in midiccionario:
    print(clave)
    print(midiccionario[clave])


for clave,valor in midiccionario.items():
    print(clave)
    print(valor)


print(midiccionario.items())