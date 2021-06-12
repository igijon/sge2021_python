from Constants import *
from Factorias.SpacecraftFactory import SpacecraftFactory
import random

def try_move_member(member, spacecraft):
    try:
        #Decidimos si se mueve o no
        move = random.randint(0, 2)
        
        if move != 0: # Se moverá
            #Elegimos aleatoriamente la sala
            room = random.randint(0, N_ROOMS-1)
            spacecraft.move_member(member, member.room, spacecraft.rooms[room])
    except ValueError as e:
        print(e)

def try_move_impostor(impostor, spacecraft):
    try:
        #Decidimos si se mueve o no
        move = random.randint(0, 2)
        
        if move != 0: # Se moverá
            #Elegimos aleatoriamente la sala
            room = random.randint(0, N_ROOMS-1)
            spacecraft.move_impostor(impostor, impostor.room, spacecraft.rooms[room])
    except ValueError as e:
        print(e)

def movements(spacecraft):
    for r in spacecraft.rooms:
        for m in r.members:
            if m.alive:
                try_move_member(m, spacecraft)
        for i in r.impostors:
            if not i.expelled:
                try_move_impostor(i, spacecraft)

# Comienza flujo del programa
ship = SpacecraftFactory.new_spacecraft("Virgen Ship")
print(ship)
while ship.are_members_in_danger() and ship.are_impostors():
    movements(ship)
    ship.trigger_murders()
    print(ship)
    key = input("Presione una tecla ...")

if not ship.are_impostors():
    print("SE HAN DESENMASCARADO TODOS LOS IMPOSTORES: GANAN LOS TRIPULANTES")
else:
    print("NO SE PUEDEN MATAR MÁS TRIPULANTES: GANAN LOS IMPOSTORES")


