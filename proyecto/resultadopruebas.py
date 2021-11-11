from datetime import datetime

class ResultadoPrueba:
    def __init__(self,resultado ,info_extra):
        self.resultado=resultado
        self.info_extra=info_extra
        self.timestamp=datetime.now()

class ResultadoPruebaPing(ResultadoPrueba):
    def __init__(self,resultado ,info_extra, servidor, ip):
        super().__init__(resultado ,info_extra)
        self.servidor=servidor
        self.ip=ip
    
    def __repr__(self):  # Mostrarlo como texto cuando está dentro de una coleccion (lista, diccionario)
        return self.__str__()
        
    def __str__(self):   # Convertirlo a un texto
        representacion="Resultado de una prueba de ping:\n"
        representacion+="  Fecha/Hora:     "+str(self.timestamp)+"\n"
        representacion+="  Servidor:       "+self.servidor.nombre+"\n"
        representacion+="  IP:             "+self.ip+"\n"
        representacion+="  Resultado:      "+("OK" if self.resultado else "NOK")+"\n"
        representacion+="  Observaciones:  "+str(self.info_extra)+"\n"
        return representacion
