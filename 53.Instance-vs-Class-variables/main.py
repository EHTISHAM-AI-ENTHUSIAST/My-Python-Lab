class Employee:
    companyName = "Apple"  # Class Variable (Shared by all)
    noOfEmployees = 0      # Class Variable

    def __init__(self, name):
        self.name = name          # Instance Variable (Unique for each)
        self.raise_amount = 0.02  # Instance Variable
        Employee.noOfEmployees += 1 # Accessing Class variable

    def showDetails(self):
        print(f"Name: {self.name}, Raise: {self.raise_amount}, Company: {self.companyName}")

# --- Using the Class ---

emp1 = Employee("Ali")
emp1.raise_amount = 0.05 #  emp1  raise change 
emp1.showDetails()

emp2 = Employee("Ahmed")
emp2.showDetails() #  raise default (0.02) 

# Changing Class Variable for everyone
Employee.companyName = "Google"

emp1.showDetails() #  company name "Google" for both
emp2.showDetails()

print(f"Total Employees: {Employee.noOfEmployees}")