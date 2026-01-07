#dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 30


# Adding a new key-value pair
my_dict["job"] = "Engineer"
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# Updating an existing value
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# Removing a key-value pair
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'job': 'Engineer'}
removed_value = my_dict.pop("job")
print(removed_value)  # Output: Engineer
print(my_dict)  # Output: {'name': 'Alice', 'age': 31

# Iterating through the dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 31

# Checking if a key exists
if "name" in my_dict:
    print("Name exists in the dictionary.")
# Output: Name exists in the dictionary.

# Getting all keys and values
keys = my_dict.keys()
values = my_dict.values()
print(keys)    # Output: dict_keys(['name', 'age'])
print(values)  # Output: dict_values(['Alice', 31])
# Output: {'name': 'Alice', 'age': 31}

print(my_dict)  # Output: {'name': 'Alice', 'age': 31}

