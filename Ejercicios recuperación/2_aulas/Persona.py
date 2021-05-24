
class Persona():
    '''Clase de la que heredarán Profesor y Alumno'''
    def __init__(self, dni, nombre, fecha_nacimiento):
        self.dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    @property
    def dni(self):
        return self.__dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def __eq__(self, persona):
        return self.dni == persona.dni

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => DNI: {1}, Nombre: {2}, Fecha de nacimiento: {3}"

        return msg.format(clase, self.dni, self.nombre, self.fecha_nacimiento)

    def to_dictionary(self):
        # Convierte la información de persona en un diccionario
        persona_dict = {}
        persona_dict.setdefault(self.dni, {'nombre': self.nombre, 'fecha_nacimiento': self.fecha_nacimiento})
        return persona_dict