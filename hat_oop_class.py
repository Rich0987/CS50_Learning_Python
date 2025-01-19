# decorator / function
# for classes
#
#     @classmethod  # not an instance that has access to self, but does know what class it is inside

#sorting hat in harry potter
import random

class Hat:
    def __init__(self):               #need to initialize self
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in", house)

hat = Hat()
hat.sort("Harry")

