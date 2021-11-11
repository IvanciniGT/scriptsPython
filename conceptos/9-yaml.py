import yaml
# Selenium
# Pandas
# Numpy
# Fabrik
# yaml - pyyaml

with open ("prueba.yaml","r") as fichero_yaml:
    contenido=yaml.load(fichero_yaml, Loader=yaml.FullLoader)
    print(contenido)
    
    contenido['servers'].append({ "name": "Facebook", "ips": ["facebook.es"] })
    
    
class Prueba:
        def __init__(self, numero):
            self.numero=numero

with open ("modificado.yaml","w") as fichero_yaml:
    yaml.dump(Prueba(7),fichero_yaml)
    
with open ("modificado.yaml","r") as fichero_yaml:
    valor=yaml.load(fichero_yaml, Loader=yaml.FullLoader)
    print(valor)
    
    