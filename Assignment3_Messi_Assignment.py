'''
Author: Aadil Hussain
Built on: Python 3.10.11
'''

# Messi Assignment Instructions:
# You have been asked to create a new list from an existing set of Data on Lionel Messi. 
# Please view the start code below to create answers to the following question(s). 

# In each instance, create a new tuple that stores the following data.
    # The years Messi scored over 35 goals
    # The years Messi had over 11 assists
    # The total number of goals Messi scored over the course of his career (NOT TUPLE)
    # The total number of points (goals and assists) Messi scored over his career (NOT TUPLE)
    # Return a T/F tuple of whether Messi scored more than 50 pts, then have a print statement counting how many times this occurred
    # How many years did Messi score over 30 goals, what was the overall total number of goals during ONLY THOSE YEARS.

import collections
from pprint import pprint
from functools import reduce

# Messi Starter Code

Messi = collections.namedtuple('Messi',['year','gls','asts'])

player = (
Messi('2004-2005',1,0),
Messi('2005-2006',6,3),
Messi('2006-2007',14,3),
Messi('2007-2008',10,12),
Messi('2008-2009',23,11),
Messi('2009-2010',34,9),
Messi('2010-2011',31,19),
Messi('2011-2012',50,16),
Messi('2012-2013',46,11),
Messi('2013-2014',28,11),
Messi('2014-2015',43,18),
Messi('2015-2016',26,16),
Messi('2016-2017',37,9),
Messi('2017-2018',34,12),
Messi('2018-2019',36,13),
Messi('2019-2020',25,21),
Messi('2020-2021',30,9),
Messi('2021-2022',2,10)
)

# The years Messi scored over 35 goals
goals_over_35 = list(filter(lambda x: x.gls > 35, player))

# The years Messi had over 11 assists
assists_over_11 = list(filter(lambda x: x.asts > 11, player))

# The total number of goals Messi scored over the course of his career
total_goals = reduce(lambda x, y: x + y.gls, player, 0)

# The total number of points (goals and assists) Messi scored over his career
total_points = reduce(lambda x, y: x + y.gls + y.asts, player, 0)

# Return a T/F tuple of whether Messi scored more than 50 pts, then have a print statement counting how many times this occurred
more_than_50_pts = list(map(lambda x: x.gls + x.asts > 50, player))
count_more_than_50_pts = more_than_50_pts.count(True)

# How many years did Messi score over 30 goals, what was the overall total number of goals during ONLY THOSE YEARS.
goals_over_30 = list(filter(lambda x: x.gls > 30, player))
total_goals_over_30 = reduce(lambda x, y: x + y.gls, goals_over_30, 0)

# Printing the results
print("Years Messi scored over 35 goals:")
pprint(goals_over_35)

print("\nYears Messi had over 11 assists:")
pprint(assists_over_11)

print("\nTotal number of goals Messi scored over his career:", total_goals)
print("Total number of points Messi scored over his career:", total_points)

print("\nMessi scored more than 50 points in", count_more_than_50_pts, "years.")

print("\nYears Messi scored over 30 goals:", len(goals_over_30))
print("Overall total number of goals during those years:", total_goals_over_30)
