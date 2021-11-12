#!/bin/bash

# El script debe acabar con un exit code 0 si todos los servicios que quiero comprobar están arrancados
# Debe acabar con un exit code 1 si alguno de los servicios no está arrancado
SALIDA=$( systemctl status sshd | grep -c "active (running)" )

if [[ $SALIDA == 0 ]]; then
    echo El servicio sshd no está disponible
    exit 1
fi
