"""
def nombreNormal(nombre):
    return nombre.capitalize()

def nombreEfusivo(nombre):
    return nombre.upper()


#def saludoEfusivo(nombre, funcion_transformacion_nombre):
#    print("HOLA "+funcion_transformacion_nombre(nombre)+"!!!!!!!!!")
    
def saludoNormal(nombre,funcion_transformacion_nombre):
    print("Hola "+funcion_transformacion_nombre(nombre))
    
usuario="ivan"
saludoNormal(usuario, nombreNormal)
saludoNormal(usuario, nombreEfusivo)

"""

def opcionA():
    print("A")

def opcionB():
    print("B")
    
def opcionC():
    print("C")
    
def opcionD():
    print("D")


def menu( funciones_posibles ):
    print("Titulos....")
    numero=input("Dame numero: ")
    
    opcion=int(numero)-1
    
    funciones_posibles[opcion]()

funciones=(opcionA, opcionB, opcionC, opcionD)
menu( funciones )





"""
###########################
tipo_saludo=input("Tipo de saludo: ")
if tipo_saludo=="e":
    saludo=saludoEfusivo
else:
    saludo=saludoNormal
    
    
saludo(usuario)
"""