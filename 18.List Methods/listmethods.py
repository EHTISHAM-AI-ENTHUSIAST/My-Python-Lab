#list methods in Python

#example 1 sorting a list
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(1, colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(2, num)

# example 2 reversing a list What if you want to print the list in descending order?
# We must give reverse=True as a parameter in the sort method.

colors.reverse()
print(3, colors)
num.sort(reverse=True)
print(4, num)

# example 3 finding the index of an element in a list
fruits = ["apple", "banana", "cherry", "date"]
index = fruits.index("cherry")
print(5, index)  # Output: 2
index = fruits.index("date")
print(6, index)  # Output: 3

# example 4 counting occurrences of an element in a list
letters = ["a", "b", "c", "a", "b", "a"]
count_a = letters.count("a")
print(7, count_a)  # Output: 3
count_b = letters.count("b")
print(8, count_b)  # Output: 2


# example 5 copying a list
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print(9, copied_list)  # Output: [1, 2, 3, 4, 5]

# example 6 clearing a list
my_list = [10, 20, 30, 40]
my_list.clear()
print(10, my_list)  # Output: []

# example 7 appending elements to a list
my_list = [1, 2, 3]
my_list.append(4)
print(11, my_list)  # Output: [1, 2, 3, 4]

# example 8 inserting elements at a specific position
my_list.insert(1, 1.5)
print(12, my_list)  # Output: [1, 1.5, 2, 3, 4]

# example 9 extending a list with another list
another_list = [5, 6, 7]
my_list.extend(another_list)
print(13, my_list)  # Output: [1, 1.5, 2, 3, 4, 5, 6, 7]

# example 10 removing an element from a list
my_list.remove(1.5)
print(14, my_list)  # Output: [1, 2, 3, 4, 5, 6, 7]
my_list.remove(7)
print(15, my_list)  # Output: [1, 2, 3, 4, 5, 6]

# example 11 concatenating two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(16, combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# example 12 repeating a list
repeated_list = list1 * 3
print(17, repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]



