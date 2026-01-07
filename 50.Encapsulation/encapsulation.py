# here we learn about encapsulation in python
# Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP).
# It refers to the bundling of data (attributes) and methods (functions) that operate
# on that data into a single unit, typically a class.
# Encapsulation helps to restrict direct access to some of an object's components,
# which can prevent the accidental modification of data. It also helps to
# maintain a clear interface for interacting with an object.
# In Python, encapsulation is implemented using access specifiers:
# 1. Public: Attributes and methods that are accessible from outside the class.
# 2. Protected: Attributes and methods that are intended to be accessed only within
# the class and its subclasses.
# 3. Private: Attributes and methods that are intended to be accessed only within
# the class itself.


class BankAccount:
    def __init__(self, name, balance):
        self.name = name  # public
        self.__balance = balance  # private - data mangling

    def get_balance(self):  # getter
        return self.__balance

    def set_balance(self, newbalance):  # setter
        self.__balance = newbalance


acc1 = BankAccount("EHtisham", 10_000)

acc1.set_balance(200_000)

print(acc1.name, acc1.get_balance())

# another way to access private variable is=

print(acc1.name, acc1._BankAccount__balance)
