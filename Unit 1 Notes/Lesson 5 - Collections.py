# 09/26/23

## Collections

import collections
from pprint import pprint
from functools import reduce

# Collections and Named Tuple

Scientist = collections.namedtuple('Scientist',['name',
                                                'field',
                                                'born',
                                                'nobel'])

# Create tuple called 'scientists'
scientists = (
    Scientist(name = 'Ada Lovelace', field = 'math', born = 1815, nobel = False),
    Scientist(name = 'Emmy Noehter', field = 'math', born = 1882, nobel = False),
    Scientist(name = 'Marie Currie', field = 'physics', born = 1867, nobel = True),
    Scientist(name = 'Tu Youyou', field = 'physics', born = 1930, nobel = True),
    Scientist(name = 'Ada Yonath', field = 'chemistry', born = 1939, nobel = True),
    Scientist(name = 'Vera Rubin', field = 'astronomy', born = 1928, nobel = False),
    Scientist(name = 'Sally Ride', field = 'physics', born = 1951, nobel = False)
)

## Using .filter()

# All scientists with Nobel Prize
nobel = tuple(filter(lambda x : x.nobel is True, scientists))
pprint(nobel)

# Only physics
physics = tuple(filter(lambda x : x.field == 'physics', scientists))
pprint(physics)

# Only math nobel winners
new_nobel = tuple(filter(lambda x : x.field == 'math' and x.nobel is True, scientists))
print(new_nobel)

# Reuse a function
def nobel_filter(x):
    return x.nobel is True

pprint(tuple(filter(nobel_filter, scientists)))

# Use a list comprehension
pprint(tuple(x for x in scientists if x.nobel is True))

## Using .map()

# Create a new dictionary from existing tuple that has output of name and age
name_age = tuple(map(
    lambda x : {'name' : x.name, 'age' : 2023 - x.born}, scientists))

pprint(name_age)

# Use name_age tuple and determine the overall age of the group
age = tuple(reduce(
    lambda x,y : x + y['age'], name_age, 0
))


# Use list comprehension
age1 = sum(x['age'] for x in name_age)
print(age1)

# Another way to use the reduce function -> Group sccientists by field | {'fields': [names]}
def reducer(x,y):
    x[y.field].append(y.name)
    return x

by_field = reduce(reducer,scientists,
                  {'math':[],
                  'physics':[],
                  'chemistry':[],
                  'astronomy':[]
                  })