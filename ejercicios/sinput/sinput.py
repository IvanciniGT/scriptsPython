import re 

def sinput(pregunta, intentos=1, valor_por_defecto=None, respuestas_posibles=None, patron_validacion=None):
    valor_a_devolver=None
    
    # Voy a preparar la pregunta a mostrar al usuario
    texto_a_preguntar=pregunta
    # Añadir los valores posibles, si existen
    if respuestas_posibles is not None:
        texto_a_preguntar+=" ("
        for respuesta_posible in respuestas_posibles:
            texto_a_preguntar+=respuesta_posible+"|"
        # Se que me queda una barrita de más
        texto_a_preguntar=texto_a_preguntar[:-1]+")"
        
    # Añadir el valor por defecto a la pregunta si existe
    if valor_por_defecto is not None:
        texto_a_preguntar=texto_a_preguntar+" ["+valor_por_defecto+"]" 
    texto_a_preguntar=texto_a_preguntar+"? "
    
    # Voy a intentar sacar un valor del usuario...
    # Para ello, mientras le queden reintentos disponibles y no haya conseguido yo un valor
    # le preguntaré por un valor
    while intentos > 0 and valor_a_devolver is None:
        #valor_del_usuario=input(pregunta+(" ["+valor_por_defecto+"]" if valor_por_defecto is not None else "")+"? ")
        valor_del_usuario=input(texto_a_preguntar)
        # Si el usuario al preguntarle SOLO PULSA ENTER, la variable valor_del_usuario contendrá un texto vacio: ""
        # Comprobar si se ha escrito algo
        if len(valor_del_usuario) > 0:
            # Si el usuario ha escrito algo
            
            # Si hay respuestas posibles, tendria que mirar si el valor que me ha dado el usuario
            # está dentro de los permitidos
            if respuestas_posibles is not None and valor_del_usuario not in respuestas_posibles:
                print("El valor introducido '"+valor_del_usuario+"' no es válido.")
            
            # Si hay un patron, debemos validarlo
            elif patron_validacion is not None and not re.match(patron_validacion, valor_del_usuario):
                print("El valor introducido '"+valor_del_usuario+"' no es válido.")
            else:
                # Todo está bien, ya tengo valor. EUREKA !!!
                valor_a_devolver=valor_del_usuario
        elif valor_por_defecto is not None:
            # Si no ha escrito nada y hay un valor por defecto, devuelvo el valor por defecto
            valor_a_devolver=valor_por_defecto
        # Le quito un intento
        intentos=intentos - 1
    return valor_a_devolver
        
    # No sale el valor por defecto en el prompt

