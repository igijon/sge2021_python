# coding=utf-8
class Personaje():

    # Algunos valores están fijos como el límite de desplazamiento. Debería ser parametrizable pero para el ejemplo se deja así
    # La dirección también debería ser parametrizable
    def __init__(self, id, nombre, pos_x, pueblo):
        self.id = id
        self.nombre = nombre
        self.pos_x = pos_x
        self.pueblo = pueblo
        

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def pueblo(self):
        return self.__pueblo

    @property
    def pos_x(self):
        return self.__pos_x

    @id.setter
    def id(self, id):
        self.__id = id

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    
    @pos_x.setter
    def pos_x(self, pos_x):
        self.__pos_x = pos_x

    @pueblo.setter
    def pueblo(self, pueblo):
        self.__pueblo = pueblo

    def desplazar(self, distancia, direccion):
        """El personaje se desplaza una distancia en una dirección"""
       
        if direccion == "IZQDA":
            self.pos_x -= distancia
        else:
            self.pos_x += distancia

        # No permitimos salirnos del límite -200, 200
        if self.pos_x < -200:
            self.pos_x = -200
        if self.pos_x > 200:
            self.pos_x = 200

    def __str__(self):
        clase = type(self).__name__

        msg = "{0} => ID: {1}, Nombre: {2},  Posición: {3}"
        return msg.format(clase, self.id, self.nombre, self.pos_x)