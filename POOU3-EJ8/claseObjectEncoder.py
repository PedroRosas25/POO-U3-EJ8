import json
from pathlib import Path

class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Lista':
                listaPersonales = class_()
                vehiculos = d['comienzo']
                for i in range(len(vehiculos)):
                    dpersonal = vehiculos[i]
                    class_name = dpersonal.pop("_class_")
                    class_= eval(class_name)
                    atributos = dpersonal["_atributos_"]
                    unPersonal = class_(**atributos)
                    listaPersonales.agregarElemento(unPersonal)              
                return listaPersonales
    
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:json.dump(diccionario, destino, indent=4)
        destino.close()
    
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:diccionario=json.load(fuente)
        fuente.close()
        return diccionario
    
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)