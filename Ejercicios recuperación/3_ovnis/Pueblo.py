
class Pueblo():

    def __init__(self, nombre):
        self.nombre = nombre
        self.humanos = []
        self.ovnis = []

    @property
    def humanos(self):
        return self.__humanos

    @property
    def ovnis(self):
        return self.__ovnis

    @property
    def nombre(self):
        return self.__nombre

    @humanos.setter
    def humanos(self, humanos):
        self.__humanos = humanos

    @ovnis.setter
    def ovnis(self, ovnis):
        self.__ovnis = ovnis

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def add_humano(self, humano):
        self.__humanos.append(humano)

    def add_ovni(self, ovni):
        self.__ovnis.append(ovni)

    def hay_supervivientes(self):
        return len(self.humanos) > 0

    def ordenar_elementos(self):
        self.humanos.sort(key = lambda elemento: elemento.pos_x)
        self.ovnis.sort(key = lambda elemento: elemento.pos_x)

    def humano_abducido(self, humano):
        self.humanos.remove(humano)

    def desencadenar_abducciones(self):
        """ Comprueba si los ovnis se encuentran en la misma posición que los humanos para abducirlos"""
        for ovni in self.ovnis:
            for humano in self.humanos:
                if ovni.pos_x == humano.pos_x:
                    ovni.abducir(humano)

    def __str__(self):
        """Mostrará el pueblo ordenando los personajes por posición"""
        self.ordenar_elementos()
        
        clase = type(self).__name__
        msg = "{0} => Nombre: {1}\nElementos: \n"
        for p in self.humanos:
            msg += p.__str__()+"\n"
        for o in self.ovnis:
            msg += o.__str__()+"\n"
        return msg.format(clase, self.nombre)