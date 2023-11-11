'''
Author: Aadil Hussain
Built on: Python 3.10.11
'''

# You have been asked to create a program which allows head NBA scouts to quickly and 
# efficiently sort through data on any given player in the NBA. The scout has asked that you
# use Lebron James from the Los Angeles Lakers as your test subject.

# Lebron has had a successful career as an NBA superstar, and played for a number of teams while 
# in the NBA. As such, there is a considerable amount of data to course through – and scouts DON’T want 
# to have to do this. You will find Lebron’s regular season data on the following page.
# Please create a program using a functional framework that allows the head scouts to determine
# key statistics of players.

# WHAT DO THE SCOUTS WANT TO KNOW IN THE PROGRAM?? (IN EACH INSTANCE CREATE A NEW DATA STRUCTURE TO DISPLAY INFORMATION
    # 1) Which years did Lebron average more than 28 ppg
    # 2) Which years was Lebron’s field goal percentage over .500 
    # 3) When Lebron played for Cleveland, what years was his free throw (FT) percentage over .720
    # 4) When Lebron played for Miami (MIA) , what was his average field goal percentage (FG)
    # 5) What is the TOTAL number of games (G) Lebron has played in his career
    # 6) A regular season has 82 games – how many games did he miss each season? (season, number of games missed)
    # 7) What percent of games did Lebron start in comparison to games played?
    # 8) How many years has Lebron played in the NBA?
    # 9) Which position (POS) was Lebron’s Assists per game average (AST) highest? (PG,SG,SF,PF)

# PLAYOFF LEBRON VS. REG. SEASON LEBRON (Hint: you might want to add an additional column stat to the reg season tuple)
    # 1) What is the total number of games (G) Lebron has played in the playoffs?
    # 2) What is Lebron’s average FG attempts per game in the playoffs?
    # 3) IN THE SEASONS WHICH LEBRON MADE THE PLAYOFFS ONLY: was his average FG% higher in the regular season or the playoffs?
    # 4) IN THE SEASONS WHICH LEBRON MADE THE PLAYOFFS ONLY: create a new data set comparing minutes played in regular season vs. playoffs (per season)
    # 5) IN THE SEASONS WHICH LEBRON MADE THE PLAYOFFS ONLY: what season was his FG% above .500 in BOTH the regular season AND playoffs.

# Make the results look pretty for the scouts by using pprint – Also – if you want, for relevant answers you can also print a summary statement (ie. Q 9 – you should show 
# the data structures grouped by POS – have a final statement after stating – Lebron’s assists per game average was highest as a POS

import collections
import csv
from functools import reduce
from pprint import pprint
from statistics import mean

Lebron = collections.namedtuple('Lebron',['Season','Age','Team','Lg','Pos','G','GS','MP','FG','FGA','FG_per','three_P','three_PA','three_P_per','two_P','two_PA','two_P_per',
'eFG_per','FT','FTA','FT_per','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS'])

lebron_data = (
    Lebron('2003-04',19,'CLE','NBA','SG',79,79,39.5,7.9,18.9,.417,0.8,2.7,.290,7.1,16.1,.438,.438,4.4,5.8,.754,1.3,4.2,5.5,5.9,1.6,0.7,3.5,1.9,20.9),
    Lebron('2004-05',20,'CLE','NBA','SF',80,80,42.4,9.9,21.1,.472,1.4,3.9,.351,8.6,17.2,.499,.504,6.0,8.0,.750,1.4,6.0,7.4,7.2,2.2,0.7,3.3,1.8,27.2),
    Lebron('2005-06',21,'CLE','NBA','SF',79,79,42.5,11.1,23.1,.480,1.6,4.8,.335,9.5,18.3,.518,.515,7.6,10.3,.738,0.9,6.1,7.0,6.6,1.6,0.8,3.3,2.3,31.4),
    Lebron('2006-07',22,'CLE','NBA','SF',78,78,40.9,9.9,20.8,.476,1.3,4.0,.319,8.6,16.8,.513,.507,6.3,9.0,.698,1.1,5.7,6.7,6.0,1.6,0.7,3.2,2.2,27.3),
    Lebron('2007-08',23,'CLE','NBA','SF',75,74,40.4,10.6,21.9,.484,1.5,4.8,.315,9.1,17.1,.531,.518,7.3,10.3,.712,1.8,6.1,7.9,7.2,1.8,1.1,3.4,2.2,30.0),
    Lebron('2008-09',24,'CLE','NBA','SF',81,81,37.7,9.7,19.9,.489,1.6,4.7,.344,8.1,15.2,.535,.530,7.3,9.4,.780,1.3,6.3,7.6,7.2,1.7,1.1,3.0,1.7,28.4),
    Lebron('2009-10',25,'CLE','NBA','SF',76,76,39.0,10.1,20.1,.503,1.7,5.1,.333,8.4,15.0,.560,.545,7.8,10.2,.767,0.9,6.4,7.3,8.6,1.6,1.0,3.4,1.6,29.7),
    Lebron('2010-11',26,'MIA','NBA','SF',79,79,38.8,9.6,18.8,.510,1.2,3.5,.330,8.4,15.3,.552,.541,6.4,8.4,.759,1.0,6.5,7.5,7.0,1.6,0.6,3.6,2.1,26.7),
    Lebron('2011-12',27,'MIA','NBA','SF',62,62,37.5,10.0,18.9,.531,0.9,2.4,.362,9.1,16.5,.556,.554,6.2,8.1,.771,1.5,6.4,7.9,6.2,1.9,0.8,3.4,1.5,27.1),
    Lebron('2012-13',28,'MIA','NBA','PF',76,76,37.9,10.1,17.8,.565,1.4,3.3,.406,8.7,14.5,.602,.603,5.3,7.0,.753,1.3,6.8,8.0,7.3,1.7,0.9,3.0,1.4,26.8),
    Lebron('2013-14',29,'MIA','NBA','PF',77,77,37.7,10.0,17.6,.567,1.5,4.0,.379,8.5,13.6,.622,.610,5.7,7.6,.750,1.1,5.9,6.9,6.3,1.6,0.3,3.5,1.6,27.1),
    Lebron('2014-15',30,'CLE','NBA','SF',69,69,36.1,9.0,18.5,.488,1.7,4.9,.354,7.3,13.6,.536,.535,5.4,7.7,.710,0.7,5.3,6.0,7.4,1.6,0.7,3.9,2.0,25.3),
    Lebron('2015-16',31,'CLE','NBA','SF',76,76,35.6,9.7,18.6,.520,1.1,3.7,.309,8.6,14.9,.573,.551,4.7,6.5,.731,1.5,6.0,7.4,6.8,1.4,0.6,3.3,1.9,25.3),
    Lebron('2016-17',32,'CLE','NBA','SF',74,74,37.8,9.9,18.2,.548,1.7,4.6,.363,8.3,13.5,.611,.594,4.8,7.2,.674,1.3,7.3,8.6,8.7,1.2,0.6,4.1,1.8,26.4),
    Lebron('2017-18',33,'CLE','NBA','PF',82,82,36.9,10.5,19.3,.542,1.8,5.0,.367,8.6,14.3,.603,.590,4.7,6.5,.731,1.2,7.5,8.6,9.1,1.4,0.9,4.2,1.7,27.5),
    Lebron('2018-19',34,'LAL','NBA','SF',55,55,35.2,10.1,19.9,.510,2.0,5.9,.339,8.1,14.0,.582,.560,5.1,7.6,.665,1.0,7.4,8.5,8.3,1.3,0.6,3.6,1.7,27.4),
    Lebron('2019-20',35,'LAL','NBA','PG',67,67,34.6,9.6,19.4,.493,2.2,6.3,.348,7.4,13.1,.564,.550,3.9,5.7,.693,1.0,6.9,7.8,10.2,1.2,0.5,3.9,1.8,25.3),
    Lebron('2020-21',36,'LAL','NBA','PG',43,43,33.7,9.3,18.1,.513,2.3,6.4,.366,7.0,11.7,.594,.578,4.1,5.8,.701,0.6,7.3,7.9,7.8,1.0,0.6,3.8,1.6,25.0)
)

# Question 1
print("\n\nWhich years did Lebron average more than 28 ppg")
pprint(list(filter(lambda season: season.PTS > 28, lebron_data)))

# Question 2
print("\n\nWhich years was Lebron's field goal percentage over .500 ")
pprint(list(filter(lambda season: season.FG_per > .500, lebron_data)))

# Question 3
print("\n\nWhen Lebron played for Cleveland, what years was his free throw percentage (FT_per) over .720")
pprint(list(filter(lambda season: season.Team == 'CLE' and season.FT_per > .720, lebron_data)))

# Question 4
print("\n\nWhen Lebron played for Miami (MIA) , what was his average field goal percentage (FG_per)")
mia_seasons = filter(lambda season: season.Team == 'MIA', lebron_data)
mia_fg_percentages = list(map(lambda season: season.FG_per, mia_seasons)) #FG_per is index 10
pprint(mean(mia_fg_percentages))

# Question 5
print("\n\nWhat is the TOTAL number of games (G) Lebron has played in his career")
total_games = reduce(lambda acc, season: acc + season.G, lebron_data, 0)
print(total_games)

# Question 6
print("\n\nA regular season has 82 games - how many games did he miss each season? (season, number of games missed)")
missed_games_per_season = list(map(lambda season: (season.Season, 82 - season.G), lebron_data))
pprint(missed_games_per_season)

# Question 7
print("\n\nWhat percent of games did Lebron start in comparison to games played?")
total_games_started = reduce(lambda acc, season: acc + season.GS, lebron_data, 0)
start_percentage = total_games_started/total_games*100
# can also use: reduce(lambda acc, season: acc + season[6] / season[5], lebron_data, 0) / len(lebron_data) * 100
print(f"LeBron started {start_percentage:.2f}% of the games.")

# Question 8
print("\n\nHow many years has Lebron played in the NBA?")
years_played = len(set(map(lambda season: season.Season[:4], lebron_data)))
print(f"LeBron has played in the NBA for {years_played} years.")

# Question 9
print("\n\nWhich position (POS) was Lebron's Assists per game average (AST) highest? (PG,SG,SF,PF)")
positions = {'PG': [], 'SG': [], 'SF': [], 'PF': []}
for season in lebron_data:
    positions[season.Pos].append(season.AST)
# i wrote this at 2am ik i couldve done this an easier way
max_pos = 'PG'
for position in positions:
    pos_val = positions[position]
    if pos_val > positions[max_pos]:
        for key in positions.keys():
            if positions[key] == position:
                max_pos = key
print(f"{max_pos} has highest AST")
pprint(positions)

# PLAYOFF vs. REG QUESTIONS

PLAYOFF_DATA_FILEPATH = "Assignment4_Playoff_Data.csv"
# playoff data formatted as such:
# ['Season,Age,Tm,Lg,Pos,G,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,eFG%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS']
with open(PLAYOFF_DATA_FILEPATH, 'r') as opened_playoff_data:
    raw_csv_playoff_data = (csv.reader(opened_playoff_data))
    next(raw_csv_playoff_data) #skip header line
    # should i convert csv list data into Lebron collection
    # idk i'll do it anyways just in case
    playoff_data = [Lebron(*row) for row in raw_csv_playoff_data]
    # failed 2AM attempt:
    # playoff_data = list(raw_csv_playoff_data)
    # lebron_playoff_data = ()
    # for playoff in playoff_data:
    #     # get rid of headers from csv
    #     if playoff[0][0] != '2': # if season val doesnt start with 2
    #         continue # next iteration of loop
    #     lebron_playoff_data_new = lebron_playoff_data + Lebron(tuple(playoff))
    # lebron_playoff_data = lebron_playoff_data_new

print("\n\nPLAYOFF DATA")
print(playoff_data)

# Question 1
print("\n\nQuestion 1: What is the total number of games (G) Lebron has played in the playoffs?")
total_playoff_games = sum(int(player.G) for player in playoff_data)
print(f"Lebron has played a total of {total_playoff_games} games in the playoffs.")

# Question 2
print("\n\nQuestion 2: What is Lebron's average FG attempts per game in the playoffs?")
average_fg_attempts_playoffs = mean(float(player.FGA) for player in playoff_data)
print(f"Lebron's average FG attempts per game in the playoffs is {average_fg_attempts_playoffs:.2f}.")

# Question 3
print("\n\nQuestion 3: IN THE SEASONS WHICH LEBRON MADE THE PLAYOFFS ONLY: was his average FG% higher in the regular season or the playoffs?")
regular_season_fg_percentages = [float(player.FG_per) for player in lebron_data]
playoff_fg_percentages = [float(player.FG_per) for player in playoff_data]

if mean(regular_season_fg_percentages) > mean(playoff_fg_percentages):
    print("Lebron had a higher average FG% in the regular season.")
else:
    print("Lebron had a higher average FG% in the playoffs.")

# Question 4
print("\n\nQuestion 4: IN THE SEASONS WHICH LEBRON MADE THE PLAYOFFS ONLY: create a new data set comparing minutes played in the regular season vs. playoffs (per season)")
minutes_comparison_data = [
    {'Season': player_season.Season, 'Regular Season MP': player_season.MP, 'Playoff MP': playoff_player.MP}
    for player_season, playoff_player in zip(lebron_data, playoff_data)
]

pprint(minutes_comparison_data)

# Question 5
print("\n\nQuestion 5: IN THE SEASONS WHICH LEBRON MADE THE PLAYOFFS ONLY: what season was his FG% above .500 in BOTH the regular season AND playoffs.")
seasons_fg_above_500_both = [player.Season for player, playoff_player in zip(lebron_data, playoff_data) if float(player.FG_per) > 0.5 and float(playoff_player.FG_per) > 0.5]
print(f"In the seasons Lebron made the playoffs, his FG% was above .500 in both the regular season and playoffs in the following seasons: {', '.join(seasons_fg_above_500_both)}")

# even though it looks bad apparently im using pprint right?

print("pls give me 100 Mr.P")
