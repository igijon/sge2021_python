from Constants import *
from Room import *
from Member import *
from Impostor import *
from Spacecraft import *

class SpacecraftFactory:

    def new_spacecraft(id):
        rooms = []
        for r in range(N_ROOMS):
            rooms.append(Room("Sala"+str(r)))
        #Inicialmente los ponemos a todos en la sala 0
        for i in range(MAX_MEMBERS):
            rooms[0].add_member(Member("M"+str(i), "Miembro_"+str(i), rooms[0]))
        for i in range(MAX_IMPOSTORS):
            rooms[0].add_impostor(Impostor("I"+str(i), "Impostor_"+str(i), rooms[0]))
        n = Spacecraft(id, rooms)
        return n