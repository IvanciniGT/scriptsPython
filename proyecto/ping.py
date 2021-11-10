from subprocess import run, PIPE
import platform     # Obtener información del SO donde estamos corriendo el programa


def ping(servidor):
    parametro="-n" if platform.system().upper() == "WINDOWS" else "-c"
    comando=( "ping" , parametro , "1", servidor )
    resultado_de_su_ejecucion=run( comando , stdout=PIPE , stderr=PIPE)
    return resultado_de_su_ejecucion.returncode==0

#print(   ping("google.es")   )
#print(   ping("googlecito.es")   )
