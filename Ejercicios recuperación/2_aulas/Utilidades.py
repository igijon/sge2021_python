from datetime import datetime
from Aula import Aula
from Profesor import Profesor
from Alumno import Alumno
from Asignatura import Asignatura

"""UTILIDADES LECTURA"""
def leer_entero(msg, min, max):
    correcto = False
    entero = -1
    while not correcto:
        try:
            entero = int(input(msg))
            if entero < min or entero > max:
                raise ValueError("Debe ser un entero entre "+str(min)+" y "+str(max))
            correcto = True
        except ValueError:
            print("Debe introducir un número entero entre "+str(min)+" y "+str(max))
    return entero

def leer_fecha(msg):
    correcto = False
    fecha = None
    while not correcto:
        fecha_str = input(msg)
        try:
            fecha = datetime.strptime(fecha_str, '%d/%m/%Y').strftime('%d-%m-%Y')
            correcto = True
        except ValueError:
            print("Debe introducir una fecha correcta")
    return fecha

"""UTILIDADES DE LISTAS"""

def add_elemento(elemento, lista, error_msg):
    '''Añade un elemento a la lista si no está previamente en ella. Si está en la lista lanza una excepción con el
    mensaje de error que recibe por parámetro'''
    if not esta_elemento(elemento, lista):
        lista.append(elemento)
    else:
        raise ValueError(error_msg)

def esta_elemento(elemento, lista):
    '''Nos indica si el elemento se encuentra en la lista'''
    if elemento in lista:
        return True
    else:
        return False

def remove_elemento(elemento, lista, error_msg):
    '''Elimina el elemento de la lista. Si no se encuentra, lanzará una excepción con el mensaje de error recibido por
    parámetro.'''
    if elemento in lista:
        lista.remove(elemento)
    else:
        raise ValueError(error_msg)

"""UTILIDADES DE FICHEROS JSON"""

def add_profesores(dictionary_datos_aula, aula):
    """Obtiene los profesores del diccionario de datos del aula"""
    profesores_dict = dictionary_datos_aula["profesores"]
    for profesor_dict_dni in profesores_dict.keys():
        p = Profesor(profesor_dict_dni)
        datos_profesor_dict = profesores_dict.get(p.dni)
        p.nombre = datos_profesor_dict.get("nombre")
        p.fecha_nacimiento = datos_profesor_dict.get("fecha_nacimiento")
        p.fecha_incorporacion = datos_profesor_dict.get("fecha_incorporacion")
        aula.add_profesor(p)

def add_asignaturas(dictionary_datos_aula, aula):
    asignaturas_dict = dictionary_datos_aula["asignaturas"]
    for asignatura_dict_codigo in asignaturas_dict.keys():
        a = Asignatura(asignatura_dict_codigo)
        datos_asignatura_dict = asignaturas_dict.get(a.codigo)
        a.nombre = datos_asignatura_dict.get("nombre")
        # Obtenemos el objeto profesor a partir del dni del json
        profesor_asignatura = aula.get_profesor(Profesor(datos_asignatura_dict.get("profesor")))
        a.profesor = profesor_asignatura
        aula.add_asignatura(a)

def add_alumnos(dictionary_datos_aula, aula):
    alumnos_dict = dictionary_datos_aula["alumnos"]
    for alumno_dict_dni in alumnos_dict.keys():
        datos_alumno_dict = alumnos_dict.get(alumno_dict_dni)
        nombre = datos_alumno_dict.get("nombre")
        fecha_nacimiento = datos_alumno_dict.get("fecha_nacimiento")
        al = Alumno(alumno_dict_dni, nombre, fecha_nacimiento)
        # Obtenemos la lista de asignaturas y vamos obteniendo cada asignatura a partir de su código
        asignaturas_alumno = list(datos_alumno_dict.get("asignaturas"))
        for asignatura_alumno in asignaturas_alumno:
            asignatura = aula.get_asignatura(Asignatura(asignatura_alumno))
            al.matricular_asignatura(asignatura)
        aula.add_alumno(al)

def json_to_aula(dictionary):
    try:
        # Obtenemos el código del aula
        codigo_aula = list(dictionary.keys())[0]
        aula = Aula(codigo_aula)
        # Obtenemos los datos del aula
        datos_aula = dictionary.get(codigo_aula) #dictionary[codigo_aula]
        # Obtenemos los profesores y los vamos añadiendo al aula
        add_profesores(datos_aula, aula)

        # Obtenemos las asignaturas y las vamos añadiendo al aula
        add_asignaturas(datos_aula, aula)

        # Obtenemos los alumnos y los vamos añadiendo al aula
        add_alumnos(datos_aula, aula)

        return aula
    except Exception as err:
        print(err)

def buscar_profesor_auladict(aula_key, aula_dict, **kwargs):
    resultadosBusqueda = []
    profesores_dict = aula_dict[aula_key]["profesores"]
    if "dni" in kwargs.keys() and kwargs["dni"]!="":
        # Con dni sólo puede haber un profesor
        dni_profesor_buscar = kwargs["dni"]
        profesor = profesores_dict[dni_profesor_buscar];
        resultadosBusqueda.append(profesor);
    else:
        # si no viene el dni puede que busquen por nombre, fecha_nacimiento o fecha_incorporación
        # almacen_filtrado = profesores_dict.values()
        profesor_buscado = True
        for dni, profesor_dict in profesores_dict.items():
            for name, value in kwargs.items():
                if profesor_buscado and value != "" and profesor_dict[name] != value: profesor_buscado = False
            if profesor_buscado:
                resultadosBusqueda.append({dni: profesor_dict})
            else:
                profesor_buscado = True

    return resultadosBusqueda;





