from Humano import Humano
from Alien import Alien
from Ovni import Ovni
from Pueblo import Pueblo
import random

class PuebloFactory:

    def generate_pueblo(nombre, num_humanos, num_ovnis, num_aliens):
        p = Pueblo(nombre)
        for i in range(num_humanos):
            p.add_humano(Humano("h" + str(i), "humano" + str(i), random.randrange(-200, 200), p))
        for i in range(num_ovnis):
            o = Ovni("ovni"+str(i), random.randrange(-200,200))
            for j in range(num_aliens):
                o.add_alien(Alien("a"+str(i), "alien"+str(i), 0, p, o))
            p.add_ovni(o)
        return p