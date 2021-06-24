# create Python class to inherit Snake class

from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True

    def digest_large_prey(self):
        return "I can eat and digest anything without chewing!"

    def climb(self):
        return "I can climb trees easily!"

    def __shed_skin(self):  # this __ hides the data
        return "I am growing out of my skin!"


fast_python = Python()
# print(fast_python.climb()) # Python method
# print(fast_python.use_tongue_to_smell()) # Snake method
# print(fast_python.seek_heat()) # Reptile method
# print(fast_python.move()) # Animal method
