# coding=utf-8
from Constants import *
import random

class Member():

    def __init__(self, id, name, room):
        self.id = id
        self.name = name
        self.room = room
        self.alive = True
        self.__missions = [room]

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def room(self):
        return self.__room

    @property
    def alive(self):
        return self.__alive

    @property
    def missions(self):
        return self.__missions

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @room.setter
    def room(self, room):
        self.__room = room

    @alive.setter
    def alive(self, alive):
        self.__alive = alive
        
    def add_mission(self, room):
        if not room in self.missions:
            self.missions.append(room)

    def move_to_room(self, room):
        """Nos moveremos a la sala siempre, pero sólo añadiremos la misión en el caso en el que
        no esté ya realizada (dicha comprobación está en add_mission)"""
        self.room = room
        self.add_mission(room)

    def be_killed(self):
        """Cuando un tripulante es asesinado, se notifica a la sala que se ha producido el asesinato"""
        if self.is_safe():
            raise ValueError("Tripulante "+self.id+" está a salvo y no puede ser asesinado.")
        if not self.alive: 
            raise ValueError("Tripulante "+self.id+" ya está muerto y no puede ser asesinado.")
        self.alive = False
        self.room.someone_has_died()

    def vote(self, max_members):
        """Devolvemos aleatoriamente un miembro resultado de la votación"""
        return random.randrange(0, max_members)

    def is_safe(self):
        """Está a salvo si ha completado todas las misiones"""
        return len(self.missions) == N_ROOMS

    def __eq__(self, member):
        return self.id == member.id
        
    def __str__(self):
        clase = type(self).__name__

        msg = "{0} => ID: {1}, Nombre: {2}, Sala: {3}\nMisiones: ["
        for m in self.missions:
            msg += m.id+" "
        msg += "] => "
        if self.alive:
            msg += "VIVO"
        else: 
            msg += "MUERTO"
        
        return msg.format(clase, self.id, self.name, self.room.id)