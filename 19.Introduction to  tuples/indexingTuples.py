#Tuple Indexes


#example 1 
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]

#Accessing tuple items

#I. Positive Indexing:

print(country[0])  #Output: Spain
print(country[1])  #Output: Italy
print(country[2])  #Output: India

#II. Negative Indexing:
print(country[-1])  #Similar to print(country[len(country) - 1])#Output: India
print(country[-2])  #Output: Italy
print(country[-3])  #Output: Spain

#III. Check for item:

if "Italy" in country:
    print("Italy is present in the tuple")  
else:
    print("Italy is not present in the tuple") #Output: Italy is present in the tuple

if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")  #Output: Russia is absent.


#IV. Range of Index: Tuple syntax [start : end : jumpIndex]

print(country[1:4])  #Output: ('Italy', 'India', 'England')

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes
#Output: ('cat', 'bat', 'pig', 'donkey', 'cow')



