# 09/19/23

# Three Common Classes in Functional Programming for all languages: Filter, Map, Reduce

# Basic Functional Program
def add(x,y):
    return x + y

def mult(x,y):
    return x * y

def do_math(action,x,y):
    return action(x,y)  # First parameter is the name of a function

# Way we know:
print(add(3,4))  # = 7
print(mult(3,4))  # = 12

# Run functions within another function
print(do_math(add,3,4))  # = 7
print(do_math(mult,3,4))  # = 12

# Standard vs Lambda (inline) Functions
## Lambda: single-use purposes, defined in single line
people = [('Steve',35),  # List of tuples
        ('Karen',58),
        ('Gerald',58),
        ('Jo',72)]  

people.sort()  # Sort by alpha (non-destructive)
print(people)

# Sort by second element (age)
people.sort(key = lambda x: x[1])  # Declare variable for lambda function; Call inline function; x is EACH element in list; Return the elements in x with index 1
print(people)

# .sort() params
## .sort(key = None, reverse = False) -> default

nums = [6,2,8]

# Square a number
squared = lambda x: x * x
print(squared(3))

# Add two numbers
sum = lambda x,y: x + y
print(sum(6,2))

# Multiply three numbers
prod = lambda x,y,z: x * y * z
print(prod(6,2,8))

# Add 10 to any number
add_ten = lambda x: x + 10
print(add_ten(6))