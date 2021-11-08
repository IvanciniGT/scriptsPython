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
