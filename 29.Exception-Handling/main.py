# we are learning about exception handling in Python
# so if you enter a non-integer value, it will raise a ValueError
try:
    num = int(input("Enter an integer: "))
    print(f"You entered the integer: {num}")
except ValueError:
    print("Number entered is not an integer.")