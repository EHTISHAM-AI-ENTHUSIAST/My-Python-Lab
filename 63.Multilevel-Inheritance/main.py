# Level 1: Grandparent Class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def show_details(self):
        print(f"Name: {self.name}, Species: {self.species}")

# Level 2: Parent Class (Inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
    def show_dog_details(self):
        print(f"Breed: {self.breed}")

# Level 3: Child Class (Inherits from Dog)
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
    def show_all_info(self):
        self.show_details()      # From Grandparent
        self.show_dog_details()  # From Parent
        print(f"Color: {self.color}")

# --- Using Multilevel Inheritance ---
my_dog = GoldenRetriever("Buddy", "Golden")
my_dog.show_all_info()