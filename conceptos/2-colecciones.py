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
# Diccionarios
