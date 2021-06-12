from Personaje import Personaje
import random

class Humano(Personaje):

    def __init__(self, id, nombre, pos_x, pueblo):
        super().__init__(id, nombre, pos_x, pueblo)

    def es_abducido(self):
        if random.randint(1,10) <= 20:
            return False
        else:
            return True

    def recibir_abduccion(self):
        self.pueblo.humano_abducido(self)
        
    def __str__(self):
        clase = type(self).__name__

        msg = super().__str__()+ " => {0}"
        
        return msg.format(clase)

