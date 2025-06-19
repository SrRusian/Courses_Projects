# --- IMPORTING MODULES ---

# Importing the entire math module
import math
result = math.sqrt(25)
print(result)  # Prints 5.0

# Importing specific function from a module
from math import sqrt
result = sqrt(25)
print(result)  # Prints 5.0

# Using additional standard modules
import random
import datetime

random_number = random.randint(1, 10)
print(random_number)  # Prints a random integer between 1 and 10

current_datetime = datetime.datetime.now()
print(current_datetime)  # Prints current date and time


# --- CUSTOM MODULES ---

# Example content of my_module.py
def greet(name):
    print(f"Hello, {name}!")

def calculate_sum(a, b):
    return a + b

"""
# Usage example (assuming my_module.py is available in the same directory)
import my_module

my_module.greet("John")             # Prints "Hello, John!"
result = my_module.calculate_sum(5, 3)
print(result)                       # Prints 8
"""


# --- ORGANIZING CODE INTO MODULES ---

# Example content of operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# Example content of utilities.py
def print_message(message):
    print(message)

def get_username():
    return input("Enter your name: ")

"""
# Usage example
import operations
import utilities

result = operations.add(5, 3)
utilities.print_message(f"The result of the addition is: {result}")

username = utilities.get_username()
utilities.print_message(f"Hello, {username}!")
"""


# --- CREATING AND USING PACKAGES ---

"""
# Example package structure:

  my_package/
    __init__.py
    module1.py
    module2.py

# Using modules from a package
from my_package import module1, module2

module1.function1()
module2.function2()
"""
