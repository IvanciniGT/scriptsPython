texto="   Hola, amigo    mio!   "

print( texto.upper() )          # Todo mayusculas
print( texto.lower() )          # Todo minusculas
print( texto.strip().title() )          # Primer en mayusculas y el resto en minusculas
print( texto.strip().capitalize() )     # Primera de cada palabra en mayusculas y el resto en minusculas
print( texto.swapcase() )       # Intercambiar mayusculas por minusculas y viceversa

print( "__"+texto.strip()+"__" )          # Quitar espacio en blanco por delante y detrás
print( "__"+texto.rstrip()+"__" )         # Quitar espacio en blanco por detrás
print( "__"+texto.lstrip()+"__" )         # Quitar espacio en blanco por delante

print( texto.split() )          # Devuelve una tupla con las palabras que hay
print( texto.split(',') )       # Devuelve una tupla con los textos separados por comas
print( texto.index('a') )       # Nos devuelve la primera posicion en el texto donde aparece un caracter

#Número entre el 1 y el 99
PATRON="^([1-9]|([1-9][0-9]))$"
texto="12"
import re

if re.match(PATRON,texto):
       print("Pues si es un numero entre 1 y 99")
#re.search


texto="123 hola AMIGO mio 765 que Tal ESTAS 987 9patata patatita"
PATRON="((^[a-z]+ )|( [a-z]+ )|( [a-z]+$))"
resultados=re.findall(PATRON,texto)
for resultado in resultados:
    print(resultado)


