class Employee:
    def __init__(self, name):
        self.name = name

    # 1. String representation for users
    def __str__(self):
        return f"Employee Name: {self.name}"

    # 2. String representation for developers (fallback)
    def __repr__(self):
        return f"Employee('{self.name}')"

    # 3. Custom length (e.g., length of the name)
    def __len__(self):
        return len(self.name)

    # 4. Making the object callable like a function
    def __call__(self):
        print(f"Hey, {self.name} is being called!")

# --- Using the Magic ---
e = Employee("ehtisham")

print(e)        # Automatically calls __str__
print(str(e))   # Explicitly calls __str__
print(repr(e))  # Explicitly calls __repr__
print(len(e))   # Calls __len__
e()             # Calls __call__