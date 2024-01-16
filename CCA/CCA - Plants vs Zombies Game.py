'''
Author: Aadil Hussain
Built on: Python 3.12.1
'''

import pygame, random, asyncio
import sys, csv
from pygame import Surface
from tkinter import *

# CULMINATING ASSIGNMENT INSTRUCTIONS
# Incorportate all the techniques learned in the course over the semester.
# You will be creating a computer game level using PyGame. You must:
# -	Include an OOP approach
# --	Have User Classes
# --	A Scoring element (4U only)
# --	Collision detection
# --	Sprite groups
# --	Music and SFX (4U only)
# -	Save user results to a CSV
# -	Use Jupyter Notebooks and Pandas to analyze some piece from the CSV
# --	Proper data frame organization
# --	More than one data Series within the data frame
# --	Do some sorting OR filtering OR groupby within the data frame
# --	Display a relevant data piece that has been analyzed in some way
# --	Visualize the Data (4U only)

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plants vs Zombies")

# Define colors
AMBIENT_PVZ_BG_COLOR = (127, 202, 159)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
HOVER_GRAY = (150, 150, 150)

# predefined default possible spawnpoints for zombies
PLANT_SPAWNPOINTS = [(60, 240), (60, 180), (60, 320)]
ZOMBIE_SPAWNPOINTS = [(720, 240), (720, 180), (720, 320)]

# background Plants vs Zombies Img filepath loaded in pygame
PVZ_LAWN_IMG = pygame.image.load('CCA\\assets\\images\\Lawn.png')

# player
class Player():
    def __init__(self, username='player', start_money=500, start_plants=1):
        self.name = username
        self.wallet = start_money
        self.num_plants = 0 # max 5 plants
        self.plants = []

        # create starting plant row
        spawnpoint = PLANT_SPAWNPOINTS[self.num_plants]
        self.plants.append(Peashooter(spawnpoint[0], spawnpoint[1], self))
        self.num_plants += 1
        print("Created initial player plant row.")
    
    def add_plant(self, spawn_coords):
        self.plants.append(Peashooter(spawn_coords[0], spawn_coords[1], self))
        self.num_plants += 1
        print(f"Created Plant ID {self.num_plants}")

# Peashooter class
class Peashooter():
    def __init__(self, x, y, player:Player, image_path = "CCA\\assets\\images\\plants\\peashooter.png"):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (60,100))
        self.enemies:Zombie
        self.enemies = []
        self.enemy_spawnpoint = ZOMBIE_SPAWNPOINTS[player.num_plants] # tuple (x, y)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    
    def add_enem_zombie(self):
        self.enemies.append(Zombie(self.enemy_spawnpoint[0], self.enemy_spawnpoint[1], random.randint(10, 30)))
        

# zombie class
class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, speed = 1, image_path = "CCA\\assets\\images\\zombies\\normal.png"):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (70,100))
        self.hp = 100
    
    def damaged(self, damage_dealt):
        self.hp -= damage_dealt

    async def update(self):
        await asyncio.sleep(1)
        self.x -= self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# dropshadow to increase sprite visibility
class DropShadow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("CCA\\assets\\images\\black.jpg")
        self.img = pygame.transform.scale(self.img, (750,525))
        self.img.set_alpha(100)
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))

# build player object
main_player = Player()

dropshadow = DropShadow(30,30)

async def gen_rand_zombies(player:Player):
    for plant in player.plants:
        plant:Zombie
        plant.add_enem_zombie()

main_player.add_plant(PLANT_SPAWNPOINTS[main_player.num_plants])

x=1

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # add background image
    screen.blit(PVZ_LAWN_IMG, (0,0))
    
    # add "dropshadow" to increase sprite visibility
    dropshadow.draw()

    zombies = []
    zombie:Zombie

    # Draw the Peashooter
    for plant in main_player.plants:
        print(f"Found plant {plant}")
        plant.draw()
        print("Drew plant")
        enemy:Zombie
        for enemy in plant.enemies:
            print(f"Found Zombie {enemy}")
            zombies.append(enemy)
    while x==1:
        print(zombies)
        x=0

    for zombie in zombies:
        zombie.update()
        zombie.draw()

    pygame.display.flip() # pygame window mainloop
