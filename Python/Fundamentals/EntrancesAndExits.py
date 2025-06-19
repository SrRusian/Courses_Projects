# --- USER INPUT AND CONDITIONALS ---

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello, " + name + "!")
print("You are " + age + " years old.")

# Convert age to integer for comparison
age = int(age)
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# --- FORMATTED STRING OUTPUT ---

name = "John"
age = 25
print(f"Hello, my name is {name} and I am {age} years old.")


# --- FILE READING AND WRITING ---

# Reading from a file (basic)
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Writing to a file (overwrites existing content)
file = open("data.txt", "w")
file.write("Hello, world!")
file.close()

# Reading from a file using context manager (preferred way)
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
