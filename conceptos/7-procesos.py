#import re
#import time
#from threading from Thread

from subprocess import run, PIPE

comando=( "ls" , "-l", "/" )
resultado_de_su_ejecucion=run( comando , stdout=PIPE , stderr=PIPE)

print(resultado_de_su_ejecucion.returncode)
print(resultado_de_su_ejecucion.stdout)
print(resultado_de_su_ejecucion.stderr)