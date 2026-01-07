class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    # OPERATOR OVERLOADING for '+'
    def __add__(self, x):
        # 'self' is v1, 'x' is v2
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)

# --- Using the overloaded operator ---
v1 = Vector(3, 5, 6)
print(f"Vector 1: {v1}")

v2 = Vector(1, 2, 9)
print(f"Vector 2: {v2}")

# This '+' now calls the __add__ method we wrote
v3 = v1 + v2
print(f"Result (v1 + v2): {v3}")
print(type(v3)) # It's still a Vector object!