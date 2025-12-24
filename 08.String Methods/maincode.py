str1 = "AbcDEfghIJ"
print(1, str1.upper())      # Output: "ABCDEFGHIJ" uppercase
print(1, str1.lower())  # Output: "abcdefghij" lowercase   
print(1, str1.capitalize())  # Output: "Abcdefghij" Capitalized


str2 = "    Silver Spoon    "
print(2, str2.strip())  # Output: "Silver Spoon" Stripped of whitespace

str3 = "Hello !!!"
print(3, str3.rstrip("!"))  # Output: "Hello " Stripped of trailing exclamation marks

str4 = "Spaghetti"
print(4, str4.replace("ghetti", "ghetta with meatballs"))  # Output: "Spaghetti with meatballs" Replaced substring

str5 = "Data Science"
print(5, str5.find("Science"))  # Output: 5 Index of substring "Science"

str6 = "Machine Learning"
print(6, str6.index("Learning"))  # Output: 8 Index of substring "Learning"

str7 = "Welcome to the Console!!!"
print(7, str7.center(50,"."))  # Output: Centered string within 50 characters
str7 = "Welcome to the programing"
print(7, str7.center(50))  # Output: Centered string within 50 characters

str8 = "Python Programming"
print(8, str8.count("o"))  # Output: 2 Count of character 'o'

str9 = "Data-Science-Is-Fun"
print(9, str9.split("-"))  # Output: ['Data', 'Science', 'Is', 'Fun'] Split string by delimiter '-'

str10 = "Welcome to the Console !!!"
print(10, str10.endswith("!!!")) # Output: True Check if string ends with "!!!"
str10 = "Welcome to the Console !!!"
print(10, str10.endswith("to",0,10)) # Output: True Check if string ends with "!!!"

str11 = "Hello World"
print(11, str11.startswith("Hello")) # Output: True Check if string starts with "Hello"
str11 = "Hello World"   
print(11, str11.startswith("World",6,11)) # Output: True Check if string starts with "World"

str12 = "WelcomeToTheConsole"
print(12, str12.isalnum()) # Output: True Check if string is alphanumeric
str12 = "WelcomeToTheConsole@2024"
print(12, str12.isalnum()) # Output: True Check if string is alphanumeric

str13 = "WelcomeToTheConsole"
print(13, str13.isalpha()) # Output: True Check if string is alphabetic
str13 = "WelcomeToTheConsole2024"
print(13, str13.isalpha()) # Output: False Check if string is alphabetic

str14 = "1234567890"
print(14, str14.isdigit()) # Output: True Check if string is numeric
str14 = "12345abc67890"
print(14, str14.isdigit()) # Output: False Check if string is numeric

str15 = "   "
print(15, str15.isspace()) # Output: True Check if string contains only whitespace
str15 = "  a "
print(15, str15.isspace()) # Output: False Check if string contains only whitespace

str16 = "hello world"
print(16, str16.islower()) # Output: True Check if all characters are lowercase
str16 = "Hello World"
print(16, str16.islower()) # Output: False Check if all characters are lowercase

str17 = "HELLO WORLD"
print(17, str17.isupper()) # Output: True Check if all characters are uppercase
str17 = "Hello World"
print(17, str17.isupper()) # Output: False Check if all characters are uppercase

str18 = "Title Case Example"
print(18, str18.istitle()) # Output: True Check if string is in title case meaning each word starts with uppercase
str18 = "title case example"
print(18, str18.istitle()) # Output: False Check if string is in title case

str19 = "We wish you a Merry Christmas"
print(19, str1.isprintable()) # Output: True Check if all characters are printable
str19 = "Hello\nWorld"
print(19, str1.isprintable()) # Output: False Check if all characters are printable

str20 = "Python is a Interpreted Language" 
print(20, str20.swapcase()) # Output: meaning uppercase to lowercase and vice versa

str21 = "He's name is Dan. Dan is an honest man."
print(21, str21.title()) # Output: "He'S Name Is Dan. Dan Is An Honest

