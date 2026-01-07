class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name is {self.name} and I am an Employee.")

class Dancer:
    def __init__(self, dance_style):
        self.dance_style = dance_style
    def show(self):
        print(f"I am a dancer and my style is {self.dance_style}.")

# MULTIPLE INHERITANCE (Inheriting from both Employee and Dancer)
class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance_style):
        self.name = name
        self.dance_style = dance_style

# --- Using Multiple Inheritance ---
o = DancerEmployee("Shivani", "Kathak")

# Which 'show()' will be called? 
# Since 'Employee' was written first in the bracket, it will be called.
o.show() 

# To see the order Python follows:
print(DancerEmployee.mro())