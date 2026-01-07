# walrus operator :=
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

#----------------- example 1:
# print(n := 10)
#----------------- example 2:
# happy = False
# print(happy)
# print(happy := True)


#----------------old way:
# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#       break
#   foods.append(food)

#----------------- new way with walrus operator
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)