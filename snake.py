# create Snake class to inherit Reptile class

from reptile import Reptile # as Reptile inherited Animal, inheriting Reptile inherits both

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return "I can work out what is near me with my tongue!"

smart_snake = Snake()
# print(smart_snake.use_tongue_to_smell()) # Snake behaviour
# print(smart_snake.hunt()) # Reptile behaviour
# print(smart_snake.move()) # Animal behaviour
