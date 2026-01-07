class MathOperations:
    def __init__(self, num):
        self.num = num

    # Instance Method (Needs self to access self.num)
    def add_to_num(self, n):
        self.num = self.num + n
        return self.num

    # Static Method (Just a utility function, no self needed)
    @staticmethod
    def add(a, b):
        return a + b

# --- Using the class ---

# 1. Calling static method  (No object needed)
result1 = MathOperations.add(5, 10)
print(f"Static Method Result: {result1}") 

# 2. Calling instance method (Object is required)
obj = MathOperations(10)
result2 = obj.add_to_num(5)
print(f"Instance Method Result: {result2}") 