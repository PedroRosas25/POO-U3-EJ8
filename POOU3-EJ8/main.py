from menu import Menu
from manejador import Manejador as M

if __name__=='__main__':
    m=M()
    m.cargarlista()
    tipo=str(input('Ingrese si quiere entrar como usuario, tesorero o director '))
    if tipo=='usuario':
        menu=Menu()
        menu.opciones(m)
    elif tipo=='tesorero':
        usuario=str(input('Ingrese usurio de tesorero '))
        if usuario=='uTesoreso':
            contrasenia=str(input('Ingrese contraseña de tesorero '))
            if contrasenia=='ag@74ck':
                cuil=str(input('Ingrese cuil '))
                m.gastosSueldoPorEmpleado(cuil)
    elif tipo=='director':
        usuario=str(input('Ingrese usuario de director '))
        if usuario=='uDirector':
            contrasenia=str(input('Ingrese contraseña de director ')) 
            if contrasenia=='ufC77#!1':       
                opcion=0
                while opcion!=5:
                    print('1--Modificar basico\n2--Modificar porcentaje por cargo\n3--Modificar porcentaje por categoria\n4--Modificar importe')
                    opcion=int(input('Ingrese una opcion '))
                    if opcion==1:
                        cuil=str(input('Imgrese cuil '))
                        nuevoBasico=float(input('Ingrese nuevo sueldo basico '))
                        m.modificarBasico(cuil,nuevoBasico) 
                    elif opcion==2:
                        cuil=str(input('Imgrese cuil de docente '))
                        nuevoPorcentaje=int(input('Ingrese nuevo porcentaje '))
                        m.modificarPorcentajeporcargo(cuil,nuevoPorcentaje)
                    elif opcion==3:
                        cuil=str(input('Imgrese cuil de personal de apoyo '))
                        nuevoPorcentaje=int(input('Ingrese nuevo porcentaje '))
                        m.modificarPorcentajeporcategoria(cuil,nuevoPorcentaje)
                    elif opcion==4:
                        cuil=str(input('Ingrese cuil de docente investigador'))
                        nuevoImporteExtra=float(input('Ingrese nuevo importe extra '))
                        m.modificarImporteExtra(cuil,nuevoImporteExtra)
                    elif opcion==5:
                        print('SALIENDO DEL SISTEMA')
                    else:
                        print('Opcion ingresada incorecta')    