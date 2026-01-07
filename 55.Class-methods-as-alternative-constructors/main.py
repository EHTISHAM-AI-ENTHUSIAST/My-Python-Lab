class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        name, salary = string.split("-")
        return cls(name, int(salary))

# --- Using the Class ---

# 1. Standard way
e1 = Employee("Harry", 12000)
print(e1.name, e1.salary)

# 2. Alternative way (Using string directly)
string = "Rohan-15000"
e2 = Employee.fromStr(string)

print(e2.name, e2.salary)