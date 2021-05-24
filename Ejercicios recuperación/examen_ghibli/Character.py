
class Character():

    def __init__(self, name, gender = None, age = None, film = None, specie = None):
        self.name = name
        self.gender = gender
        self.age = age
        self.film = film
        self.specie = specie

    @property
    def name(self):
        return self.__name
    
    @property
    def gender(self):
        return self.__gender

    @property
    def age(self):
        return self.__age

    @property
    def film(self):
        return self.__film

    @property
    def specie(self):
        return self.__specie

    @name.setter
    def name(self, name):
        self.__name = name

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @age.setter
    def age(self, age):
        self.__age = age
    
    @film.setter
    def film(self, film):
        self.__film = film

    @specie.setter
    def specie(self, specie):
        self.__specie = specie

    def __eq__(self, character):
        return self.name.__eq__(character.name)

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => Name: {1}, Gender: {2}, Age: {3}, Film: {4}, specie: {5}"
        return msg.format(clase, self.name, self.gender, self.age, self.film.title, self.specie)

    def to_dictionary(self):
        # Convierte la información de film en un diccionario
        character_dict = {}
        character_data = {}
        character_data["gender"] = self.gender
        character_data["age"] = self.age
        character_data["film"] = self.film.title
        character_data["specie"] = self.specie
        character_dict.setdefault(self.name, character_data)
        return character_dict