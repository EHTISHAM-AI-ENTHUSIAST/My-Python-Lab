a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True 
print(a is b)  # Output: False (because they are different objects in memory)




a = [1, 2, 3]
b = a  # b is now referencing the same object as a
print(a == b)  # Output: True
print(a is b)  # Output: True (because they reference the same object in memory)




a = [1, 2]
b = [1, 2]
print(id(a)) # let: 12345
print(id(b)) # let: 67890 (different address)




a = 3
b = 3
print(a == b) # True
print(a is b) # True (because small integers are cached in Python)

