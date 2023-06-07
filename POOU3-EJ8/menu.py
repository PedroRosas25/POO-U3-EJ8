from claseapoyo import Apoyo
from clasedocente import Docente
from claseinvestigador import Investigador
from clasedocenteinvestigador import DocenteInvestigador
class Menu:
    __opcion=0

    def __init__(self):
        self.__opcion=0

    def opciones(self,m):
        while self.__opcion!=9:
            print('1--Insertar personal\n2--Agregar personal\n3--Mostrar tipo de personal\n4--Generar listado ordenado de docentes investigadores\n5--Contar docentes investigadores\n6--Generar listado ordenado de todo el personal\n7--Listar docente investigadores de categoria especifica\n8--Almacenar datos en archivo personal2.json\n')
            self.__opcion=int(input('Ingrese una opcion '))
            if self.__opcion==1:
                tipopersonal=str(input('Ingrese tipo de personal(apoyo,docente,investigador o docente investigador) '))
                cuil=str(input('Ingrese cuil '))
                apellido=str(input('Ingrese apellido '))
                nombre=str(input('Ingrese nombre '))
                sueldobasico=float(input('Ingrese sueldo basico '))
                antiguedad=int(input('Ingrese antiguedad '))
                if tipopersonal=='apoyo':
                   categoria=str(input('Ingrese categoria '))
                   unpersonal=Apoyo(cuil,apellido,nombre,sueldobasico,antiguedad,categoria)
                elif tipopersonal=='docente':
                     carrera=str(input('Ingrese carrea '))
                     cargo=str(input('Ingrese cargo '))
                     catedra=str(input('Ingrese catedra '))
                     unpersonal=Docente(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra)
                elif tipopersonal=='investigador':
                     area=str(input('Ingrese area de investigacion '))
                     tipo=str(input('Ingrese tipo de investigacion '))
                     unpersonal=Investigador(cuil,apellido,nombre,sueldobasico,antiguedad,area,tipo)
                elif tipopersonal=='docente investigador':
                     carrera=str(input('Ingrese carrea '))
                     cargo=str(input('Ingrese cargo '))
                     catedra=str(input('Ingrese catedra '))
                     area=str(input('Ingrese area de investigacion '))
                     tipo=str(input('Ingrese tipo de investigacion '))
                     categoriaincent=str(input('Ingrese categoria del incentivo ')) 
                     importeextra=float(input('Ingrese importe extra '))
                     unpersonal=DocenteInvestigador(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area,tipo,categoriaincent,importeextra)
                indice=int(input('Ingrese posicion a insertar el elemento '))
                m.insertarelemento(unpersonal,indice)     
                print('Personal insertado ')
                print('\n')

            elif self.__opcion==2:
                tipopersonal=str(input('Ingrese tipo de personal(apoyo,docente,investigador o docente investigador) '))
                cuil=str(input('Ingrese cuil '))
                apellido=str(input('Ingrese apellido '))
                nombre=str(input('Ingrese nombre '))
                sueldobasico=float(input('Ingrese sueldo basico '))
                antiguedad=int(input('Ingrese antiguedad '))
                if tipopersonal=='apoyo':
                   categoria=str(input('Ingrese categoria '))
                   unpersonal=Apoyo(cuil,apellido,nombre,sueldobasico,antiguedad,categoria)
                elif tipopersonal=='docente':
                     carrera=str(input('Ingrese carrea '))
                     cargo=str(input('Ingrese cargo '))
                     catedra=str(input('Ingrese catedra '))
                     unpersonal=Docente(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra)
                elif tipopersonal=='investigador':
                     area=str(input('Ingrese area de investigacion '))
                     tipo=str(input('Ingrese tipo de investigacion '))
                     unpersonal=Investigador(cuil,apellido,nombre,sueldobasico,antiguedad,area,tipo)
                elif tipopersonal=='docente investigador':
                     carrera=str(input('Ingrese carrea '))
                     cargo=str(input('Ingrese cargo '))
                     catedra=str(input('Ingrese catedra '))
                     area=str(input('Ingrese area de investigacion '))
                     tipo=str(input('Ingrese tipo de investigacion '))
                     categoriaincent=str(input('Ingrese categoria del incentivo ')) 
                     importeextra=float(input('Ingrese importe extra '))
                     unpersonal=DocenteInvestigador(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area,tipo,categoriaincent,importeextra)
                m.agregarelemento(unpersonal)
                print('Personal agregado')
                print('\n')     
            elif self.__opcion==3:
                indice=int(input('Ingrese posicion del personal '))
                m.mostrarelemento(indice)
                print('\n')
            elif self.__opcion==4:
                carerrax=str(input('Ingrese nombre de carrera '))
                m.ordenarymostrar(carerrax)
                print('\n')
            elif self.__opcion==5:
                areax=str(input('Ingrese area de investigacion '))
                m.contarymostrar(areax)
                print('\n')
            elif self.__opcion==6:
                print('entra a la opcion 6 ')
                m.ordenarycalcular()
                print('\n')
            elif self.__opcion==7:
                categoriax=str(input('Ingrese categoria(I,II,III,IV,V) '))
                m.mostrarporcategoria(categoriax)
                print('\n')
            elif self.__opcion==8:
                m.toJSON()
                print('Archivo cargado con exito ')
                print('\n')
            elif self.__opcion==9:
                print('SALIO DEL PROGRAMA')    
            elif self.__opcion==10:
                m.mostrartodos()
                print('\n')
            else:
                print('Opcion ingresada incorrecta ')




