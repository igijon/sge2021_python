import Utilities

class Studio():
    '''Un studio tendrá un conjunto de películas'''
    def __init__(self, id):
        self.id = id
        self.__films = []
        self.__people = []
        self.__vehicles = []

    """Getters y setters"""

    @property
    def id(self):
        return self.__id

    @property
    def films(self):
        return self.__films

    @property
    def people(self):
        return self.__people

    @property
    def vehicles(self):
        return self.__vehicles

    @id.setter
    def id(self, codigo):
        self.__id = codigo


    def add_film(self, film):
        '''Añade una película a la colección de películas'''
        error_msg = "Película previamente registrada. Pelicula: "+str(film)
        Utilities.add_element(film, self.__films, error_msg)

    def add_character(self, character):
        '''Añade un personaje a la colección de personajes'''
        if character.film not in self.films:
            raise ValueError("No podemos añadir el personaje porque la película no está registrada "+str(character))
        error_msg = "Personaje previamente registrado. Personaje: "+str(character)
        Utilities.add_element(character, self.__people, error_msg)

    def add_vehicle(self, vehicle):
        '''Añade un vehículo a la colección de vehículos, siempre que la película esté registrada y el piloto (personaje) también lo esté'''
        if vehicle.film not in self.films:
            raise ValueError("No podemos añadir el vehículo porque la película no está registrada "+str(vehicle))
        if vehicle.pilot not in self.people:
            raise ValueError("No podemos añadir el vehículo porque el piloto no está registrado "+str(vehicle))
        error_msg = "Vehículo previamente registrado. Vehículo: "+str(vehicle)
        Utilities.add_element(vehicle, self.__vehicles, error_msg)
    
    def remove_film(self, film):
        '''Elimina la película si no hay personajes ni vehículos asociados a ella'''
        if self.are_elements_movie(film, self.people):
            raise ValueError("Película no eliminada. Personajes asociados")
        if self.are_elements_movie(film, self.vehicles):
            raise ValueError("Película no eleiminada. Vehículos asociados")
        error_msg = "No existe la película. Película "+film.title
        Utilities.remove_element(film, self.__films, error_msg)

    def are_elements_movie(self, film, elements_list):
        '''Devuelve true si existen elementos asociados a dicha película'''
        elements = False
        n = 0
        while not elements and n < len(elements_list):
            if elements_list[n].film == film: 
                elements = True
            else:
                n+=1
        return elements

    def remove_character(self, character):
        '''Podemos borrar un personaje únicamente si no hay vehículos asociados a él, es decir que le tengan como piloto'''
        if self.are_vehicles_character(character):
            raise ValueError("Personaje no eliminado. Vehículos asociados")
        error_msg = "No existe el personaje. Personaje "+character.name
        Utilities.remove_element(character, self.__people, error_msg)

    def are_vehicles_character(self, character):
        '''Devuelve true si existen vehículos asociados a dicho personaje'''
        vehicles = False
        n = 0
        while not vehicles and n < len(self.vehicles):
            if self.vehicles[n].pilot == character:
                vehicles = True
            else:
                n+=1
        return vehicles

    def remove_vehicle(self, vehicle):
        '''Elimina el vehículo del conjunto de vehículos. Si no se lanzará una
        excepción'''
        error_msg = "Vehículo no existente: "+str(vehicle)
        Utilities.remove_element(vehicle, self.__vehicles, error_msg)


    def get_film(self, film):
        if Utilities.is_element(film, self.films):
            index = self.films.index(film)
            return self.films[index]
        else:
            raise ValueError("Película no registrada. Película: "+str(film))

    def get_character(self, character):
        '''Devuelve el personaje de la colección de personajes. Se basa internamente en buscarlo en su id. Los
        datos reales de los personajes están en la lista de personajes del studio'''
        if Utilities.is_element(character, self.people):
            index = self.people.index(character)
            return self.people[index]
        else:
            raise ValueError("Personaje no registrado. Personaje: "+str(character))

    def is_film_studio(self, film):
        if film in self.films:
            return True
        return False

    def is_character_studio(self, character):
        if character in self.people:
            return True
        return False
        
    def __eq__(self, studio):
        return self.id == studio.id

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => Id: {1}\nFilms: \n"

        for film in self.films:
            msg += str(film) + "\n"

        msg += "Personajes:\n"

        for character in self.people:
            msg += str(character) + "\n"

        msg += "Vehículos:\n"

        for vehicle in self.vehicles:
            msg += str(vehicle)+"\n"

        return msg.format(clase, self.id)

    def to_dictionary(self):
        # Convierte la información del studio en un diccionario
        studio_dict = {}
        studio_dict.setdefault(self.id, {})
        datos_studio = studio_dict[self.id]
        films = {}
        people = {}
        vehicles = {}

        for film in self.films:
            films.update(film.to_dictionary())
        datos_studio["films"] = films

        for character in self.people:
            people.update(character.to_dictionary())
        datos_studio["people"] = people

        for vehicle in self.vehicles:
            vehicles.update(vehicle.to_dictionary())
        datos_studio["vehicles"]=vehicles

        studio_dict[self.id] = datos_studio
        return studio_dict