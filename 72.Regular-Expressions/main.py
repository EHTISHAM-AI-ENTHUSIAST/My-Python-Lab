import re  # 1. Import the RegEx module

# Our text (from which we want to extract emails)
text = """
Hello, my name is Ali and my email is ali@gmail.com
Please contact support at info@yahoo.com for help.
Do not email fake@website
.com or test@.com as they are invalid.
Thank you!
"""

# 2. Create the formula (pattern)
# [a-z]+  --> Means: consecutive lowercase letters (like 'ali')
# @       --> Means: '@' must appear in the middle
# [a-z]+  --> Means: consecutive letters (like 'gmail')
# \.      --> Means: a dot (.) must appear
# [a-z]+  --> Means: letters (like 'com')

pattern = r"[a-z]+@[a-z]+\.[a-z]+"

# 3. Magic function: re.findall()
# This function will extract all emails from the text and store them in a list
emails = re.findall(pattern, text)

print(emails)
