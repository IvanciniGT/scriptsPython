#!/bin/bash


SALIDA=$( systemctl status sshd | grep -c "active (running)" )

if [[ $SALIDA == 0 ]]; then
    echo El servicio SSHD no está disponible
    exit 1
fi

SALIDA=$( systemctl status hhtpd | grep -c "active (running)" )

if [[ $SALIDA == 0 ]]; then
    echo El servicio HHTPD no está disponible
    exit 1
fi

SALIDA=$( systemctl status mysql | grep -c "active (running)" )

if [[ $SALIDA == 0 ]]; then
    echo El servicio MYSQL no está disponible
    exit 1
fi
