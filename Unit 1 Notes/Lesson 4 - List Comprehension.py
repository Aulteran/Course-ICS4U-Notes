# 09/25/23

## List Comprehensions - the "pythonic" way to filter, map, and reduce
# Create a NEW list within (or from) an existing list
# Syntax: <expression> for item in list:

## If we're using for loops
# Step 1: define an empty list
squares = []

# Step 2: use for loop
for i in range(10):
    # Step 3: append to list
    squares.append(i * i)

print(squares)

## Same result using list comprehension
# new_list = <expression for member in iterable>
squares2 = [i * i for i in range(10)]  # expressin is i * i; individual member is i; range(10) is iterable
print(squares2)

## Conditional Logic
# new_list = [expression for member initerable (if condition)]
sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']  # Replacing .filter()
print(vowels)

## Place condition in return
# new_list = [expression (if condition) for member in iterable]
# GOAL: change -ve prices to 0 and leave +ve prices unchanged
prices = [-1.25,-9.4,8.6,1.3,-0.4]
new_prices = [i if i > 0 else 0 for i in prices]  # Replacing .map(); return i (if condition) (else return y) for i in iterable
print(new_prices)