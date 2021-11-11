from sinput import sinput

sangrado=" "*10

def mostrarTextoSangrado(texto):
    print(sangrado+ texto)
    
def menu(TITULO_MENU,OPCIONES_MENU, FUNCIONES):
    opcion_del_usuario=None
    while opcion_del_usuario!="0":
        # Borro la pantalla
        print("\n"*60)
        
        # Mostrando el titulo del menu
        print("-"*60)
        mostrarTextoSangrado(TITULO_MENU)
        print("-"*60)
        print()
        
        # Saco todas las opciones de menu normales
        for numero_opcion in range(0,len(OPCIONES_MENU)-1):
            mostrarTextoSangrado(str(numero_opcion+1)+" - "+OPCIONES_MENU[numero_opcion])
        
        # Mostraría la opción 0... la de salir
        print()
        mostrarTextoSangrado("0 - "+OPCIONES_MENU[-1])
        print()
    
        #Pregunta:     Elija una opción (0|1|2) [0]:      # Que opciones son válidas? 0-2                
        print("-"*60)
        print()
        opcion_del_usuario=sinput(sangrado+"Opcion elegida",
                patron_validacion="^[0-"+str(len(OPCIONES_MENU)-1)+"]$",
                valor_por_defecto="0",
                intentos=1
              )
        
        # Procesamos la opcion_del_usuario
        opcion_a_ejecutar=int(opcion_del_usuario)-1
        if opcion_a_ejecutar != -1 :
            FUNCIONES[opcion_a_ejecutar]()
###################
