import random


class Hat:
    # def __init__(self):
        # self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    # class variables
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # 不要給特定
    @classmethod
    # cls = class
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

# hat = Hat()
# hat.sort("Harry")
Hat.sort("Harry")