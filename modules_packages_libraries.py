# pythons extensive documentation on python.org
# have used functions we created as well as built in

# import is keyword used to import any available python modules

# math
import math # imports whole class
from random import random # imports specific file from class

num1 = 23.44 # float

# have to round figure depending on value
# if value is less the .50 round down, if .50 or above round up

print(math.ceil(num1)) # rounds up to next integer
print(math.floor(num1)) # rounds down to next integer
print(math.pi)

# if specific file is imported it doesn't need to be called from class
print(random()) # random number between 0 and 1 everytime it is run
