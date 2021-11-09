
def sinput(pregunta, intentos, valor_por_defecto="NADA"):
    
    # Voy a intentar sacar un valor del usuario...
    # Para ello, mientras le queden reintentos disponibles, le preguntaré por un valor
    while intentos > 0:
        valor_del_usuario=input(pregunta)
        # Comprobar si se ha escrito algo
        if len(valor_del_usuario) > 0:
            # Si se ha escrito algo, que hago? lo devuelvo
            return valor_del_usuario
        else:
            # Si no se ha escrito nada, vuelvo a preguntar... mientras le queden reintentos
            intentos=intentos - 1
    
    
nombre=sinput("Como se llama el servidor que quieres reiniciar? ",3 , "localhost")
print(nombre)

servicio=sinput("Que servicio desea reiniciar? ",3 )
print(servicio)

reinicio=sinput("Estás seguro que quieres reiniciar el servidor? ",2 , "si")
print(reinicio)


