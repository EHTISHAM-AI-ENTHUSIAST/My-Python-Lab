#we are using enumerate to get both index and value from the list

marks = [12, 56, 32, 98, 45]

for index, mark in enumerate(marks):
    print(f"ON Index {index} marks are: {mark}")
    if(index == 3):
        print("Ali, amazing!")

# another example using start parameter in enumerate

fruits = ['apple', 'banana', 'mango']

for index, fruit in enumerate(fruits, start=1):
    print(f"Fruit number {index} is {fruit}")