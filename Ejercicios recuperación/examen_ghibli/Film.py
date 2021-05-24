
class Film():

    def __init__(self, title, release_year = None, director = None):
        self.title = title
        self.release_year = release_year
        self.director = director

    @property
    def title(self):
        return self.__title
    
    @property
    def release_year(self):
        return self.__release_year

    @property
    def director(self):
        return self.__director

    @title.setter
    def title(self, title):
        self.__title = title

    @release_year.setter
    def release_year(self, release_year):
        self.__release_year = release_year

    @director.setter
    def director(self, director):
        self.__director = director

    def __eq__(self, film):
        return self.title.__eq__(film.title)

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => Title: {1}, Release year: {2}, Director: {3}"
        return msg.format(clase, self.title, self.release_year, self.director)

    def to_dictionary(self):
        # Convierte la información de film en un diccionario
        film_dict = {}
        film_data = {}
        film_data["release_year"] = self.__release_year
        film_data["director"] = self.__director
        film_dict.setdefault(self.title, film_data)
        return film_dict