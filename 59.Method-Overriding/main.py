class Shape:
    def area(self):
        print("Calculating area of a generic shape...")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # METHOD OVERRIDING: Same name as parent class method
    def area(self):
        # We can still use the parent's logic if we want using super()
        # super().area() 
        print(f"Calculating area of Circle: {3.14 * self.radius * self.radius}")

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    # METHOD OVERRIDING
    def area(self):
        print(f"Calculating area of Rectangle: {self.l * self.w}")

# --- Using Overriding ---
s = Shape()
s.area() # Calls parent method

c = Circle(5)
c.area() # Calls Overridden method in Circle

r = Rectangle(10, 5)
r.area() # Calls Overridden method in Rectangle