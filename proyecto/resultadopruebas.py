from datetime import datetime

class ResultadoPrueba:
    def __init__(self,resultado ,info_extra):
        self.resultado=resultado
        self.info_extra=info_extra
        self.timestamp=datetime.now()

class ResultadoPruebaPing(ResultadoPrueba):
    def __init__(self,resultado ,info_extra):
        super().__init__(resultado ,info_extra):
