# dont need __init__ with @classmethod... removes self

import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):                    #now it's a class/cls variable and not an instance/init
        house = random.choice(cls.houses)
        print(name, "is in", house)

Hat.sort("Harry")