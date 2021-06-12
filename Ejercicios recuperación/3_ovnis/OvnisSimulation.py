from Factorias.PuebloFactory import PuebloFactory
from Pueblo import Pueblo
from Humano import Humano
from Ovni import Ovni
import random


def realizar_acciones_simulacion(pueblo):
    for individuo in pueblo.humanos:
        try:
            distancia = random.randint(1, 3)
            direccion = random.randint(0, 2)
            if direccion == 0: #Izquierda
                print(individuo.id + " se desplaza "+str(distancia)+" a la izquierda.")
            elif direccion == 1: #Derecha
                print(individuo.id + " se desplaza "+str(distancia)+" a la derecha.")
            individuo.desplazar(distancia, direccion)
        except ValueError as e:
            print(e)

    for ovni in pueblo.ovnis:
        try:
            distancia = random.randint(1, 3)
            direccion = random.randint(0,2)
            if direccion == 0: #Izquierda
                print(ovni.id + " se desplaza "+str(distancia)+" a la izquierda")
            elif direccion == 1: #Derecha
                print(ovni.id + " se desplaza "+str(distancia)+" a la derecha")
            ovni.desplazar(distancia, direccion)
        except ValueError as e:
            print(e)

# Comienza flujo del programa
pueblo = PuebloFactory.generate_pueblo("Puertollano", 10,20,5)

while pueblo.hay_supervivientes():
    realizar_acciones_simulacion(pueblo)
    pueblo.desencadenar_abducciones()
    print(pueblo)
    key = input("Presione una tecla ...")







