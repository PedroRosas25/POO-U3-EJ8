from clasepersonal import Personal
from claseapoyo import Apoyo
from clasedocente import Docente
from claseinvestigador import Investigador
from clasedocenteinvestigador import DocenteInvestigador
class Nodo:
    __personal:Personal
    __siguiente:object

    def __init__(self,personal):
        self.__personal=personal
        self.__siguiente=None
    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__personal
    
    def getTipo(self):
        tipo=''
        if isinstance(self.__personal,Apoyo):
            tipo=type(self.__personal)
            print('El personal con posicion ingresada es Personal de apoyo \n')
        elif isinstance(self.__personal,DocenteInvestigador):
            tipo=type(self.__personal)
            print('El personal con posicion ingresada es Personal docente investigador \n')    
        elif isinstance(self.__personal,Docente):
            tipo=type(self.__personal)
            print('El personal con posicion ingresada es Personal docente \n')
        elif isinstance(self.__personal,Investigador):
            tipo=type(self.__personal)
            print('El personal con posicion ingresada es Personal investigador \n')   
        return tipo    
    
    def getTipo2(self):
        tipo=''
        if isinstance(self.__personal,Apoyo):
            tipo='Apoyo'
        elif isinstance(self.__personal,DocenteInvestigador):
            tipo='DocenteInvestigador'      
        elif isinstance(self.__personal,Docente):
            tipo='Docente'
        elif isinstance(self.__personal,Investigador):
            tipo='Investigador'
        return tipo    

    def getCarrera(self):
        if isinstance(self.__personal,DocenteInvestigador):
            return self.__personal.getCarrera()

    def getNombre(self):
        return self.__personal.getNombre()
    def getApellido(self):
        return self.__personal.getApellido()
    def getSueldo(self):
        sueldo=0
        if isinstance(self.__personal,Apoyo):
            sueldo=self.__personal.getSueldo()
        elif isinstance(self.__personal,DocenteInvestigador):
            sueldo=self.__personal.getSueldo()
        elif isinstance(self.__personal,Docente):
            sueldo=self.__personal.getSueldo()
        elif isinstance(self.__personal,Investigador):
            sueldo=self.__personal.getSueldo()  
        return sueldo  
    def getCuil(self):
        return self.__personal.getCuil()

    def getCategoriaInve(self):
        if isinstance(self.__personal,DocenteInvestigador):
            return self.__personal.getCategoriaincent()
    def getImporteextra(self):
        if isinstance(self.__personal,DocenteInvestigador):
            return self.__personal.getImporteextra()    
    def modificarBasico(self,nuevoBasico):
        self.__personal.modificarBasico(nuevoBasico)
    def modificarPorcentajeporcargo(self,nuevoPorcentaje):
        if isinstance(self.__personal,Docente):
            self.__personal.modificarPorcentajeporcargo(nuevoPorcentaje)
    def modificarPorcentajeporcategoria(self,nuevoPorcentaje):
        if isinstance(self.__personal,Apoyo):
            self.__personal.modificarPorcentajeporcategoria(nuevoPorcentaje)  
    def modificarImporteExtra(self,nuevoImporteExtra):
        if isinstance(self.__personal,DocenteInvestigador):
            self.__personal.modificarImporteExtra(nuevoImporteExtra)           

    def __gt__(self,otro):
        return self.getApellido()>otro.getApellido()

    def getArea(self):
        if isinstance(self.__personal,DocenteInvestigador) or isinstance(self.__personal,Investigador):
            return self.__personal.getArea()

    def toJSON(self):
        if isinstance(self.__personal,Apoyo):
           d=dict(tipo='personal de apoyo',cuil=self.__personal.getCuil(),apellido=self.__personal.getApellido(),nombre=self.__personal.getNombre(),sueldobasico=self.__personal.getSueldobasico(),antiguedad=self.__personal.getAntiguedad(),categoria=self.__personal.getCategoria()) 
        elif isinstance(self.__personal,DocenteInvestigador):
            d=dict(tipo='docente investigador',cuil=self.__personal.getCuil(),apellido=self.__personal.getApellido(),nombre=self.__personal.getNombre(),sueldobasico=self.__personal.getSueldobasico(),antiguedad=self.__personal.getAntiguedad(),carrea=self.__personal.getCarrera(),cargo=self.__personal.getCargo(),catedra=self.__personal.getCatedra(),area=self.__personal.getArea(),tipoinvestigacion=self.__personal.getTipo(),categoriainvestigacion=self.__personal.getCategoriaincent(),importeextra=self.__personal.getImporteextra(),)
        elif isinstance(self.__personal,Docente):
            d=dict(tipo='docente',cuil=self.__personal.getCuil(),apellido=self.__personal.getApellido(),nombre=self.__personal.getNombre(),sueldobasico=self.__personal.getSueldobasico(),antiguedad=self.__personal.getAntiguedad(),carrera=self.__personal.getCarrera(),cargo=self.__personal.getCargo(),catedra=self.__personal.getCatedra())
        elif isinstance(self.__personal,Investigador):
            d=dict(tipo='investigador',cuil=self.__personal.getCuil(),apellido=self.__personal.getApellido(),nombre=self.__personal.getNombre(),sueldobasico=self.__personal.getSueldobasico(),antiguedad=self.__personal.getAntiguedad(),area=self.__personal.getArea(),tipoinvestigacion=self.__personal.getTipo())
        return d                    