#!/usr/bin/env python

def crear_lista(nombre_lista):
    """Crea una lista mientras el usuario introduce datos"""
    parar = False

    print("***"+nombre_lista+"***")
    lista = []
    while not parar:
        # Este es un comentario dentro del while
        lista.append(input("Elemento: "))
        opcion = input("¿Seguir?(s/n) ")
        if opcion != "s" and opcion != "S":
            parar = True
    return lista

def sustituir_elemento(lista, elemento, elemento_nuevo):
    '''Sustituye las ocurrencias del elemento en la lista por elemento_nuevo'''
    for i in range(len(lista)):
        if lista[i] == elemento:
            lista[i] = elemento_nuevo

def lista_interseccion(lista1, lista2):
    '''Devuelve la lista con los elementos que están en ambas'''
    lista_interseccion = []
    for i in lista1:
        if i in lista2:
            lista_interseccion.append(i)
    return lista_interseccion

def lista_diff(lista1,lista2):
    '''Devuelve una lista con los elementos que están en la primera lista pero no en la segunda'''
    elementos = []
    for i in lista1:
        if i not in lista2:
            elementos.append(i)
    return elementos

def ordenar(lista):
    '''Ordena los elementos de la lista'''
    return lista.sort()

def pedir_entero(mensaje):
    correcto = False
    while not correcto:
        try:
            num = int(input(mensaje))
            correcto = True
            return num
        except ValueError:
            print("Debe introducir un valor numérico")

def menu():
    print("***MENU***")
    print("1. Número de elementos de las listas")
    print("2. Número de ocurrencias de un elemento en cada lista")
    print("3. Sustituir un elemento en una lista")
    print("4. Ordenar lista")
    print("5. Lista intersección")
    print("6. Lista diferencia")
    print("7. Mostrar listas")
    print("8. Salir")

def num_elementos_listas(lista1, lista2):
    '''Muestra el número de elementos de las listas'''
    print("Número de elementos de lista1: " + str(len(lista1)))
    print("Número de elementos de lista2: " + str(len(lista2)))

def num_ocurrencias_listas(lista1, lista2):
    '''Muestra el número de ocurrencias de un elemento en las listas'''
    elemento = input("Elemento: ")
    print("Número de ocurrencias en lista1: " + str(lista1.count(elemento)))
    print("Número de ocurrencias en lista2: " + str(lista2.count(elemento)))

def sustituir_elemento_elegir_lista(lista1, lista2):
    '''Sustituye un elemento en la lista elegida por otro elemento'''
    num_lista = pedir_entero("Número de lista (1/2): ")
    if not num_lista == 1 and not num_lista == 2:
        print("Número de lista erróneo.")
    else:
        elemento = input("Elemento a sustituir: ")
        elemento_nuevo = input("Elemento nuevo: ")
        if num_lista == 1:
            sustituir_elemento(lista1, elemento, elemento_nuevo)
        else:
            sustituir_elemento(lista2, elemento, elemento_nuevo)
    print("LISTA1: "+str(lista1))
    print("LISTA2: "+str(lista2))

def ordenar_elegir_lista(lista1, lista2):
    '''Ordena una lista elegida'''
    num_lista = pedir_entero("Número de lista (1/2): ")
    if not num_lista == 1 and not num_lista == 2:
        print("Número de lista erróneo.")
    else:
        if num_lista == 1:
            lista1.sort()
            print("LISTA1: "+str(lista1))
        else:
            lista2.sort()
            print("LISTA2: "+str(lista2))

def lista_diferencia_elegir_lista(lista1, lista2):
    '''Elige la lista minuendo'''
    num_lista = pedir_entero("Lista minuendo (1/2): ")
    if not num_lista == 1 and not num_lista == 2:
        print("Número de lista erróneo")
    else:
        if num_lista == 1:
            lista = lista_diff(lista1, lista2)
        else:
            lista = lista_diff(lista2, lista2)
        return lista

def operar_listas(lista1, lista2):
    '''Muestra el menú por pantalla hasta que el usuario pulsa salir'''
    salir = False
    while not salir:
        menu()
        opcion = pedir_entero("Opción: ")
        if opcion == 1:
            # número de elementos de las listas
            num_elementos_listas(lista1, lista2)
        elif opcion == 2:
            # número de ocurrencias de un elemento en cada lista
            num_ocurrencias_listas(lista1, lista2)
        elif opcion == 3:
            # Sustituir elemento en una lista
            sustituir_elemento_elegir_lista(lista1, lista2)
        elif opcion == 4:
            # Ordena una lista elegida por el usuario
            ordenar_elegir_lista(lista1, lista2)
        elif opcion == 5:
            # Genera la lista intersección
            lista = lista_interseccion(lista1, lista2)
            print("LISTA INTERSECCIÓN: "+str(lista))
        elif opcion == 6:
            # Genera una lista diferencia
            lista = lista_diferencia_elegir_lista(lista1, lista2)
            print("LISTA DIFERENCIA: " + str(lista))
        elif opcion == 7:
            # Mostrar listas
            print("LISTA1: "+str(lista1))
            print("LISTA2: "+str(lista2))
        elif opcion == 8:
            # Salir
            salir = True
        else:
            print("Opción incorrecta")


##### Ejecución
lista1 = crear_lista("lista1")
lista2 = crear_lista("lista2")

operar_listas(lista1, lista2)