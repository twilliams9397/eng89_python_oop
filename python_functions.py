# creating a function
# syntax def name_of_function(inputs) is used to declare a function

# def greeting():
#     print("Welcome on board, enjoy your trip!")
# # pass can be used to skip without any errors
#
# greeting() # function must be called to give output
#
# def greeting():
#     return "Welcome on board, enjoy your trip!"
#
# print(greeting())

# def greeting(name):
#     return "Welcome on board " + name
#
# print(greeting("Tom"))

def greeting(name):
    return "Welcome on board " + name + "!"

user = input("What is your name?  ").capitalize()

print(greeting(user))