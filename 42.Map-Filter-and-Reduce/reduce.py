from functools import reduce

numbers = [1, 2, 3, 4, 5]

def mysum(x, y):
    return x + y

sum_val = reduce(mysum, numbers)
print(sum_val) 