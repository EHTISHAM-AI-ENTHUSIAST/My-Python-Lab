# Typecasting (Type Conversion) — simple guide

Typecasting means changing a value from one data type to another (for example, from a string to an integer). In Python you commonly use built-in functions such as int(), float(), str(), list(), tuple(), dict(), set(), etc.

There are two kinds of type conversion in Python:

1. Explicit conversion — you (the programmer) convert values manually.
2. Implicit conversion — Python converts values automatically to avoid losing data.

### Explicit conversion (manual)
When you convert a value yourself using a function like int() or float(), that is explicit conversion. This is useful when you know the data should be treated as a certain type.

Example:
```python
string = "15"
number = 7
# Convert the string '15' to integer before adding
string_number = int(string)  # will raise ValueError if string is not a valid integer
result = number + string_number
print("The sum is:", result)
```

Output:
```
The sum is: 22
```

Tips / edge cases:
- Converting a non-numeric string with int() or float() will raise a ValueError.
- Use try/except if input might be invalid.

### Implicit conversion (automatic)
Python sometimes converts values automatically during operations so that the result keeps precision. For example, when you add an int and a float, Python converts the int to float first.

Example:
```python
a = 7        # int
b = 3.0      # float
print(type(a))
print(type(b))

c = a + b    # a is converted to float, result is float
print(c)
print(type(c))
```

Output:
```
<class 'int'>
<class 'float'>
10.0
<class 'float'>
```

Summary:
- Use explicit conversion when you need a specific type (int(), float(), str(), etc.).
- Rely on implicit conversion when mixing numeric types — Python will upcast smaller types to larger ones automatically.

If you want, I can also add a short section showing safe conversions with try/except or examples converting lists/tuples/dicts. 
