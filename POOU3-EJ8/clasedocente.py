from clasepersonal import Personal
class Docente(Personal):
    __carrera=str
    __cargo=str
    __catedra=str
    __porcentaje=10

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad,carrera,cargo,catedra,porcentaje=10):
        Personal.__init__(self,cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
        self.__porcentaje=porcentaje
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    def getCuil(self):
        return super().getCuil()
    def getApellido(self):
        return super().getApellido()
    def getNombre(self):
        return super().getNombre()
    def getSueldobasico(self):
        return super().getSueldobasico()
    def getAntiguedad(self):
        return super().getAntiguedad()   
    def getPorcentaje(self):
        return self.__porcentaje
    
    def modificarPorcentajeporcargo(self,nuevoPorcentaje):
        self.__porcentaje=nuevoPorcentaje
        print('Porcentaje modificado ')

    def getSueldo(self):
        sueldo=0
        porcentaje=0
        if self.__cargo=='simple':
           porcentaje=float(self.__porcentaje)
        elif self.__cargo=='semiesxclusivo':
            porcentaje=float(self.__porcentaje*2)
        elif self.__cargo=='exclusivo':
            porcentaje=float(self.__porcentaje*5)
        sueldo=float(self.getSueldobasico()+float(self.getAntiguedad()*self.getSueldobasico()/100))
        sueldo=float(sueldo+porcentaje*sueldo/100)
        return sueldo           

    def __str__(self):
        return super().__str__()+'Carrera:{} Cargo:{} Catedra:{}'.format(self.__carrera,self.__cargo,self.__catedra) 