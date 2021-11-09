from menu import menu


def altaServicio():
    print("Alta de servicio")
    input("Pulse ENTER para continuar...")

def bajaServicio():
    print("Baja de servicio")
    input("Pulse ENTER para continuar...")

def gestionDeServicios():
    TITULO_MENU="Submenu de gestión de servicios"
    OPCIONES_MENU=( "Alta de servicio" , "Baja de servicio", "Volver al menu principal" )
    FUNCIONES_A_EJECUTAR=(altaServicio, bajaServicio )
    menu(TITULO_MENU, OPCIONES_MENU, FUNCIONES_A_EJECUTAR)

def estadoDeLosServicios():
    print("ESTADO DE LOS SERVICIOS")
    input("Pulse ENTER para continuar...")

TITULO_MENU="Menu principal"
OPCIONES_MENU=( "Gestión de servicios" , "Monitorización de servicios", "Salir" )
FUNCIONES_A_EJECUTAR=(gestionDeServicios, estadoDeLosServicios )
menu(TITULO_MENU, OPCIONES_MENU, FUNCIONES_A_EJECUTAR)
