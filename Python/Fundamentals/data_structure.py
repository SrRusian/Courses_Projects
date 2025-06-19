# --- LISTS ---

fruits = ["apple", "banana", "orange"]

print(fruits[0])  # Prints "apple"
print(fruits[1])  # Prints "banana"
print(fruits[2])  # Prints "orange"

# Negative indexing
print(fruits[-1])  # Prints "orange"
print(fruits[-2])  # Prints "banana"
print(fruits[-3])  # Prints "apple"

# Append and insert
fruits.append("pear")
print(fruits)  # ["apple", "banana", "orange", "pear"]

fruits.insert(1, "grape")
print(fruits)  # ["apple", "grape", "banana", "orange", "pear"]

# Remove and pop
fruits.remove("banana")
print(fruits)  # ["apple", "grape", "orange", "pear"]

removed_fruit = fruits.pop(2)
print(fruits)         # ["apple", "grape", "pear"]
print(removed_fruit)  # "orange"

# Sorting and reversing
fruits.sort()
print(fruits)  # ["apple", "grape", "pear"]

fruits.reverse()
print(fruits)  # ["pear", "grape", "apple"]

# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers if x % 2 == 0]
print(squares)  # [4, 16]


# --- TUPLES ---

point = (3, 4)
print(point[0])  # 3
print(point[1])  # 4

my_tuple = (1, 2, 3, 2, 4, 2)
print(my_tuple.index(2))          # 1
print(my_tuple.index(2, 2))       # 3
print(my_tuple.index(2, 2, 4))    # 3


# --- DICTIONARIES ---

person = {
    "name": "John",
    "age": 25,
    "city": "Madrid"
}

print(person["name"])   # John
print(person["age"])    # 25
print(person["city"])   # Madrid

print(person.keys())    # dict_keys(["name", "age", "city"])
print(person.values())  # dict_values(["John", 25, "Madrid"])
print(person.items())   # dict_items([("name", "John"), ("age", 25), ("city", "Madrid")])

person.update({"profession": "Engineer"})
print(person)  # {"name": "John", "age": 25, "city": "Madrid", "profession": "Engineer"}


# --- SETS ---

fruits = {"apple", "banana", "orange"}
numbers = set([1, 2, 3, 4, 5])

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2
print(union)  # {1, 2, 3, 4, 5}

intersection = set1 & set2
print(intersection)  # {3}

difference = set1 - set2
print(difference)  # {1, 2}

symmetric_difference = set1 ^ set2
print(symmetric_difference)  # {1, 2, 4, 5}

# Set modification
fruits.add("pear")
print(fruits)  # {"apple", "banana", "orange", "pear"}

fruits.remove("banana")
print(fruits)  # {"apple", "orange", "pear"}

fruits.discard("grape")  # No error if item is not present
print(fruits)  # {"apple", "orange", "pear"}

fruits.clear()
print(fruits)  # set()
