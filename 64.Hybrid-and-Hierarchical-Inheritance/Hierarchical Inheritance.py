class Parent:
    def func1(self):
        print("This is the Parent class.")

class Child1(Parent):
    def func2(self):
        print("This is Child 1.")

class Child2(Parent):
    def func3(self):
        print("This is Child 2.")

# --- Using Hierarchical ---
obj1 = Child1()
obj2 = Child2()

obj1.func1() # Works
obj1.func2() # Works

obj2.func1() # Works
obj2.func3() # Works
# obj2.func2() # Error! (Child2 cannot access Child1)