letter = "my name is {} and I am from {}"
country = "pakistan"
name = "ali"

print(letter.format(name, country))
print(f"my name is {name} and I am from {country}")


txt = "For only {price} dollars!"
print(txt.format(price = 49.9999))
print(f"For only {49.9999:.2f} dollars!")
print(type(f"{3 * 40}"))