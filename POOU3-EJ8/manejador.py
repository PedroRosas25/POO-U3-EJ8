from zope.interface import implementer
from claseapoyo import Apoyo
from clasedocente import Docente
from claseinvestigador import Investigador
from clasedocenteinvestigador import DocenteInvestigador
from interface import IPersonal
from interfacedirector import IDirector
from interfacetesorero import ITesorero
from claselista import Lista
from claseObjectEncoder import ObjectEncoder

@implementer(IPersonal,IDirector,ITesorero)
class Manejador:
    __lista=Lista()

    def __init__(self):
        self.__lista=Lista()

    def insertarelemento(self,personal,indice):
        self.__lista.agregarPersonalIndice(personal,indice)
    def agregarelemento(self,personal):
        self.__lista.agregarPersonalFinal(personal)
    def mostrarelemento(self,indice):
        self.__lista.getTipo(indice)

    def toJSON(self):
        json=ObjectEncoder()
        d=self.__lista.toJSON()
        json.guardarJSONArchivo(d,'personal2.json')        

    def ordenarymostrar(self,carrerax):
        self.__lista.ordenarymostrar(carrerax)    

    def contarymostrar(self,areax):
        self.__lista.contarymostrar(areax)    

    def ordenarycalcular(self):
        self.__lista.ordenarycalcular()

    def mostrarporcategoria(self,categoriax):
        self.__lista.mostrarporcategoria(categoriax)    

    def gastosSueldoPorEmpleado(self,cuil):
        self.__lista.gastosSueldoPorEmpleado(cuil)    
    def modificarBasico(self,cuil,nuevoBasico):
        self.__lista.modificarBasico(cuil,nuevoBasico)
    def modificarPorcentajeporcargo(self,cuil, nuevoPorcentaje):
        self.__lista.modificarPorcentajeporcargo(cuil,nuevoPorcentaje)
    def modificarPorcentajeporcategoria(self,cuil, nuevoPorcentaje):
        self.__lista.modificarPorcentajeporcategoria(cuil,nuevoPorcentaje)
    def modificarImporteExtra(self,cuil, nuevoImporteExtra):
        self.__lista.modificarImporteExtra(cuil,nuevoImporteExtra)


    def cargarlista(self):
        json=ObjectEncoder()
        diccionario=json.leerJSONArchivo('personal.json') 
        personales=json.decodificarDiccionario(diccionario)
        for personal in personales:
            cuil=str(personal['cuil'])
            apellido=str(personal['apellido'])
            nombre=str(personal['nombre'])
            sueldobasico=float(personal['sueldobasico'])
            antiguedad=int(personal['antiguedad'])
            tipo=str(personal['tipo'])

            if tipo=='docente':
                carrera=str(personal['carrera'])
                cargo=str(personal['cargo'])
                catedra=str(personal['catedra'])
                unpersonal=Docente(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra)
                self.agregarelemento(unpersonal)
            elif tipo=='personal de apoyo':
                categoria=str(personal['categoria'])
                unpersonal=Apoyo(cuil,apellido,nombre,sueldobasico,antiguedad,categoria)
                self.agregarelemento(unpersonal)
            elif tipo=='investigador':
                area=str(personal['area'])
                tipoin=str(personal['tipoinvestigacion'])
                unpersonal=Investigador(cuil,apellido,nombre,sueldobasico,antiguedad,area,tipoin)
                self.agregarelemento(unpersonal)
            elif tipo=='docente investigador':
                carrera=str(personal['carrera'])
                cargo=str(personal['cargo'])
                catedra=str(personal['catedra'])        
                area=str(personal['area'])
                tipoin=str(personal['tipoinvestigacion'])
                categ=str(personal['categoriainvestigacion'])
                importeextra=float(personal['importeextra'])
                unpersonal=DocenteInvestigador(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area,tipoin,categ,importeextra)
                self.agregarelemento(unpersonal)

    def mostrartodos(self):
        self.__lista.mostrartodos()

