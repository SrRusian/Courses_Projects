# --- CONDITIONAL STATEMENTS ---

age = 18
grade = 85

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

if grade >= 90:
    print("Excellent")
elif grade >= 80:
    print("Very good")
elif grade >= 70:
    print("Good")
else:
    print("Needs improvement")


# --- LOOPS ---

fruits = ["apple", "banana", "orange"]
counter = 0

# For loop
for fruit in fruits:
    print(fruit)

# While loop
while counter < 5:
    print(counter)
    counter += 1


# --- CONTROLLED LOOPS ---

# Infinite loop with break
counter = 0
while True:
    print(counter)
    counter += 1
    if counter == 5:
        break

# Continue statement: skips even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Pass statement: placeholder for future code
for i in range(5):
    pass
