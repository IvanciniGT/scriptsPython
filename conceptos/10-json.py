import json

with open ("modificado.json","r") as fichero_json:
    contenido=json.load(fichero_json)
    print(contenido)
    
    contenido['servers'].append({ "name": "Facebook", "ips": ["facebook.es"] })
    
    
with open ("modificado.json","w") as fichero_json:
    json.dump(contenido,fichero_json)
    