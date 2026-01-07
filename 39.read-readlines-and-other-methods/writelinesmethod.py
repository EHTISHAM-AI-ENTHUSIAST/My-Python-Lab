#writelines() Method
#The writelines() method writes a list of strings to a file.
#It does not add newline characters automatically, so you need to include them if required.

lines = ['Line 1\n', 'this is Line 2\n', 'Line 3\n']
with open('myfile2.txt', 'w') as f:
    f.writelines(lines)

#now we are going to read the file to verify the contents
f = open('myfile2.txt', 'r')
content = f.read()
print(content)
f.close()
