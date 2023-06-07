from clasepersonal import Personal

class Apoyo(Personal):
    __categotria=int
    __porcentaje=10

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad,categoria,porcentaje=10):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__categotria=categoria
        self.__porcentaje=porcentaje

    def getCategoria(self):
        return self.__categotria
    def getSueldobasico(self):
        return super().getSueldobasico()
    def getAntiguedad(self):
        return super().getAntiguedad()
    def getApellido(self):
        return super().getApellido()
    def getCuil(self):
        return super().getCuil()
    def getNombre(self):
        return super().getNombre()
    def getPorcentaje(self):
        return self.__porcentaje
    
    def modificarPorcentajeporcategoria(self,nuevoPorcentaje):
        self.__porcentaje=nuevoPorcentaje
        print('Porcentaje modificado ')

    def getSueldo(self):
        sueldo=0
        if int(self.getCategoria())>=1 and int(self.getCategoria())<=10:
            porcentaje=self.__porcentaje
        elif int(self.getCategoria())>=11 and int(self.getCategoria())<=20:
            porcentaje=float(self.__porcentaje*2)
        elif int(self.getCategoria())>=21 and int(self.getCategoria())<=22:
            porcentaje=float(self.__porcentaje*3)
        sueldo=float(self.getSueldobasico()+float(self.getAntiguedad()*self.getSueldobasico()/100))
        sueldo=float(sueldo+porcentaje*sueldo/100)    
        return sueldo

    def __str__(self):
        return super().__str__()+'Categoria:{}'.format(self.__categotria)    