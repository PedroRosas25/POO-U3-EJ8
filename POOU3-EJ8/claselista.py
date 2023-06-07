from clasedocenteinvestigador import DocenteInvestigador
from claseinvestigador import Investigador
from clasenodo import Nodo

class Lista:
    __comienzo=Nodo

    def __init__(self):
        self.__comienzo=None
    def agregarPersonalFinal(self,vehiculo):
        nuevonodo = Nodo(vehiculo)
        if self.__comienzo == None:
            self.__comienzo = nuevonodo
        else:
            temporal = self.__comienzo
            while temporal.getSiguiente() is not None:
                temporal = temporal.getSiguiente()
            temporal.setSiguiente(nuevonodo)    

    def agregarPersonalIndice(self,vehiculo,indice):
        nuevonodo=Nodo(vehiculo)
        if indice == 1:
            nuevonodo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevonodo
        else:
            temporal = self.__comienzo
            contador = 1
            while temporal:
                if contador + 1 == indice:
                    nuevonodo.setSiguiente(temporal.getSiguiente())
                    temporal.setSiguiente(nuevonodo)
                    break
                temporal = temporal.getSiguiente()
                contador += 1

    def getTipo(self,posicion):
        c=0
        aux=self.__comienzo
        while aux!= None and c!= posicion:
            aux=aux.getSiguiente()
            c+=1
        if c==posicion:
            aux.getTipo() 

    def ordenarymostrar(self,carrerax):
        print('Listado ordenado por nombre de Docente Investigadores ')
        listaordenada=[]
        aux=self.__comienzo
        while aux!=None:
            if aux.getTipo2()=='DocenteInvestigador' and aux.getCarrera()==carrerax:
                listaordenada.append(aux.getDato())
            aux=aux.getSiguiente()    
        listaordenada.sort()    
        for i in range(len(listaordenada)):
            print('{}'.format(listaordenada[i]))  

    def contarymostrar(self,areax):
        c1=0
        c2=0
        aux=self.__comienzo
        while aux!=None:
            if aux.getTipo2()=='DocenteInvestigador' and aux.getArea()==areax:
                c1+=1
            elif aux.getTipo2()=='Investigador' and aux.getArea()==areax:
                c2+=1
            aux=aux.getSiguiente()    
        print('Cantidad de DocentesInvestigadores en el area ingresada:{}'.format(c1))
        print('Cantidad de Investigador en el area ingresada:{}'.format(c2))        

    def ordenarycalcular(self):
        listaordenada=[]
        aux=self.__comienzo
        while aux!=None:
            listaordenada.append(aux)
            aux=aux.getSiguiente()
        listaordenada.sort()
        for i in range(len(listaordenada)):
            print('{} {} {} {}'.format(listaordenada[i].getNombre(),listaordenada[i].getApellido(),listaordenada[i].getTipo2(),listaordenada[i].getSueldo()))    

    def mostrarporcategoria(self,categoriax):
        totalimporteextra=0
        aux=self.__comienzo
        while aux!=None:
            if aux.getTipo2()=='DocenteInvestigador':
                if aux.getCategoriaInve()==categoriax:
                    totalimporteextra+=float(aux.getImporteextra())
                    print('{} {} {}'.format(aux.getApellido(),aux.getNombre(),aux.getImporteextra())) 
            aux=aux.getSiguiente()
        print('Total a pagar en importes extras de la categoria ingresada:{}'.format(totalimporteextra))               

    def gastosSueldoPorEmpleado(self,cuil):
        aux=self.__comienzo
        while aux!=None:
            if aux.getCuil()==cuil:
                print('sueldo del personal con cuil ingresado:{}'.format(aux.getSueldo()))
            aux=aux.getSiguiente()    

    def modificarBasico(self,cuil,nuevoBasico):
        aux=self.__comienzo
        while aux!=None:
            if aux.getCuil()==cuil:
                aux.modificarBasico(nuevoBasico)
            aux=aux.getSiguiente()                           
    def modificarPorcentajeporcargo(self,cuil,nuevoPorcentaje):
        aux=self.__comienzo
        while aux!=None:
            if aux.getTipo2()=='Docente' and aux.getCuil()==cuil:
                aux.modificarPorcentajeporcargo(nuevoPorcentaje)
            aux=aux.getSiguiente()    
    def modificarPorcentajeporcategoria(self,cuil,nuevoPorcentaje):
        aux=self.__comienzo
        while aux!=None:
            if aux.getTipo2()=='Apoyo' and aux.getCuil()==cuil:
                aux.modificarPorcentajeporcategoria(nuevoPorcentaje)
            aux=aux.getSiguiente()    
    def modificarImporteExtra(self,cuil,nuevoImporteExtra):
        aux=self.__comienzo
        while aux!=None:
            if aux.getTipo2()=='DocenteInvestigador' and aux.getCuil()==cuil:
                aux.modificarImporteExtra(nuevoImporteExtra)
            aux=aux.getSiguiente()                   


    def toJSON(self):
        aux=self.__comienzo
        listajson=[]
        while aux!=None:
            personal=aux.toJSON()
            listajson.append(personal)
            aux=aux.getSiguiente()  
        return listajson       

    def mostrartodos(self):
        aux=self.__comienzo
        while aux!=None:
            print(aux.getDato())
            aux=aux.getSiguiente()    

