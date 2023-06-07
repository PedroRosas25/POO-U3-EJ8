from clasepersonal import Personal

class Investigador(Personal):
    __area=str
    __tipo=str

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad,area,tipo):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__area=area
        self.__tipo=tipo

    def getArea(self):
        return self.__area
    def getTipo(self):
        return self.__tipo
    def getAntiguedad(self):
        return super().getAntiguedad()
    def getApellido(self):
        return super().getApellido()
    def getCuil(self):
        return super().getCuil()
    def getNombre(self):
        return super().getNombre()
    def getSueldobasico(self):
        return super().getSueldobasico()
    def getSueldo(self):
        sueldo=0
        sueldo=float(self.getSueldobasico()+float(self.getAntiguedad()*self.getSueldobasico()/100))
        return sueldo
    
    def __str__(self):
        return super().__str__()+'Area:{} Tipo:{}'.format(self.__area,self.__tipo)