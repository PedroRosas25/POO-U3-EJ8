class Personal:
    __cuil=str
    __apellido=str
    __nombre=str
    __sueldobasico=float
    __antiguedad=int

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldobasico=sueldobasico
        self.__antiguedad=antiguedad

    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getSueldobasico(self):
        return self.__sueldobasico
    def getAntiguedad(self):
        return self.__antiguedad   
    def getSueldo(self):
        pass
    def modificarBasico(self,nuevoBasico):
        self.__sueldobasico=nuevoBasico
        print('Suledo basico modificado ')

    

    def __str__(self):
        return 'CUIL:{} Apellido:{} Nombre:{} Sueldobasico:{} Antiguedad:{} '.format(self.__cuil,self.__apellido,self.__nombre,self.__sueldobasico,self.__antiguedad)