# PARENT CLASS
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

# CHILD CLASS (Inheriting from only ONE class)
class Dog(Animal):
    def __init__(self, name, breed):
        # Using super() to call Parent's constructor
        super().__init__(name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

# --- Using Single Inheritance ---
d = Dog("Buddy", "Golden Retriever")
d.make_sound() # Calls Dog's version (Method Overriding)

# Accessing Parent Class attribute
print(f"Name: {d.name}, Species: {d.species}, Breed: {d.breed}")