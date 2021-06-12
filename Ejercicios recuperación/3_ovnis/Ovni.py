from Alien import Alien

class Ovni():

    def __init__(self, id, pos_x):
        self.id = id
        self.pos_x = pos_x
        self.aliens = []

    @property
    def aliens(self):
        return self.__aliens

    @property
    def id(self):
        return self.__id

    @property
    def pos_x(self):
        return self.__pos_x

    @pos_x.setter
    def pos_x(self, pos_x):
        self.__pos_x = pos_x
    
    @aliens.setter
    def aliens(self, aliens):
        self.__aliens = aliens

    @id.setter
    def id(self, id):
        self.__id = id

    def add_alien(self, alien):
        self.__aliens.append(alien)

    def desplazar(self, distancia, direccion):
        
        if direccion == "IZQDA":
            self.pos_x -= distancia
        else:
            self.pos_x += distancia

        for a in self.aliens:
            a.pos_x = self.pos_x
            
        # No permitimos salirnos del límite -200, 200
        if self.pos_x < -200:
            self.pos_x = -200
        if self.pos_x > 200:
            self.pos_x = 200


    def abducir(self, humano):
        if humano.es_abducido():
            humano = Alien(humano.id, humano.nombre, self.pos_x, self.pueblo, self)
        self.add_alien(humano)
        humano.recibir_abduccion()

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => Nombre: {1}, Pos: {2}\nAliens: \n"
        for p in self.aliens:
            msg += p.__str__()+"\n"
        return msg.format(clase, self.id, self.pos_x)