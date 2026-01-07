# WRITING TO A FILE
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")

# READING A FILE
with open('example.txt', 'r') as filee:
    content = filee.read()
    print(content)

# APPENDING TO A FILE
with open('example.txt', 'a') as file:
    file.write("Appending a new line.\n")

# READING THE UPDATED FILE
with open('example.txt', 'r') as filee:
    updated_content = filee.read()
    print(updated_content)