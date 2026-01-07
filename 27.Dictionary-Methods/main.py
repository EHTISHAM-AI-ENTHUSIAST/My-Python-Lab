# we are learning dictionary methods

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using the get() method to retrieve a value
value_a = my_dict.get('a')
print(f"Value for key 'a': {value_a}")

# Using the keys() method to get all keys
keys = my_dict.keys()
print(f"Keys in the dictionary: {list(keys)}")

# Using the values() method to get all values
values = my_dict.values()
print(f"Values in the dictionary: {list(values)}")

# Using the items() method to get all key-value pairs
items = my_dict.items()
print(f"Items in the dictionary: {list(items)}")

# Using the pop() method to remove a key-value pair
removed_value = my_dict.pop('b')
print(f"Removed value for key 'b': {removed_value}")
print(f"Dictionary after popping key 'b': {my_dict}")

# Using the update() method to add a new key-value pair
my_dict.update({'d': 4})
print(f"Dictionary after updating with new key 'd': {my_dict}")

# Using the clear() method to remove all items from the dictionary
my_dict.clear()
print(f"Dictionary after clearing all items: {my_dict}")

# Using the fromkeys() method to create a new dictionary
new_dict = dict.fromkeys(['x', 'y', 'z'], 0)
print(f"New dictionary created using fromkeys(): {new_dict}")
# Using the setdefault() method to get a value or set a default
default_value = new_dict.setdefault('x', 10)
print(f"Value for key 'x' after setdefault(): {default_value}")
print(f"New dictionary after setdefault(): {new_dict}")


