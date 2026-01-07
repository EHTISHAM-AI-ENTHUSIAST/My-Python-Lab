class Parent:
    def parent_method(self):
        print("This is parent method.")

class Child(Parent):
    def child_method(self):
        print("This is child method.")
        
        super().parent_method()

c = Child()
c.child_method()