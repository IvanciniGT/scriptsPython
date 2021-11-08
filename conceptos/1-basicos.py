# Comentarios
# Todo lo que ponga detrás de este símbolo se ignorará por el interprete.
# En python a diferencia de otros lenguajes, no existe comentario en bloque.
# En python existe una chapuza GRANDE que usamos para hacer comentarios en bloque, ya que de por si no se puede
"""
Y aqui escribo cosas
Que el interprete ignorará????
"""

#######################################################################
# Tipos de datos: VALORES
#######################################################################

# Tipos simples

## Numeros
### Números enteros:
17
-45
### Números decimales
37.98

## Textos
### Textos en una linea
'Hola soy un texto'
"Hola yo también soy un texto"

### Textos multilinea
"""
Esto es un texto
multilinea
"""

## Valores lógicos
True
False

# Tipos de colección
## Tupla: Secuencia ordenada e inalterable de datos (ARRAY), CONSTANTE
(1,2,3,4)
('HOLA', 'AMIGO')   # Esto es una tupla de textos
('HOLA')            # Como se interpreta esto: SE INTERPRETA COMO SI NO HUBIERA PARENTESIS, es decir, como un texto
                    # USO DE PARENTESIS EN PYTHON. Los parentesis los usamos para varias cosas:
                        # 1- Definir tuplas
                        # 2- Agrupar valores en expresiones: (3+7)*4   (3)*4     (3) 
                        # 3- Ejecutar funciones
("HOLA",)           # Aqui python interpreta una tupla con un solo valor

## Lista: Secuencia ordenada de datos (ARRAY), modificables
[1,2,3,4]
['HOLA', 'AMIGO',]  # Es una lista de textos
['HOLA', 'AMIGO']   # Es una lista de textos. EQUIVALENTE A LA ANTERIOR
['HOLA']            # Es una lista con un texto

## Diccionario: Colecciones no ordenadas de valores, modificables, donde cada valor va identificado por una clave
{"palabra1":"HOLA", "palabra2": 54}

# VARIABLES: 
# El signo = es el operador de asignación 
numero=17
texto = "HOLA"
mi_variable_logica=True

# CONSTANTES:Una variable que no puedo variar, que siempre apunta al mismo valor.
# En python no existen
# Usamos el nombre de una variable todo en mayusculas, cuando queremos incicar que no cambia de valor (constante)

# OPERADORES
# Operadores aritmenticos:   numero OP numero -> numero
2+3-4*7/8
7/2     # División con decimales: 3.5
7//2    # División entera:        3
7%2     # Resto:                  1  

# Operadores relaciones   numero OP numero -> valor logico
#> < >= <= == !=
3>2   # True

# Operadores lógicos      valor logico OP valor logico -> valor logico
True and True    #=> True
True or False    #   True
not True         #   False

# Operadores que podemos aplciar sobre textos
"HOLA" + "AMIGO"   # Operador concatenar   "HOLAAMIGO"
"HOLA" * 3         # "HOLAHOLAHOLA"

# Funciones básicas definidas por python
print("HOLA AMIGO")     # Para ejcutar una funcion, debo llamarla con unos parentesis detrás. 
                        # Si la función admite o requiere argumentos, se incluirian dentro de los parentesis
edad = input("Dame tu edad ")       # Permite leer de la consola
#- input -> El valor que se devuelve se anota en RAM
#- definir la variable edad
#- pegar la variable edad al ladito de lo que devuelva la funcion input

# Que tipo de datos referenciará la variable edad? TEXTO
print(edad)

# Funciones de conversion de tipos
str(32)
int("32")
float("43.8")
bool("True")

print(  "Dentro de 10 años, tendrás: " + str(     int(edad) + 10   ) )



