cube = lambda x: x * x * x


l = [1, 2, 4, 6, 3]

# old way (For loop):
newL = []
for item in l:
    newL.append(cube(item))
print(newL)


# new way (Map):
new_list = list(map(cube, l))
print(new_list)
