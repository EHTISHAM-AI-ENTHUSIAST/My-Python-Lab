age = 15

if (age >= 0):
    if (age >= 18):
        print("You can watch all movies!")
    elif (age >= 13):
        print("You can watch PG-13 and PG movies")
    elif (age >= 7):
        print("You can only watch PG movies")
    else:
        print("You're too young for most movies")
else:
    print("Please enter a valid age!")