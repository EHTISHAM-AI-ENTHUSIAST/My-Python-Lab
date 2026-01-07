# def double(x):
#   return x*2




double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))


#defining a function that takes another function as argument
def test (fx, value):
  return 6 +fx(value)
#first way
print(test(cube, 5))
#second way
print(test(lambda x: x * x * x, 5))