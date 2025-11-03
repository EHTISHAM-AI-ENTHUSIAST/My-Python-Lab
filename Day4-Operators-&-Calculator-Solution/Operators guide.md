# Python Operators - A Simple Guide

Python uses special symbols called operators to perform calculations. Think of them as basic math symbols you use in everyday life. Here are the main ones you need to know:

1. **Addition (+)**
   - Just like regular addition
   - Example: `5 + 3 = 8`

2. **Subtraction (-)**
   - Works like normal subtraction
   - Example: `10 - 4 = 6`

3. **Multiplication (*)**
   - Used to multiply numbers
   - Example: `4 * 3 = 12`

4. **Division (/)**
   - Divides one number by another
   - Example: `10 / 2 = 5.0`

5. **Modulus (%)**
   - Gives you the remainder after division
   - Example: `7 % 3 = 1` (because 7 divided by 3 leaves remainder 1)

6. **Floor Division (//)** 
   - Similar to regular division but removes the decimal part
   - Example: `7 // 3 = 2` (because 7 divided by 3 is 2.33..., floor division gives just 2)

7. **Exponential (**)** 
   - Used for raising a number to a power
   - Example: `2 ** 3 = 8` (2 raised to power 3)

## Practice Example
Here's a real-world example using numbers 15 and 7:
```python
15 + 7  = 22    (Addition)
15 - 7  = 8     (Subtraction)
15 * 7  = 105   (Multiplication)
15 / 7  = 2.14  (Division)
15 % 7  = 1     (Modulus - remainder after dividing 15 by 7)
15 // 7 = 2     (Floor Division - whole number result of 15 divided by 7)
```

## Code Example
```python
n = 15
m = 7
ans1 = n + m
print("Addition of", n, "and", m, "is", ans1)
ans2 = n - m
print("Subtraction of", n, "and", m, "is", ans2)
ans3 = n * m
print("Multiplication of", n, "and", m, "is", ans3)
ans4 = n / m
print("Division of", n, "and", m, "is", ans4)
ans5 = n % m
print("Modulus of", n, "and", m, "is", ans5)
ans6 = n // m
print("Floor Division of", n, "and", m, "is", ans6)
```

This is the foundation for creating a basic calculator in Python. Each operator performs a specific mathematical operation, just like the buttons on a regular calculator!