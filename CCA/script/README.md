# Plants vs Zombies (LITE)
## Game Logic
key points to keep a note of
- 10% chance you encounter a superzombie
- superzombie has x2 health and 30% speed boost
- you get $50 for killing a zombie
- can buy max of 5 additional plants(for a total of 6)
- you can't upgrade plant strength until you buy all plants.
- you start with $1000 so you can buy all the plants you want
- (game gets fun when you have max plants and max upgrades)

## Controls
| KEYBIND | ACTION |
|--------:|--------|
|P|Buy Plant|
|U|Buy Upgrades|
|B|Check Wallet Balance|

## Upgrades available
- Can buy new plant (up to 6 plants)
- Can increase plant strength (up to Lvl3)(cannot buy until all plants unlocked)
- Can increase pea(bullt) strength (up to Lvl3)
- Can increase pea(bullet) speed (up to Lvl3)
### Prices
|Item|Price|
|----|-----|
|PLANT ITEMS|====|
|New Plant|$250|
|Strength 2|$200|
|Strength 3|$400|
|PEA ITEMS|====|
|Strength 2|$100|
|Strength 3|$300|
|Speed 2|$500|
|Speed 3|$1000|

# Databasing
All data is stored in file named "database.csv"
The database contains the following columns:
- Username
- Money
- NumPlants
- ZombiesKilled
- SuperZombiesKilled
- ShotsMade
- MaxShotStrength
- MaxShotSpeed
Columns are listed in order.

## Properties of Columns
The following are key points containing details, parameters, and properties of each of the columns
- **Username**: This column stores the login username credential of the player.
- **Money**: Players earn $50 for every zombie they kill.
- **NumPlants**: The amount of Peashooter plants the player owns, player starts off at 1 by default and can buy a maximum of 5 additional plants for a total of 6.
- **ZombiesKilled**: the amount of zombies the player has killed, including Super Zombies.
- **SuperZombiesKilled**: the amount of superzombies the player has killed.
- **ShotsMade**: the amount of shots the player has made from all their plants overall.
- **MaxShotStrength**: The maximum strength the player has unlocked for their shots from peashooter plants. Player initially starts off with Level 1, and can increase to Levels 2 and 3 upon purchase of upgrade.
- **MaxShotSpeed**: The maximum speed the player has unlocked for their shots from peashooter plants. Player initially starts off with Level 1, and can increase to Levels 2 and 3 upon purchase of upgrade.