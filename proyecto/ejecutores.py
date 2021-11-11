from threading import Thread

class PoolDeEjecutores:
    
    def __init__(self, numero_de_ejecutores, lista_tareas, funcion_a_ejecutar_en_cada_tarea):
        self.numero_de_ejecutores=numero_de_ejecutores
        self.lista_tareas=lista_tareas
        self.funcion_a_ejecutar_en_cada_tarea=funcion_a_ejecutar_en_cada_tarea
        self.listado_ejecutores=[]
        
    def comenzarTrabajos(self):
        for ejecutor in range(0,self.numero_de_ejecutores):
            nuevo_ejecutor=Ejecutor( self.lista_tareas, self.funcion_a_ejecutar_en_cada_tarea )
            self.listado_ejecutores.append( nuevo_ejecutor )
            nuevo_ejecutor.start()

    def avisaCuandoAcabes(self):
        for ejecutor in self.listado_ejecutores:
            ejecutor.join()
    
    #def trabajoAcabado():
    #    #return len(lista_tareas)==0
    #    for ejecutor in self.listado_ejecutores:
    #        if ejecutor.is_alive():
    #            return False
    #    return True
        

class Ejecutor(Thread):
    
    def __init__(self, lista_tareas, funcion_a_ejecutar):
        super().__init__()
        self.lista_tareas=lista_tareas
        self.funcion_a_ejecutar=funcion_a_ejecutar  # ejecutar
        
    def run(self):
        while True:
            una_tarea_a_ejecutar= None
            try:
                if len (self.lista_tareas) != 0 
                    una_tarea_a_ejecutar=self.lista_tareas.pop()
            except IndexError:
                return 
            else:
                if una_tarea_a_ejecutar is not None:
                    # Ejecutar la tarea
                                                # Me permite recuperar la referencia a una función
                                                # de un objeto a través de su nombre
                    referencia_funcion_a_ejecutar=getattr(una_tarea_a_ejecutar, self.funcion_a_ejecutar)
                    referencia_funcion_a_ejecutar()            
