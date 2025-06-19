# --- BASIC FUNCTIONS ---

def greeting():
    print("Hello, world!")

greeting()  # Prints "Hello, world!"


def greeting(name):
    print(f"Hello, {name}!")

greeting("John")   # Prints "Hello, John!"
greeting("Mary")   # Prints "Hello, Mary!"


def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Prints 7


# --- LAMBDA FUNCTIONS ---

square = lambda x: x ** 2
print(square(5))  # Prints 25


# --- VARIABLE SCOPE ---

def function_with_local():
    local_variable = 10
    print(local_variable)  # Accessible only inside the function

global_variable = 20

def function_with_global():
    print(global_variable)  # Accessible from anywhere

function_with_local()   # Prints 10
function_with_global()  # Prints 20
print(global_variable)  # Prints 20

# print(local_variable)  # Would raise an error: local_variable is not defined here


# --- FUNCTION WITH DOCSTRING ---

def rectangle_area(base, height):
    """
    Calculates the area of a rectangle.

    Args:
        base (float): The base of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return base * height

print(rectangle_area(5, 10))  # Prints 50


# --- VARIABLE NUMBER OF ARGUMENTS ---

def variable_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(variable_sum(1, 2, 3))        # Prints 6
print(variable_sum(4, 5, 6, 7))     # Prints 22
