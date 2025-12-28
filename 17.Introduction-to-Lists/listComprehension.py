# Example 1: Accepts items which have the letter "o"
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(1, namesWith_O)
# Output: ['Milo', 'Bruno', 'Rosa']



#Example 2: Accepts items which have more than 4 letters
list = ["Milo" ,"volsvoka", "Sara", "Brno", "Anastasia", "Rosa"]
longNames = [item for item in list if len(item) > 4]
print(2, longNames)
# Output: ['volsvoka', 'Anastasia']


# Example 3: Accepts even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = [num for num in numbers if num % 2 == 0]
print(3, evenNumbers)
# Output: [2, 4, 6, 8, 10]

# Example 4: Accepts numbers greater than 5
numbers = [1, 3, 5, 7, 9, 11, 13]
greaterThanFive = [num for num in numbers if num > 5]
print(4, greaterThanFive)
# Output: [7, 9, 11, 13]

# Example 5: Accepts items that start with the letter "A"
fruits = ["Apple", "Banana", "Avocado", "Cherry", "Apricot"]
aFruits = [fruit for fruit in fruits if fruit.startswith("A")]
print(5, aFruits)
# Output: ['Apple', 'Avocado', 'Apricot']

# Example 6: Accepts items that are not empty strings
strings = ["Hello", "", "World", " ", "Python", ""]
nonEmptyStrings = [s for s in strings if s]
print(6, nonEmptyStrings)
# Output: ['Hello', 'World', ' ', 'Python']

# Example 7: Accepts numbers that are multiples of 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
multiplesOfThree = [num for num in numbers if num % 3 == 0]
print(7, multiplesOfThree)
# Output: [3, 6, 9, 12]

# Example 8: Accepts items that contain the substring "cat"
words = ["catalog", "dog", "caterpillar", "elephant", "cat"]
catWords = [word for word in words if "cat" in word]
print(8, catWords)
# Output: ['catalog', 'caterpillar', 'cat']