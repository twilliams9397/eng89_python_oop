# Python OOP
## Four Pillars of OOP
### Functions and good practice of functions
```python
# creating a function
# syntax def name_of_function(inputs) is used to declare a function

def greeting():
    print("Welcome on board, enjoy your trip!")
# pass can be used to skip without any errors

greeting() # function must be called to give output
```
- calling the above function will print out the string as the print statement is part of the function
- functions can also have a return function which returns variables which can later be called:
```python
def greeting():
    print("Good morning.")
    return "Welcome on board, enjoy your trip!"

print(greeting())
```
- this function will print the `"Good morning."` string then print the returned string afterwards
- the returned line is always what is outputted last from the function
- functions can take inputs from either the code or user inputs and run the code with this data:
```python
def greeting(name):
    return "Welcome on board " + name + "!"

print(greeting("Tom")) # this line is calling the function for "Tom"
```
```python
def greeting(name):
    return "Welcome on board " + name + "!"

print(greeting(input("What is your name?  ").capitalize()))
```
#### DRY Don't Repeat Yourself