from ping import ping
from resultadopruebas import ResultadoPruebaPing

class Prueba:
    def __init__(self,nombre, timeout):
        self.nombre=nombre
        self.timeout=timeout
        self.resultados_ejecuciones=[]
    
    def ejecutar(self):
        pass 
    
    
class PruebaPing(Prueba):
    def __init__(self, servidor, intentos, timeout):
        super().__init__("Prueba de ping sobre el servidor "+servidor.nombre, timeout)
        self.servidor=servidor
        self.intentos=intentos
    
    def ejecutar(self):
        resultados=[]
        for ip in self.servidor.ips:
            resultado=False
            for intento in range(0,self.intentos):
                resultado, info_extra = ping(ip, self.timeout)
                if resultado: 
                    break
            # Llegados a este punto habria hecho los intento que me han dicho para conseguir un ping satisfactorio
            # Y tengo el resultado en una variable TRUE | FALSE
            resultados.append( ResultadoPruebaPing( resultado, info_extra, self.servidor, ip) )
        self.resultados_ejecuciones.append(resultados)
        return resultados
            