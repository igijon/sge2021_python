from Utilidades import *
from Aula import *
from Profesor import *
from Asignatura import *
from Alumno import *
import json


def print_menu_principal():
    print("********CIFP Virgen de Gracia********")
    print("1. Crear aula vacía")
    print("2. Cargar aula de un fichero")
    print("3. Salir")
    opcion = leer_entero("Opcion: ", 1, 3)

    if opcion == 1:
        # Creamos el aula vacía
        codigo = input("Código: ")
        aula = Aula(codigo)
    elif opcion == 2:
        aula = cargar_json()
    elif opcion == 3:
        return 0
    if not aula is None:
        print_menu_aula(aula)



def print_menu_aula(aula):
    salir = False
    while not salir:
        print("********" + aula.codigo + "********")
        # Tendremos que añadir profesores en primer lugar, no se podrán añadir asignaturas si no están agregados los profesores
        # correspondientes en el curso. Por último se deben agregar alumnos. Es decir, no podremos agregar una asignatura
        # que es impartida por un profesor no agregado ni un alumno con asignaturas que no estén añadidas al sistema
        print("1. Añadir profesor")
        print("2. Eliminar profesor")
        print("3. Añadir asignatura")
        print("4. Eliminar asignatura")
        print("5. Añadir alumno")
        print("6. Eliminar alumno")
        print("7. Mostrar aula")
        print("8. Guardar JSON")
        print("9. Buscar profesor")
        print("10. Salir")
        opcion = leer_entero("Opción: ", 1, 10)

        if opcion == 1:
            # Añadimos un profesor
            add_profesor(aula)
        elif opcion == 2:
            # Eliminamos un profesor
            del_profesor(aula)
        elif opcion == 3:
            # Añadir una asignatura
            add_asignatura(aula)
        elif opcion == 4:
            # Eliminamos una asignatura
            del_asignatura(aula)
        elif opcion == 5:
            # Añadimos un alumno
            add_alumno(aula)
        elif opcion == 6:
            # Eliminar un alumno
            del_alumno(aula)
            pass
        elif opcion == 7:
            print(aula)
            print(aula.to_dictionary())
        elif opcion == 8:
            # Escribimos los datos del aula en un fichero json
            guardar_json(aula)
        elif opcion == 9:
            # Solicitamos los datos para buscar
            buscar_profesor(aula)
        elif opcion == 10:
            salir = True


def add_profesor(aula):
    profesor = pedir_datos_profesor()
    try:
        aula.add_profesor(profesor)
    except ValueError as err:
        print(err)


def del_profesor(aula):
    dni = input("Dni: ")
    try:
        aula.remove_profesor(Profesor(dni))
    except ValueError as err:
        print(err)

def buscar_profesor(aula):
    aula_dict = aula.to_dictionary()
    dni = input("Dni (enter si no desea este dato): ")
    nombre = input("Nombre (enter si no desea este dato): ")
    fecha_nacimiento = input("Fecha de nacimiento (enter si no desea este dato): ")
    fecha_incorporacion = input("Fecha de incorporación (enter si no desea este dato): ")
    resultado_busqueda = buscar_profesor_auladict(aula.codigo, aula_dict, dni=dni, nombre=nombre, fecha_nacimiento=fecha_nacimiento, fecha_incorporacion=fecha_incorporacion)
    print("El resultado de la búsqueda es: ")
    for profesor in resultado_busqueda:
        print(profesor)

def add_asignatura(aula):
    asignatura = pedir_datos_asignatura()
    # Antes de añadirla tenemos que comprobar que el profesor está en el sistema y si es así, recuperarlo y asignar
    # los datos reales a la asignatura
    if aula.esta_profesor_en_curso(asignatura.profesor):
        profesor = aula.get_profesor(asignatura.profesor)
        asignatura.profesor = profesor
        try:
            aula.add_asignatura(asignatura)
        except ValueError as err:
            print(err)
    else:
        print("No se puede añadir la asignatura. Profesor no registrado. " + str(asignatura.profesor.dni))


def del_asignatura(aula):
    codigo = input("Código: ")
    try:
        aula.remove_asignatura(Asignatura(codigo))
    except ValueError as err:
        print(err)


def add_alumno(aula):
    alumno = pedir_datos_alumno()
    # Antes de añadirlo tenemos que comprobar que existen las asignaturas, recuperarlas y asignar sus datos reales.
    asignaturas_registradas = True
    contador = 0
    asignaturas_pendientes = []
    while asignaturas_registradas and contador < len(alumno.asignaturas_matricula):
        if aula.asignatura_en_curso(alumno.asignaturas_matricula[contador]):
            asignatura = aula.get_asignatura(alumno.asignaturas_matricula[contador])
            asignaturas_pendientes.append(asignatura)
            contador += 1
        else:
            asignaturas_registradas = False
    if asignaturas_registradas:
        alumno.asignaturas_matricula = asignaturas_pendientes
        try:
            aula.add_alumno(alumno)
        except ValueError as err:
            print(err)
    else:
        print("No se puede añadir el alumno. Hay asignaturas no registradas. Asignatura: " +
              alumno.asignaturas_matricula[contador].codigo)


def del_alumno(aula):
    dni = input("Dni: ")
    try:
        aula.remove_alumno(Alumno(dni))
    except ValueError as err:
        print(err)

def guardar_json(aula):
    fichero = input("Fichero: ")
    try:
        fichero_json = open(fichero, "w")
        json.dump(aula.to_dictionary(), fichero_json)
        fichero_json.close()
    except Exception as err:
        print(err)


def cargar_json():
    try:
        fichero = input("Fichero a cargar: ")
        with open(fichero) as fichero_json:
            datos_aula = json.load(fichero_json)
        return json_to_aula(datos_aula)
    except Exception as err:
        print(err)

def pedir_datos_profesor():
    '''Crea un profesor pidiendo los datos al usuario'''
    dni = input("DNI: ")
    nombre = input("Nombre: ")
    fecha_nacimiento = leer_fecha("Fecha de nacimiento (dd/mm/yyyy): ")
    fecha_incorporacion = leer_fecha("Fecha de incorporación (dd/mm/yyyy): ")
    return Profesor(dni, nombre, fecha_nacimiento, fecha_incorporacion)


def pedir_datos_asignatura():
    '''Crea una asignatura pidiendo los datos al usuario'''
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    profesor_dni = input("Dni profesor: ")
    return Asignatura(codigo, nombre, Profesor(profesor_dni))


def pedir_datos_alumno():
    '''Crea un alumno pidiendo los datos al usuario'''
    codigo = input("DNI: ")
    nombre = input("Nombre: ")
    fecha_nacimiento = leer_fecha("Fecha de nacimiento (dd/mm/yyyy): ")
    alumno = Alumno(codigo, nombre, fecha_nacimiento)
    salir = False
    while not salir:
        print("Introduzca los códigos de las asignaturas pendientes (S o s)")
        codigo = input("Código asignatura: ")
        if codigo != "S" and codigo != "s":
            alumno.matricular_asignatura(Asignatura(codigo))
        else:
            salir = True
    return alumno


if __name__ == '__main__':
    print_menu_principal()
