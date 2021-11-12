from jinja2 import Template
# pip3 install jinja2
import stat
import os

servicios=("SSHD","HHTPD","MYSQL")

### Generación del codigo del script
#contenido_script="#!/bin/bash\n\n"

#for servicio in servicios:
#    contenido_script+='SALIDA=$( systemctl status '+servicio+' | grep -c "active (running)" )\n\n'
    
#    contenido_script+="if [[ $SALIDA == 0 ]]; then\n"
#    contenido_script+="    echo El servicio "+servicio+" no está disponible\n"
#    contenido_script+="    exit 1\n"
#    contenido_script+="fi\n\n"

with open("plantilla_script.j2", "r") as archivo_plantilla:
    contenido_de_la_plantilla=archivo_plantilla.read()

plantilla = Template( contenido_de_la_plantilla )
contenido_script=plantilla.render( { "servicios": servicios } )

### Guardado del script y establecimiento de permisos
with open("script_resultante.sh","w") as script:
    script.write(contenido_script)

permisos_actuales=os.stat("./script_resultante.sh").st_mode
os.chmod("script_resultante.sh",  permisos_actuales | stat.S_IXUSR | stat.S_IXGRP )
