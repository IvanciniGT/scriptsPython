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

# Operadores de asignacion
variable=3
variable+=3 # Variable= 6 
variable-=3 # Variable= 0
variable*=3 # Variable= 9 
variable/=3 # Variable= 1 

texto="HOLA"
texto+=" AMIGO" # texto= "HOLA AMIGO"


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
#list()
#tuple()

print(  "Dentro de 10 años, tendrás: " + str(     int(edad) + 10   ) )

# Programación imperativa

# Expresiones de control de flujo:
# if CONDICION:
# El codigo que pongamos dentro del if, se ejecutará solamente si la condicion es verdadera: TRUE

edad=int(edad)
if edad > 65:
    print("Eres muy muy mayor de edad")
elif edad > 18:
    print("Eres mayor de edad")
else:
    # Esto se ejecuta si no se cumple la condicion del if
    print("Eres menor de edad")

print("Acabamos")

    # VALOR_VERDADERO if CONDICION else VALOR_SI_NO

# Por cuantos caminos diferentes puede entrar el codigo:
# 3   <     Complejidad ciclomatica: Numero de caminos diferentes que puede tomar un codigo al ejecutarse
#                                   PRUEBAS DE SOFTWARE: Al menos cuantas pruebas debo realizar a mi programa? 
#                                                        Tantas como su complejidad ciclomatica
# > 18 y > 65
# > 18 y < 65
# <= 18

# Como definir nuestras propias funciones dentro de python < PROGRAMACION PROCEDURAL

                                 # Valor por defecto si no me dicen nada de exclamaciones
def saluda(nombre="Amigo", exclamaciones=True):
    if exclamaciones:
        print("HOLA "+nombre+" !!!!")
    else:
        print("HOLA "+nombre)


saluda("Ivan")
saluda("Iria", False)
saluda("Carlos", True)
saluda("Albert")
saluda()
saluda(exclamaciones=False)
saluda(exclamaciones=False, nombre="Lucas")
# Todos los valores que pase con valor por defecto, los puedo pasar mediante un nombre identificativo, 
# saltandome el orden normal de suministro de parametros

def mifuncion(arg1, arg2, arg3="Tengo valor por defecto", arg4="Yo también tengo valor por defecto"):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

mifuncion("HOLA","AMIGO",arg4="COMO",arg3="ESTAS?")

def doblar(numero):
    return numero*2

print( doblar(10) )

el_doble_de_5 = doblar(5)
print(el_doble_de_5)


resultado= doblar(5) + 7
print(resultado)

# Bucle WHILE. Es lo mismo que un if.
# Solo que la condicion no se evalua solamente 1 vez... Sino que se reevalua cada vez que acaba de ejecutarse el codigo asociado

edad=10
if edad>5:
    print("La edad es mayor que 5. De hecho vale: "+str(edad) )

while edad>5:
    print("La edad es mayor que 5. De hecho vale: "+str(edad) )
    edad=edad-1

edad=10
while True:
    print("La edad es mayor que 5. De hecho vale: "+str(edad) )
    edad=edad-1
    if edad<5:
        break

