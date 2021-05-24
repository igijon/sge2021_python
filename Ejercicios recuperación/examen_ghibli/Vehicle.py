
class Vehicle():

    def __init__(self, name, pilot = None, film = None):
        self.name = name
        self.pilot = pilot
        self.film = film

    @property
    def name(self):
        return self.__name
    
    @property
    def pilot(self):
        return self.__pilot

    @property
    def film(self):
        return self.__film

    @name.setter
    def name(self, name):
        self.__name = name

    @pilot.setter
    def pilot(self, pilot):
        self.__pilot = pilot
    
    @film.setter
    def film(self, film):
        self.__film = film

    def __eq__(self, character):
        return self.name.__eq__(character.name)

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => Name: {1}, Pilot: {2}, Film: {3}"
        return msg.format(clase, self.name, self.pilot.name, self.film.title)

    def to_dictionary(self):
        # Convierte la información de film en un diccionario
        vehicle_dict = {}
        vehicle_data = {}
        vehicle_data["pilot"] = self.pilot.name
        vehicle_data["film"] = self.film.title
        vehicle_dict.setdefault(self.name, vehicle_data)
        return vehicle_dict