from Persona import Persona

class Profesor(Persona):

    def __init__(self, dni, nombre = "", fecha_nacimiento = None, fecha_incorporacion = None):
        super().__init__(dni, nombre, fecha_nacimiento)
        self.fecha_incorporacion = fecha_incorporacion

    @property
    def fecha_incorporacion(self):
        return self.__fecha_incorporacion

    @fecha_incorporacion.setter
    def fecha_incorporacion(self, fecha_incorporacion):
        self.__fecha_incorporacion = fecha_incorporacion

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => DNI: {1}, Nombre: {2}, Fecha de nacimiento: {3}, Fecha de incorporacion: {4}"
        return msg.format(clase, self.dni, self.nombre, self.fecha_nacimiento, self.fecha_incorporacion)

    def to_dictionary(self):
        # Convierte la información de profesor en un diccionario
        profesor_dict = super().to_dictionary()
        datos_profesor = profesor_dict[self.dni]
        datos_profesor["fecha_incorporacion"] = self.fecha_incorporacion
        profesor_dict[self.dni] = datos_profesor
        return profesor_dict
