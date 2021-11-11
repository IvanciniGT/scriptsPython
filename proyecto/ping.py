from subprocess import run, PIPE
import platform     # Obtener información del SO donde estamos corriendo el programa


def ping(servidor, timeout):
    # Asumo que es windows
    parametro_numero_pings="-n"
    parametro_timeout="-w"

    if platform.system().upper() != "WINDOWS": # Si fuera unix / linux / POSIX
        parametro_numero_pings="-c"
        parametro_timeout="-W"
        timeout/=1000    

    comando=( "ping" , parametro_numero_pings , "1",parametro_timeout , str(timeout), servidor )
    resultado_de_su_ejecucion=run( comando , stdout=PIPE , stderr=PIPE)
    return (resultado_de_su_ejecucion.returncode==0, resultado_de_su_ejecucion.stderr)
