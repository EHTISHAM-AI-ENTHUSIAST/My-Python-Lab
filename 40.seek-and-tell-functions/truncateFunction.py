#truncate() Function tells Python to remove all characters from a string after a certain length.

with open('sample.txt', 'w') as f:
    f.write('Hello World')
    f.truncate(5) # File is truncated to 5 characters

with open('sample.txt', 'r') as f:
    print(f.read()) # Output: Hello