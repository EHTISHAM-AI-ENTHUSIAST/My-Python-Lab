class Student:
    def __init__(self):
        self._schoolName = "City School" # Protected variable

class Topper(Student):
    def show(self):
        print(self._schoolName) # Accessible in child class

obj = Topper()
obj.show()