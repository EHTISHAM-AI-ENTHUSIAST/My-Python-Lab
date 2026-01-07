#making Decorator Function

def my_decorator(fx):
    def wrapper():
        print("Slam/Hello! Function is now starting.")
        fx() # real function call
        print("good bye! Function is finished.\n")
    return wrapper

@my_decorator
def hello():
    print("Hello World!")

@my_decorator
def add():                                                                                                                                                                                                                                                                                   
    print(5 + 5)

# now calling these functions
hello()
add()



# If the Function Has Arguments  
# then to prevent the decorator from failing, 
# we use *args and **kwargs.

def greet(fx):
    def mfx(*args, **kwargs):
        print("work is starting...")
        result = fx(*args, **kwargs)
        print("work finished!")
        return result
    return mfx

@greet
def sum_numbers(a, b):
    print(f"The sum is: {a + b}")

sum_numbers(10, 20)