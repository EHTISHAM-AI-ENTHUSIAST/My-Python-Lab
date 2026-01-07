# we will learn about seek function in file handling
# seek() function is used to change the file object's position
# The syntax of seek() function is:
# file_object.seek(offset, whence)
# where,
# offset: This is the number of bytes to be moved.
# whence: This is optional and defaults to 0. It indicates from where the offset is to be added.
# whence can take the following values:
# 0: Beginning of the file
# 1: Current file position
# 2: End of the file
# Let's see an example of seek() function
# Open a file in read mode


with open('seekexample.txt', 'r') as file:
    file.seek(8)
    data = file.read(5)
    print(data)  


#now we will see another example of tell function which returns the current position of the file object

with open('seekexample.txt', 'r') as f:
    f.read(11) 
    print(f.tell()) 
    f.seek(12)  
    print(f.tell())