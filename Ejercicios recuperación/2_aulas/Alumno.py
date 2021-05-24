import Utilidades

from Persona import Persona


class Alumno(Persona):

    def __init__(self, dni, nombre, fecha_nacimiento):
        super().__init__(dni, nombre, fecha_nacimiento)
        self.__asignaturas_matricula = []

    @property
    def asignaturas_matricula(self):
        return self.__asignaturas_matricula

    @asignaturas_matricula.setter
    def asignaturas_matricula(self, asignaturas):
        self.__asignaturas_matricula = asignaturas

    def matricular_asignatura(self, asignatura):
        '''Añade la asignatura a la lista si no existe previamente'''
        try:
            error_msg = "Alumno ya matriculado. Asignatura: "+asignatura.codigo
            Utilidades.add_elemento(asignatura, self.__asignaturas_matricula, error_msg)
        except ValueError as err:
            print(err)

    def esta_asignatura_matricula(self, asignatura):
        '''Nos indica si el alumno se ha matriculado de una asignatura'''
        return Utilidades.esta_elemento(asignatura, self.__asignaturas_matricula)

    def remove_asignatura(self, asignatura):
        '''Borra la asignatura de la lista de asignaturas en las que está matriculado. Si no está matriculado, lanza
        una excepción'''

        error_msg = "Alumno no matriculado. Asignatura: "+str(asignatura)
        Utilidades.remove_elemento(asignatura, self.__asignaturas_matricula, error_msg)

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => DNI: {1}, Nombre: {2}, Fecha de nacimiento: {3}\nAsignaturas matriculado:\n"
        for asignatura in self.__asignaturas_matricula:
            msg += asignatura.codigo+"\n"
        return msg.format(clase, self.dni, self.nombre, self.fecha_nacimiento)

    def to_dictionary(self):
        # Convierte la información de alumno en un diccionario
        alumno_dict = super().to_dictionary()
        datos_alumno = alumno_dict[self.dni]
        asignaturas_matricula = []
        for asignatura in self.__asignaturas_matricula:
            asignaturas_matricula.append(asignatura.codigo)
        datos_alumno["asignaturas"] = asignaturas_matricula
        alumno_dict[self.dni] = datos_alumno
        return alumno_dict
