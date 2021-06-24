# create Animal class

class Animal: # capital letter used for classes
    # we need to initialise with built in method __init__(self)
    # self refers to current class
    def __init__(self): # declare attributes inside init method
        self.alive = True # setting class variables
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breath(self):
        return "Keep breathing to stay alive!"

    def eat(self):
        return "Time to eat!"

    def move(self):
        return "Move left and right to stay awake!"

# need to create an object of this class to use methods within class

cat = Animal() # creating an object of animal class
# for cat as a user the functionality inside Animal and the methods is abstracted
# print(cat.eat()) #these will run with class when imported in other scripts
# print(cat.breath())
# print(cat.lungs)
