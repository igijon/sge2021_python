
from Vehicle import Vehicle
from Character import Character
from Film import Film
from datetime import datetime
from Studio import Studio

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

def add_element(element, list, error_msg):
    '''Añade un elemento a la lista si no está previamente en ella. Si está en la lista lanza una excepción con el
    mensaje de error que recibe por parámetro'''
    if not is_element(element, list):
        list.append(element)
    else:
        raise ValueError(error_msg)

def is_element(element, list):
    '''Nos indica si el elemento se encuentra en la lista'''
    if element in list:
        return True
    else:
        return False

def remove_element(element, list, error_msg):
    '''Elimina el elemento de la lista. Si no se encuentra, lanzará una excepción con el mensaje de error recibido por
    parámetro.'''
    if element in list:
        list.remove(element)
    else:
        raise ValueError(error_msg)

"""UTILIDADES DE FICHEROS JSON"""

def add_films(studio_data, studio):
    """Obtiene las películas del diccionario de datos del studio"""
    films_dict = studio_data["films"]
    for film_dict_title in films_dict.keys():
        f = Film(film_dict_title)
        film_dict_data = films_dict.get(f.title)
        f.director = film_dict_data.get("director")
        f.release_year = film_dict_data.get("release_year")
        studio.add_film(f)

def add_people(studio_data, studio):
    people_dict = studio_data["people"]
    for character_dict_name in people_dict.keys():
        c = Character(character_dict_name)
        character_dict_data = people_dict.get(c.name)
        c.age = character_dict_data.get("age")
        c.gender = character_dict_data.get("gender")
        c.specie = character_dict_data.get("specie")
        # Obtenemos el objeto character a partir del name del json
        film_character = studio.get_film(Film(character_dict_data.get("film")))
        c.film = film_character
        studio.add_character(c)

def add_vehicles(studio_data, studio):
    vehicles_dict = studio_data["vehicles"]

    for vehicle_dict_name in vehicles_dict.keys():
        vehicle_dict_data = vehicles_dict.get(vehicle_dict_name)
        pilot = studio.get_character(Character(vehicle_dict_data.get("pilot")))
        film = studio.get_film(Film(vehicle_dict_data.get("film")))
        v = Vehicle(vehicle_dict_name, pilot, film)
        studio.add_vehicle(v)

def json_to_studio(dictionary):
    try:
        # Obtenemos el id del estudio
        studio_id = list(dictionary.keys())[0]
        studio = Studio(studio_id)
        # Obtenemos los datos del studio
        studio_data = dictionary.get(studio_id) #dictionary[codigo_aula]
        # Obtenemos las películas y los vamos añadiendo al studio
        add_films(studio_data, studio)

        # Obtenemos los personajes y las vamos añadiendo al studio
        add_people(studio_data, studio)

        # Obtenemos los vehículos y los vamos añadiendo al studio
        add_vehicles(studio_data, studio)

        return studio
        
    except Exception as err:
        print(err)

def search_film_studio_dict(studio_id, studio_dict, **kwargs):
    resultadosBusqueda = []
    films_dict = studio_dict[studio_id]["films"]
    if "title" in kwargs.keys() and kwargs["title"]!="":
        # Con título sólo puede haber una película
        title_film_search = kwargs["title"]
        film = films_dict[title_film_search];
        resultadosBusqueda.append(film);
    else:
        # si no viene el título puede que busquen por release_year o director
        film_buscado = True
        for title, film_dict in films_dict.items():
            for name, value in kwargs.items():
                if film_buscado and value != "" and film_dict[name] != value: film_buscado = False
            if film_buscado:
                resultadosBusqueda.append({title: film_dict})
            else:
                film_buscado = True

    return resultadosBusqueda;





