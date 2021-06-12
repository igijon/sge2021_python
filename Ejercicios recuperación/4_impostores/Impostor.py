from Member import Member

class Impostor(Member):

    def __init__(self, id, name, room):
        super().__init__(id, name, room)
        self.expelled = False

    @property
    def expelled(self):
        return self.__expelled

    @expelled.setter
    def expelled(self, value):
        self.__expelled = value

    def kill(self, member):
        """Podremos asesinar si:
            - Está vivo
            - No está a salvo 
        """
        if not member.is_safe() and member.alive:
            member.be_killed()

    def be_expelled(self):
        if self.expelled:
            raise ValueError("Impostor "+self.id+" ya está expulsado y no se puede expulsar de nuevo.")
        self.expelled = True
    
    def __eq__(self, impostor):
        return self.id == impostor.id
        
    def __str__(self):
        clase = type(self).__name__

        msg = super().__str__() + " => "
        if self.expelled:
            msg += "EXPULSADO"
        else:
            msg += " EN LA NAVE "
        
        return msg
