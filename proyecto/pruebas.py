from ping import ping

class Prueba:
    def __init__(self,nombre, timeout):
        self.nombre=nombre
        self.timeout=timeout
    
    def ejecutar(self):
        pass 
    
    
class PruebaPing(Prueba):
    def __init__(self, servidor, intentos, timeout):
        super().__init__("Prueba de ping sobre el servidor "+servidor.nombre, timeout)
        self.servidor=servidor
        self.intentos=intentos

    def ejecutar(self):    
        for ip in self.servidor.ips:
            resultado=False
            for intento in range(0,self.intentos):
                resultado = ping(ip, self.timeout)
                if resultado: 
                    break
            # Llegados a este punto habria hecho los intento que me han dicho para conseguir un ping satisfactorio
            # Y te go el resultado en una variable TRUE | FALSE
            