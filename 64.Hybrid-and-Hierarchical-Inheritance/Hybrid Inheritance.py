class School:
    def func1(self):
        print("This is School.")

class Student1(School): # Single Inheritance
    def func2(self):
        print("This is Student 1.")

class Student2(School): # Hierarchical Inheritance
    def func3(self):
        print("This is Student 2.")

class Student3(Student1, School): # Multiple Inheritance
    def func4(self):
        print("This is Student 3.")