from Personaje import Personaje

class Alien(Personaje):

    def __init__(self, id, nombre, pos_x, pueblo, ovni):
        super().__init__(id, nombre, pos_x, pueblo)
        self.ovni = ovni

    @property
    def ovni(self):
        return self.__ovni

    @ovni.setter
    def ovni(self, ovni):
        self.__ovni = ovni
    
    
    def __str__(self):
        clase = type(self).__name__
        msg = super().__str__()+ " => {0}"
        return msg.format(clase)