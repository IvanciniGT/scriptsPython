
def sinput(pregunta, intentos=1, valor_por_defecto=None):
    valor_a_devolver=None
    # Voy a intentar sacar un valor del usuario...
    # Para ello, mientras le queden reintentos disponibles y no haya conseguido yo un valor
    # le preguntaré por un valor
    while intentos > 0 and valor_a_devolver is None:
        valor_del_usuario=input(pregunta+"? ")
        # Si el usuario al preguntarle SOLO PULSA ENTER, la variable valor_del_usuario contendrá un texto vacio: ""
        # Comprobar si se ha escrito algo
        if len(valor_del_usuario) > 0:
            # Si se ha escrito algo,  lo devuelvo
            valor_a_devolver=valor_del_usuario
        elif valor_por_defecto is not None:
            # Si no ha escrito nada y hay un valor por defecto, devuelvo el valor por defecto
            valor_a_devolver=valor_por_defecto
        else:
            # Si no se ha escrito nada, y no hay valor por defecto vuelvo a preguntar... 
            # mientras le queden reintentos
            intentos=intentos - 1
    return valor_a_devolver
        
    # No sale el valor por defecto en el prompt

nombre=sinput("Como se llama el servidor que quieres reiniciar", valor_por_defecto="localhost")
print(nombre)

servicio=sinput("Que servicio desea reiniciar", intentos=3 )
print(servicio)

reinicio=sinput("Estás seguro que quieres reiniciar el servidor", valor_por_defecto="si")
print(reinicio)


