import Utilidades

class Aula():
    '''Un aula tendrá un código, un conjunto de alumnos y un conjunto de asignaturas(módulos) que se imparten'''
    def __init__(self, codigo):
        self.codigo = codigo
        self.__alumnos = []
        self.__asignaturas = []
        self.__profesores = []

    """Getters y setters"""

    @property
    def codigo(self):
        return self.__codigo

    @property
    def asignaturas(self):
        return self.__asignaturas

    @property
    def alumnos(self):
        return self.__alumnos

    @property
    def profesores(self):
        return self.__profesores

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    """Gestión de asignaturas"""

    def add_asignatura(self, asignatura):
        '''Añade una asignatura a la colección de asignaturas'''
        # Sólo se añade la asignatura si el profesor está registrado en el curso
        if asignatura.profesor not in self.__profesores:
            raise ValueError("No podemos añadir la asignatura porque el profesor no está registrado en el equipo educativo "+str(asignatura))
        error_msg = "Asignatura previamente registrada. Asignatura: "+str(asignatura)
        Utilidades.add_elemento(asignatura, self.__asignaturas,error_msg)

    def asignatura_en_curso(self, asignatura):
        '''Nos indica si la asignatura se encuentra en las que se dan en el aula'''
        return Utilidades.esta_elemento(asignatura, self.__asignaturas)

    def remove_asignatura(self, asignatura):
        '''Elimina la asignatura del conjunto de asignaturas que se imparten en el aula. Si no se lanzará una
        excepción'''
        # No podemos eliminar una asignatura si hay alumnos matriculados en ella
        if self.hay_alumnos_matriculados(asignatura):
            raise ValueError("Asignatura no eliminada. Alumnos matriculados.")
        error_msg = "No se imparte la asignatura. Asignatura " + asignatura.codigo
        Utilidades.remove_elemento(asignatura, self.__asignaturas, error_msg)

    def get_asignatura(self, asignatura):
        '''Devuelve la asignatura de la lista de asignaturas registradas. Se basa internamente en buscarlo en su código.
        Los datos reales de las asignaturas están en la lista de asignaturas del aula'''
        if self.asignatura_en_curso(asignatura):
            index = self.asignaturas.index(asignatura)
            return self.asignaturas[index]
        else:
            raise ValueError("Asignatura no registrada. Asignatura "+str(asignatura))

    def hay_asignaturas_impartidas_por(self, profesor):
        """Devuelve Trye si en el curso hay asignaturas impartidas por dicho profesor"""
        impartidas = False
        contador = 0
        while not impartidas and contador < len(self.__asignaturas):
            if self.__asignaturas[contador].profesor == profesor:
                impartidas = True
            else:
                contador += 1
        return impartidas

    """Gestión de alumnos"""

    def add_alumno(self, alumno):
        '''Añade un alumno a la colección de alumnos'''
        # El alumno sólo se debe añadir si las asignaturas están registradas en el sistema
        asignatura_registrada = True
        contador = 0
        while asignatura_registrada and contador < len(alumno.asignaturas_matricula):
            if alumno.asignaturas_matricula[contador] not in self.__asignaturas:
                asignatura_registrada = False
            contador+=1
        if not asignatura_registrada:
            raise ValueError("Alumno con asignaturas no registradas. "+str(alumno.asignaturas_matricula[contador-1]))
        error_msg = "Alumno previamente registrado. Alumno: "+str(alumno)
        Utilidades.add_elemento(alumno, self.__alumnos, error_msg)

    def esta_alumno_en_curso(self, alumno):
        '''Nos indica si el alumno está asignado al curso'''
        return Utilidades.esta_elemento(alumno, self.__alumnnos)

    def remove_alumno(self, alumno):
        '''Elimina la asignatura del conjunto de asignaturas que se imparten en el aula. Si no se lanzará una
        excepción'''
        error_msg = "Alumno no matriculado. Alumno: "+str(alumno)
        Utilidades.remove_elemento(alumno, self.__alumnnos, error_msg)

    def hay_alumnos_matriculados(self, asignatura):
        """Devuelve True si en el curso hay alumnos matriculados de dicha asignatura"""
        matriculados = False
        contador = 0
        while not matriculados and contador < len(self.__alumnos):
            for a in self.__alumnos[contador].asignaturas_matricula:
                if a == asignatura:
                    matriculados = True
            if not matriculados:
                contador += 1
        return matriculados

    """Gestión de profesores"""

    def add_profesor(self, profesor):
        '''Añade un profesor a la colección de profesores'''
        error_msg = "Profesor previamente registrado. Profesor: " + str(profesor)
        Utilidades.add_elemento(profesor, self.__profesores, error_msg)

    def esta_profesor_en_curso(self, profesor):
        '''Nos indica si el profesor está asignado al curso'''
        return Utilidades.esta_elemento(profesor, self.__profesores)

    def remove_profesor(self, profesor):
        '''Elimina el profesor del conjunto de profesores que imparten en el curso. Si no existe se lanzará una
        excepción'''
        # No podemos eliminar un profesor si hay asignaturas que son impartidas por él
        if self.hay_asignaturas_impartidas_por(profesor):
            raise ValueError("Profesor no eliminado. Asignaturas impartidas por él.")
        error_msg = "Profesor no registrado. Profesor: " + profesor.dni
        Utilidades.remove_elemento(profesor, self.__profesores, error_msg)

    def get_profesor(self, profesor):
        '''Devuelve el profesor de la lista de profesores registrados. Se basa internamente en buscarlo en su DNI. Los
        datos reales de los profesores están en la lista de profesores del aula'''
        if self.esta_profesor_en_curso(profesor):
            index = self.profesores.index(profesor)
            return self.profesores[index]
        else:
            raise ValueError("Profesor no registrado. Profesor "+str(profesor))

    def __eq__(self, aula):
        return self.codigo == aula.codigo

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => Código: {1}\nProfesores: \n"

        for profesor in self.__profesores:
            msg += str(profesor) + "\n"

        msg += "Asignaturas:\n"

        for asignatura in self.__asignaturas:
            msg += str(asignatura) + "\n"

        msg += "Alumnos:\n"

        for alumno in self.alumnos:
            msg += str(alumno)+"\n"

        return msg.format(clase, self.codigo)

    def to_dictionary(self):
        # Convierte la información del aula en un diccionario
        aula_dict = {}
        aula_dict.setdefault(self.codigo, {})
        datos_aula = aula_dict[self.codigo]
        asignaturas = {}
        alumnos = {}
        profesores = {}

        for profesor in self.__profesores:
            profesores.update(profesor.to_dictionary())
        datos_aula["profesores"] = profesores

        for asignatura in self.__asignaturas:
            asignaturas.update(asignatura.to_dictionary())
        datos_aula["asignaturas"] = asignaturas

        for alumno in self.__alumnos:
            alumnos.update(alumno.to_dictionary())
        datos_aula["alumnos"]=alumnos

        aula_dict[self.codigo] = datos_aula
        return aula_dict