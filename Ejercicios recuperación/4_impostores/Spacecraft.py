
class Spacecraft():

    def __init__(self, id, rooms):
        self.id = id
        self.rooms = rooms

    @property
    def id(self):
        return self.__id

    @property
    def rooms(self):
        return self.__rooms

    @id.setter
    def id(self, id):
        self.__id = id

    @rooms.setter
    def rooms(self, rooms):
        self.__rooms = rooms

    def are_impostors(self):
        are_impostors = False
        for r in self.rooms:
            if r.are_impostors():
                are_impostors = True
        return are_impostors

    def are_members_in_danger(self):
        danger = False
        for r in self.rooms:
            if not r.all_members_are_safe_or_died():
                danger = True
        return danger

    def move_member(self, member, source_room, final_room):
        index_source_room = self.rooms.index(source_room)
        if member not in self.rooms[index_source_room].members:
            raise ValueError("Tripulante "+member.id+"  no está en la sala "+source_room.id)    
        self.rooms[index_source_room].remove_member(member)
        index_final_room = self.rooms.index(final_room)
        self.rooms[index_final_room].add_member(member)
        member.move_to_room(final_room)

    def move_impostor(self, impostor, source_room, final_room):
        index_source_room = self.rooms.index(source_room)
        if impostor not in self.rooms[index_source_room].impostors:
            raise ValueError("Impostor "+impostor.id+"  no está en la sala "+source_room.id)    
        self.rooms[index_source_room].remove_impostor(impostor)
        index_final_room = self.rooms.index(final_room)
        self.rooms[index_final_room].add_impostor(impostor)
        impostor.move_to_room(final_room)

    def trigger_murders(self):
        for r in self.rooms:
            for i in r.impostors:
                if len(r.members) > 0:
                    next_victim = False
                    n = 0
                    while not next_victim and n < len(r.members):
                        if r.members[n].alive:
                            i.kill(r.members[n])
                            next_victim = True
                        n += 1

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => id: {1}\nSalas: \n"
        for r in self.rooms:
            msg += r.__str__()+"\n"
        return msg.format(clase, self.id)