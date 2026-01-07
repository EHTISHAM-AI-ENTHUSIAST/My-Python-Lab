# -------------dir() Example-------------


x = [1, 2, 3]
print(dir(x)) 
# It will show everything you can do with a list: append, pop, reverse, etc.

# -------------__dict__ Example-------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Ali", 25)
print(p1.__dict__) 
# Output: {'name': 'Ali', 'age': 25}


# -------------help() Example-------------

class Employee:
    """This class stores employee information."""
    def __init__(self, name):
        self.name = name

# help(Employee) 
# It will show the docstring and all methods available in the class.