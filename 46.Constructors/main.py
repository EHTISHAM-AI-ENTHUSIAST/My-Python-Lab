#example of default Constructor in Python
class Details:
    def __init__(self):
        self.animal = "Crab"
        self.group = "Crustaceans"

obj = Details()
print(obj.animal, "belongs to the", obj.group, "group.")





#example of Parameterized Constructor in Python
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("hen", "birds")
print(obj1.animal, "belongs to the", obj1.group, "group.")

obj2 = Details("fish", "octopuses")
print(obj2.animal, "belongs to the", obj2.group, "group.")