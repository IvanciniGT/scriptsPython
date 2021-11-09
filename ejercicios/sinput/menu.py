from sinput import sinput

TITULO_MENU="Menu principal"

OPCIONES_MENU=( "Gestion de servicios" , "Estado de los servicios", "Salir" )
sangrado=" "*10

def gestionDeServicios():
    print("GESTION DE SERVICIOS")
    input("Pulse ENTER para continuar...")

def estadoDeLosServicios():
    print("ESTADO DE LOS SERVICIOS")
    input("Pulse ENTER para continuar...")

def mostrarTextoSangrado(texto):
    print(sangrado+ texto)
    
def menuPrincipal():
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
    
    
    
#                Si el usuario introduce un valor invalido... le aviso y le vuelvo a mostrar el menu y a preguntarle    
#    0 El programa acaba
#    1-gestionDeServicios()
#    2-estadoDeLosServicios()

menuPrincipal()

