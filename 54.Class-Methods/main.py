class Employee:
    company = "Apple"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    # This is a Class Method
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

# --- Using the Class ---

e1 = Employee()
e1.name = "Ali"
e1.show() # Output: Company is Apple

# Changing company using Class Method
e1.changeCompany("Tesla") 
e1.show() # Output: Company is Tesla

# Checking another employee
e2 = Employee()
e2.name = "Ahmed"
e2.show() # Output: Company is Tesla (Sab ke liye change ho gaya!)