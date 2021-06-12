

class Room():

    def __init__(self, id):
        self.id = id
        self.members = []
        self.impostors = []

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def add_member(self, member):
        self.members.append(member)

    def add_impostor(self, impostor):
        self.impostors.append(impostor)

    def remove_member(self, member):
        if member not in self.members:
            raise ValueError("Tripulante "+member.id+" no puede salir de la sala porque no está en ella.")
        self.members.remove(member)

    def remove_impostor(self, impostor):
        if impostor not in self.impostors:
            raise ValueError("Impostor "+impostor.id+" no puede salir de la sala porque no está en ella.")
        self.impostors.remove(impostor)
        
    def someone_has_died(self):
        """Alguien ha muerto en la sala, por lo tanto hay que intentar encontrar al impostor"""
        #Cada miembro (menos el muerto) tendrá que votar entre todos los que están
        #El que más votos tenga se tendrá que comprobar si es impostor,
        #Si lo es ... será expulsado, si no ... continuará el juego
        total_members = len(self.members)+len(self.impostors)
        # Vamos a tener una lista en la que cada posición se corresponderá
        # con un tripulante y el valor será los votos recibidos
        # Las primeras posiciones las ocuparán los triupantes y las últimas los 
        # impostores
        votes_list=[0]*total_members
        for m in self.members:
            votes_list[m.vote(total_members)]+=1       

        #Los impostores también votan
        for i in self.impostors:
            votes_list[i.vote(total_members)]+=1

        # Vamos a ver quién ha sido elegido como impostor
        id_supossed = votes_list.index(max(votes_list))
        if id_supossed >= len(self.members):
            # Se ha elegido un impostor y éste será expulsado
            id_impostor = id_supossed - len(self.members)
            self.impostors[id_impostor].be_expelled()
    
    def are_impostors(self):
        are_impostors = False
        for i in self.impostors:
            if not i.expelled: 
                are_impostors = True
        return are_impostors

    def all_members_are_safe_or_died(self):
        all_members_are_safe_or_died = True
        for m in self.members:
            if (not m.is_safe()) and m.alive:
                all_members_are_safe_or_died = False
        return all_members_are_safe_or_died
        
    def __eq__(self, room):
        return self.id == room.id
        
    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => Id: {1}\nTripulantes: \n"
        for t in self.members:
            msg += t.__str__()+"\n"
        for i in self.impostors:
            msg += i.__str__()+"\n"
        return msg.format(clase, self.id)