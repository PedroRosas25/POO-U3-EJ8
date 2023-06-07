from clasedocente import Docente
from claseinvestigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    __categoriaincent=str
    __importeextra=float

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, area, tipo, categoriaincent, importeextra):
        Docente.__init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra)
        Investigador.__init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, area, tipo)
        self.__categoriaincent = categoriaincent
        self.__importeextra = importeextra

    def getCategoriaincent(self):
        return self.__categoriaincent
    def getImporteextra(self):
        return self.__importeextra
    def getTipo(self):
        return super().getTipo()
    def getAntiguedad(self):
        return super().getAntiguedad()
    def getApellido(self):
        return super().getApellido()
    def getArea(self):
        return super().getArea()
    def getCargo(self):
        return super().getCargo()
    def getCarrera(self):
        return super().getCarrera()
    def getCatedra(self):
        return super().getCatedra()
    def getCuil(self):
        return super().getCuil()
    def getNombre(self):
        return super().getNombre()
    def getSueldobasico(self):
        return super().getSueldobasico()
    def getSueldo(self):
        sueldo=0
        sueldo=float(Docente.getSueldo(self)+self.__importeextra)
        return sueldo
    
    def modificarImporteExtra(self,nuevoImporteExtra):
        self.__importeextra=nuevoImporteExtra
        print('Se modifico el importe extra ')

    def __str__(self):
        return super().__str__()+'Categoriaincentivo:{} Importeextra:{}'.format(self.__categoriaincent,self.__importeextra)
    
    def __gt__(self,otro):
        return self.getNombre()>otro.getNombre()
