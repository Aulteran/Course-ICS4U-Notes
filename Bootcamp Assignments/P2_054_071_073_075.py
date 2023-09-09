'''
Author: Aadil Hussain
Built on: Python 3.10.8
'''
import random

# For Homework to complete for tomrrow:
# Bootcamp P2: 054,071,073,075

# 054
user_sel = input("pick heads or tails[H or T]: ").lower()
if user_sel == random.choice(["h", "t"]):
    print("You win!")
else:
    print(f"Sorry you lose! The computer chose {random.choice(['heads', 'tails'])}")

# 071
sports = ["baseball", "basketball"]
sports.append(input("what is your fav sport?: ").lower())
sports.sort(); print(sports)

# 073
fav_foods = {}
for i in range(3):
    fav_foods[i] = input(f"enter favorite food {i}: ")
print(fav_foods)
fav_foods.pop(input("which number do you want to remove?: "))
print(fav_foods)

# 075
rand_nums = []
for i in range(3):
    rand_nums.append(random.randint(100, 999))
for item in rand_nums:
    print(item)
try:
    rand_nums.index(int(input("enter a three-digit number")))
except ValueError:
    print("That is not on the list")
