# Python Tuples
# Tuple items are  enclosed within round brackets (), unchangeable after creation.

#example of tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

# Accessing tuple items
print(my_tuple[1])  # Output: banana

# Tuples are immutable
# my_tuple[1] = "orange"  # This will raise a TypeError

# Tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)
print(mixed_tuple)
# Tuple unpacking
a, b, c = ("red", "green", "blue")
print(a)  # Output: red
print(b)  # Output: green
print(c)  # Output: blue

