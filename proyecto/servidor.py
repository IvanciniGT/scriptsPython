import yaml 
from parametros import Parametros

class Servidor:

    servidores={}

    @classmethod
    def cargarServidores(cls):
        fichero=Parametros.parametros["FICHERO"]
        with open (fichero,"r") as fichero_yaml:
            contenido=yaml.load(fichero_yaml, Loader=yaml.FullLoader)
        for diccionario_servidor in contenido["servers"]:
            nuevo_servidor = Servidor( diccionario_servidor["name"]  , diccionario_servidor["ips"] )
            Servidor.servidores[nuevo_servidor.nombre] = nuevo_servidor
        

    def __init__(self, un_nombre, unas_ips ): 
        self.nombre=un_nombre
        self.ips=unas_ips

