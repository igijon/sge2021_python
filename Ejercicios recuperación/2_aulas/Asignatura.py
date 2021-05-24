
class Asignatura():

    def __init__(self, codigo, nombre="", profesor=None):
        self.codigo = codigo
        self.nombre = nombre
        self.profesor = profesor

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def profesor(self):
        return self.__profesor

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @profesor.setter
    def profesor(self, profesor):
        self.__profesor = profesor

    def __eq__(self, asignatura):
        return self.codigo == asignatura.codigo

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => Código: {1}, Nombre: {2}, Profesor: {3}"
        return msg.format(clase, self.codigo, self.nombre, self.profesor.dni)

    def to_dictionary(self):
        # Convierte la información de asignatura en un diccionario
        asignatura_dict = {}
        asignatura_dict.setdefault(self.codigo, {'nombre': self.nombre,
                                                 'profesor': self.profesor.dni})
        return asignatura_dict
