#sets methods in python


info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")



cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

common_cities = cities.intersection(cities2)
print("Common cities:", common_cities)

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print("Fruits after adding orange:", fruits)


numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print("Numbers after removing 3:", numbers)

A = {"red", "blue", "green"}
B = {"blue", "yellow", "pink"}
difference = A.difference(B)
print("Difference between A and B:", difference)


set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
symmetric_diff = set1.symmetric_difference(set2)
print("Symmetric difference between set1 and set2:", symmetric_diff)

animals = {"cat", "dog", "rabbit"}
animals.clear() 
print("Animals set after clearing:", animals)

vegetables = {"carrot", "potato", "tomato"}
vegetables.discard("potato")
print("Vegetables after discarding potato:", vegetables)

colors = {"red", "green", "blue"}
colors_copy = colors.copy()
print("Copy of colors set:", colors_copy)

setA = {"apple", "banana", "cherry"}
setB = {"banana", "cherry", "date"}
is_subset = setB.issubset(setA)
print("Is setB a subset of setA?", is_subset)