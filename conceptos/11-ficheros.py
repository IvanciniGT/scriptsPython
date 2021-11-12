apuntador_al_archivo = open("escritura.txt","w")
apuntador_al_archivo.writelines( ("Esta es la primera linea\n", "Esta es la segunda linea\n") )
apuntador_al_archivo.write( "Esta es la tercera linea\n" )
apuntador_al_archivo.close()

with open("escritura.txt","w") as apuntador_al_archivo:
    apuntador_al_archivo.writelines( ("Esta es la primera linea\n", "Esta es la segunda linea\n") )
    apuntador_al_archivo.write( "Esta es la tercera linea\n" )

with open("escritura.txt","a") as apuntador_al_archivo:
    apuntador_al_archivo.write( "Esta es una nueva linea\n" )

# Comprobar si existe
import os

try:
    if os.path.exists("escritura.txt") :
        with open("escritura.txt","r") as apuntador_al_archivo:
            while True:
                linea=apuntador_al_archivo.readline()
                if len(linea) == 0:
                    break
                print("> "+linea[:-1])
except FileNotFoundError:
    print("PROBLEMA AL ABRIR EL ARCHIVO: El archivo no existe")
except PermissionError:
    print("PROBLEMA AL ABRIR EL ARCHIVO: El archivo no tiene los permisos adecuados")
except :
    print("PROBLEMA AL ABRIR EL ARCHIVO: Problema desconocido")
else:
    print("Codigo se he conseguido abrir bien el archivo")
finally:
    print("Codigo que se debe ejecutar siempre")

# CARPETAS
os.mkdir("./ejemplo")
input("Carpeta creada. PULSE ENTER PARA BORRARLA")
os.rmdir("./ejemplo")

# PERMISOS
import stat
datos_path=os.stat("./escritura.txt").st_mode
print(stat.filemode(datos_path))
print("Es un directorio: "+ str(stat.S_ISDIR(datos_path)))
os.chmod("escritura.txt",  datos_path | stat.S_IWOTH )
print(datos_path & stat.S_IRWXU)

"""
rwx
USR  GRP  OTH
001  110  100    PERMISOS ORIGINALES
010  100  000    MASCARA                AND &     OR  |
011  110  100

000 -> 0
001 -> 1 Ejecucion
010 -> 2 Escritura
100 -> 4 Lectura


Todos: 7
    Lectura: 4
    Escritura: 2
    Ejecución: 1
Lectura y Escritura: 6
Escritura y Ejecución: 3
Lectura y Ejecucion: 5


001  110  100    PERMISOS ORIGINALES
000  000  111       &   |
000  000  100
"""