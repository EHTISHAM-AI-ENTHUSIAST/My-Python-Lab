# 1. Standard Function (Uses more memory)
def my_list_function(n):
    result = []
    for i in range(n):
        result.append(i)
    return result

# 2. Generator Function (Uses almost ZERO memory)
def my_generator(n):
    for i in range(n):
        yield i

# --- Using the Generator ---
gen = my_generator(1000) # this will not consume much memory

# to get Values two ways:
# A. one by one (Using next)
print(next(gen)) # Output: 0
print(next(gen)) # Output: 1

# B. with loop (Iterating through all values)
for value in gen:
    print(value)