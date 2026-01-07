class Student:
    name = "Ali"
    marks = 85

    def info(self):
        print(f"{self.name} has {self.marks} marks")

# Object making (Instantiation)
obj1 = Student()
obj1.name = "Ahmed"
obj1.marks = 90
obj1.info()

obj2 = Student()
obj2.name = "Sara"
obj2.marks = 95
obj2.info()