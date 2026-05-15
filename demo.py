# python sets, lists, tuples, and dictionaries
# sets
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)   
# lists
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
# tuples
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
# dictionaries
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", my_dict)   
    
# all lambda functions
x = lambda a: a + 10
print("Lambda function result:", x(5))  # Output: 15
# explaining lambda functions
# A lambda function is a small anonymous function that can take any number of arguments, but can
#only have one expression. It is often used for short, simple functions that are not reused elsewhere in the code. The syntax for a lambda function is: lambda arguments: expression
# another lambda function example
y = lambda a, b: a * b
print("Lambda function result:", y(5, 3))  # Output: 15
import math
# math module functions
print("Square root of 16:", math.sqrt(16))  # Output: 40
print("Sine of 90 degrees:", math.sin(math.radians(90)))  # Output: 1.0
print("Cosine of 0 degrees:", math.cos(math.radians(0)))  # Output: 1.0
print("Factorial of 5:", math.factorial(5))  # Output: 120      
# the core concepts of oop
#explain me the below code with each steps
class Person:
    def __init__(self, name, age):
        self.name = name  # This is an instance variable that stores the name of the person
        self.age = age    # This is an instance variable that stores the age of the person

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."  # This method returns a greeting message using the person's name and age
    
# creating an instance of the Person class
person1 = Person("Alice", 30)  # This creates an object of the Person class with the name "Alice" and age 30
print(person1.greet())  # This calls the greet method of the person1 object, which returns a greeting message that is printed to
# now add more functionality to the Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def have_birthday(self):
        self.age += 1  # This method increments the age of the person by 1, simulating a birthday celebration       
    
    # what more thing we can add to the Person class
    def change_name(self, new_name):
        self.name = new_name  # This method allows changing the name of the person to a new name provided as an argument        
# what is encapsulation in oop


# Encapsulation is one of the fundamental principles of object-oriented programming (OOP) that refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, typically a class. It also involves restricting direct access to some of the object's components, which is often achieved through the use of access modifiers (like private, protected, and public)
# In Python, encapsulation is implemented using naming conventions. For example, a single underscore prefix (e.g., _variable) indicates that a variable or method is intended for internal use (protected), while a double underscore prefix (e.g., __variable) makes it name-mangled, which means it cannot be accessed directly from outside the class (private). This helps to protect the internal state of the object and prevents unintended interference from outside code.
# show me an example of encapsulation in python
class BankAccount:  
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private variable to store the account number
        self.__balance = balance  # Private variable to store the account balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Method to deposit money into the account
            return f"Deposited {amount}. New balance is {self.__balance}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount  # Method to withdraw money from the account
            return f"Withdrew {amount}. New balance is {self.__balance}."
        else:
            return "Withdrawal amount must be positive and less than or equal to the current balance."

    def get_balance(self):
        return f"The current balance is {self.__balance}."  # Method to get the current balance of the account      
