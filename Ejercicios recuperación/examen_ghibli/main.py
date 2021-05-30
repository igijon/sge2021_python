from Utilities import *
from Character import *
from Film import *
from Studio import *
from Vehicle import *
import json


def print_menu_principal():
    print("********Studio Ghibli********")
    print("1. Crear studio vacío")
    print("2. Cargar studio de un fichero")
    print("3. Salir")
    opcion = leer_entero("Opcion: ", 1, 3)

    if opcion == 1:
        # Creamos el aula vacía
        codigo = input("Código: ")
        studio = Studio(codigo)
    elif opcion == 2:
        studio = cargar_json()
    elif opcion == 3:
        return 0
    if not studio is None:
        print_menu_studio(studio)



def print_menu_studio(studio):
    salir = False
    while not salir:
        print("********" + str(studio.id) + "********")
        '''Tendremos que añadir películas en primer lugar, no se podrán añadir personajes si no están agregadas las películas
        relacionadas y tampoco se podrán añadir vehículos hasta que no esté la película y el piloto (personaje) relacionado en 
        el sistema'''
       
        print("1. Añadir pelicula")
        print("2. Eliminar pelicula")
        print("3. Añadir personaje")
        print("4. Eliminar personaje")
        print("5. Añadir vehículo")
        print("6. Eliminar vehículo")
        print("7. Mostrar studio")
        print("8. Guardar JSON")
        print("9. Buscar película")
        print("10. Salir")
        opcion = leer_entero("Opción: ", 1, 10)

        if opcion == 1:
            # Añadimos una película
            add_film(studio)
        elif opcion == 2:
            # Eliminamos una película
            del_film(studio)
        elif opcion == 3:
            # Añadir un personaje
            add_character(studio)
        elif opcion == 4:
            # Eliminamos un personaje
            del_character(studio)
        elif opcion == 5:
            # Añadimos un vehículo
            add_vehicle(studio)
        elif opcion == 6:
            # Eliminar un vehículo
            del_vehicle(studio)
        elif opcion == 7:
            print(studio)
            print(studio.to_dictionary())
        elif opcion == 8:
            # Escribimos los datos del studio en un fichero json
            guardar_json(studio)
        elif opcion == 9:
            # Solicitamos los datos para buscar
            search_film(studio)
        elif opcion == 10:
            salir = True


def add_film(studio):
    film = get_film_data()
    try:
        studio.add_film(film)
    except ValueError as err:
        print(err)


def del_film(studio):
    title = input("Title: ")
    try:
        studio.remove_film(Film(title))
    except ValueError as err:
        print(err)

def search_film(studio):
    studio_dict = studio.to_dictionary()
    title = input("Título (enter si no desea este dato): ")
    release_year = input("Año de estreno (enter si no desea este dato): ")
    director = input("Director (enter si no desea este dato): ")
    resultado_busqueda = search_film_studio_dict(studio.id, studio_dict, title=title, release_year=release_year, director=director)
    print("El resultado de la búsqueda es: ")
    for film in resultado_busqueda:
        print(film)

def add_character(studio):
    character = get_character_data()
    '''Antes de añadir un personaje nos tenemos que asegurar de que la película relacionada está en el sistema y si es 
    así, recuperarla y asignarle los datos reales'''
    if studio.is_film_studio(character.film):
        film = studio.get_film(character.film)
        character.film = film
        try:
            studio.add_character(character)
        except ValueError as err:
            print(err)
    else:
        print("No se puede añadir el personaje. Película no registrada. " + str(character.film.title))

def del_character(studio):
    name = input("Name: ")
    try:
        studio.remove_character(Character(name))
    except ValueError as err:
        print(err)

def add_vehicle(studio):
    vehicle = get_vehicle_data()
    # Antes de añadirlo tenemos que comprobar que existe la película y el piloto en personajes
    
    if not studio.is_character_studio(vehicle.pilot):
        print("No se puede añadir el vehículo. El piloto no está registrado. Piloto: "+vehicle.pilot.name)
    elif not studio.is_film_studio(vehicle.film): #Esta condición no debería ser necesaria porque si el piloto está
        #registrado, la película también lo está.
        print("No se puede añadir el vehículo. Película no registrada. Película: "+str(vehicle.film.title))
    else:
        pilot = studio.get_character(vehicle.pilot)
        film = studio.get_film(vehicle.film)
        vehicle.pilot = pilot
        vehicle.film = film
        try:
            studio.add_vehicle(vehicle)
        except ValueError as err:
            print(err)

def del_vehicle(studio):
    vehicle = input("Name: ")
    try:
        studio.remove_vehicle(Vehicle(vehicle))
    except ValueError as err:
        print(err)

def guardar_json(studio):
    fichero = input("Fichero: ")
    try:
        fichero_json = open(fichero, "w")
        json.dump(studio.to_dictionary(), fichero_json)
        fichero_json.close()
    except Exception as err:
        print(err)


def cargar_json():
    try:
        fichero = input("Fichero a cargar: ")
        with open(fichero) as fichero_json:
            datos_studio = json.load(fichero_json)
        return json_to_studio(datos_studio)
    except Exception as err:
        print(err)

def get_film_data():
    '''Crea una película pidiendo los datos al usuario'''
    title = input("Title: ")
    release_year = leer_entero("Año estreno: ", 0, 9999)
    director = input("Director: ")
    return Film(title, release_year, director)

def get_character_data():
    '''Crea un personaje pidiendo los datos al usuario'''
    name = input("Nombre: ")
    gender = input("Género: ")
    specie = input("Especie: ")
    age = leer_entero("Edad: ", 0, 9999)
    film = input("Película (título): ")
    return Character(name, gender, age, Film(film), specie)

def get_vehicle_data():
    '''Crea un vehículo pidiendo los datos al usuario'''
    name = input("Nombre: ")
    pilot = input("Piloto (Nombre): ")
    film = input("Película (título): ")
    return Vehicle(name, Character(pilot), Film(film))

if __name__ == '__main__':
    print_menu_principal()
