class Employee:
    def __init__(self):
        self.__salary = "50k" # Private variable

obj = Employee()
# print(obj.__salary) # This will throw an ERROR

# How to access anyway (Name Mangling):
print(obj._Employee__salary) # Logic: _ClassName__VariableName