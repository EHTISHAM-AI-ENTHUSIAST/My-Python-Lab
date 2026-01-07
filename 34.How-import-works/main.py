# we are learning about how imports work in python

import math

result = math.sqrt(9)
print(result)  # Output: 3.0


from datetime import datetime
now = datetime.now()
print(now)  # Output: current date and time

import os
current_directory = os.getcwd()
print(current_directory)  # Output: current working directory path

from random import randint
random_number = randint(1, 10)
print(random_number)  # Output: random number between 1 and 10


import sys
print(sys.version)  # Output: Python version information


from collections import Counter
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'apple']
counter = Counter(data) 
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

import json
data_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
json_data = json.dumps(data_dict)
print(json_data)  # Output: JSON string representation of data_dict



#import everything from a module

from math import *

print(cos(0))       # Output: 1.0

result = sqrt(9)
print(result)  # Output: 3.0
print(pi)  # Output: 3.141592653589793


#The "as" keyword

import math as m
result = m.sqrt(9)
print(result)  # Output: 3.0
print(m.pi)  # Output: 3.141592653589793

#The dir function

import math
print(dir(math))  # Output: List of all attributes and methods in the math module