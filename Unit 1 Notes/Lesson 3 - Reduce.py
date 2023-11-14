# 09/22/23

# Using lambda and Reduce

from functools import reduce  # from <module> import <function>

nums = list(range(1,11))  # Create list of numbers from 1 to 10, inclusive

# Summing all values of nums
total = reduce(lambda x, y : x + y, nums)  # x refers to initial element, y refers to second element, returns value of first + second element
# x is always the next term in the seqeunce
# y is always the previously returned term
print(total)

# Adds first two letters of each person's name
names = ['Josh','Katie','Darrne','Joanna','Jackie','Chris','Isaac']
# Note: First name will be entire name
# OUTPUT: JoshKaDaJoJaChIs
conc_1 =  reduce(lambda x, y : x + y[0:2], names)
print(conc_1)

# NOTICE: 1st term is unaffected
## Pass an optional parameter for x-value

conc_2 =  reduce(lambda x, y : x + y[0:2], names, '')  # Pass an empty third parameter
print(conc_2)

