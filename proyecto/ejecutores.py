class PoolDeEjecutores:
    # Creare un determinado pool de ejecutores para realizar una determinada tarea
    # Sobre un determinado conjunto de cosas
    # Y diré cuantos ejecutores quiero en ese pool
    
    # Comience a trabajar
    # Habrán terminado el trabajo? cuando no queden tareas por realizar

class Ejecutor(Thread):
    
    # En su ejecución, obtendrá un elemento de los que queden pro procesar, 
    # ejecutara la tearea que se le haya encomendado
    # Y cuando no queden mas tareas por realizar terminara.