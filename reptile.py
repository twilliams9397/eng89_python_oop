# create Reptile class to inherit Animal class

from animal import Animal # from file import class, use absolute path if not in same directory

class Reptile(Animal): # creates Reptile as sub class of Animal - inheritance

    def __init__(self):
        super().__init__() # super() is used to inherit everything from parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chamber = [3, 4]

    def seek_heat(self):
        return "It's cold - look for the sun!"

    def hunt(self):
        return "Keep looking for food!"

    def use_venom(self):
        return "If I have it I will use it!"

# create object of Reptile class

smart_reptile = Reptile()
# print(smart_reptile.breath()) # breathe method inherited from Animal class
# print(smart_reptile.hunt()) # hunt is available in Reptile class
# print(smart_reptile.cold_blooded) # Reptile attribute
# print(smart_reptile.lungs) # inherited Animal attribute
