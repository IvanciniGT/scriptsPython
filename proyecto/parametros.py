
import sys
import os

class Parametros:
    
    parametros={}
    
    @classmethod
    def cargarParametros(cls):
        parametros={"FICHERO":None, "PING_RETRIES": 5, "PING_TIMEOUT": 1000}
        posicion_argumento=1
        while posicion_argumento< len(sys.argv):
            if sys.argv[posicion_argumento] == "-f" or  sys.argv[posicion_argumento] == "--servers-file":
                if len(sys.argv) > posicion_argumento+1:
                    parametros["FICHERO"]=sys.argv[posicion_argumento+1]
                else:
                    print("Argumento incompleto '"+sys.argv[posicion_argumento]+"'. Falta el nombre del fichero")
                    exit(1)
                posicion_argumento+=1
        
            elif sys.argv[posicion_argumento] == "-r" or  sys.argv[posicion_argumento] == "--ping-retries":
                if len(sys.argv) > posicion_argumento+1:
                    parametros["PING_RETRIES"]=int(sys.argv[posicion_argumento+1])
                else:
                    print("Argumento incompleto '"+sys.argv[posicion_argumento]+"'. Falta el numero de reintentos")
                    exit(1)
                posicion_argumento+=1
        
            elif sys.argv[posicion_argumento] == "-t" or  sys.argv[posicion_argumento] == "--ping-timeout":
                if len(sys.argv) > posicion_argumento+1:
                    parametros["PING_TIMEOUT"]=int(sys.argv[posicion_argumento+1])
                else:
                    print("Argumento incompleto '"+sys.argv[posicion_argumento]+"'. Falta el timeout")
                    exit(1)
                posicion_argumento+=1
            posicion_argumento+=1
        
        
        if parametros["FICHERO"] is None:
            print("No ha suministrado el fichero de servidores.")
            exit(3)
        # Asegurarnos que el fichero existe
        if not os.path.exists(parametros["FICHERO"]):
            print("El fichero de servidores no existe. Reviselo!")
            exit(2)
        Parametros.parametros=parametros