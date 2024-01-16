'''
Author: Aadil Hussain
Built on: Python 3.11.7
'''

import pygame, random, asyncio
from pygame import Surface
import sys
import csv

# CULMINATING ASSIGNMENT
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

bg_lawn_image = pygame.image.load('CCA\\assets\\images\\Lawn.png')

# Define colors
AMBIENT_PVZ_BG_COLOR = (127, 202, 159)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
HOVER_GRAY = (150, 150, 150)

PLANT_SPAWNPOINTS = [(60, 240), (60, 180), (60, 320)]
ZOMBIE_SPAWNPOINTS = [(720, 240), (720, 180), (720, 320)]

# # Grid properties
# grid_size = min(WIDTH, HEIGHT) // 8  # Size of each cell
# rows = 6
# cols = 8

# # Create a 2D array to represent the grid
# grid = [[0 for _ in range(cols)] for _ in range(rows)]

# player
class Player():
    def __init__(self, username='player', start_money=500, start_plants=1):
        self.name = username
        self.wallet = start_money
        self.num_plants = 0 # max 5 plants
        self.plants = []

        # create starting plant row
        spawnpoint = PLANT_SPAWNPOINTS[self.num_plants]
        self.plants.append(Peashooter(spawnpoint[0], spawnpoint[1]))
        self.num_plants += 1
        print("Created initial player plant row.")
    
    def add_plant(self, spawn_coords):
        self.plants.append(Peashooter(spawn_coords[0], spawn_coords[1]))
        self.num_plants += 1
        print(f"Created Plant ID {self.num_plants}")



# Peashooter class
class Peashooter():
    def __init__(self, x, y, image_path = "CCA\\assets\\images\\plants\\peashooter.png"):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (60,100))
        self.enemies:Zombie = []

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    
    def add_enem_zombie(self, player:Player):
        
        

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

class DropShadow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("CCA\\assets\\images\\black.jpg")
        self.img = pygame.transform.scale(self.img, (750,525))
        self.img.set_alpha(100)
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))

main_player = Player()

dropshadow = DropShadow(30,30)

zombie = Zombie(ZOMBIE_SPAWNPOINTS[0][0], ZOMBIE_SPAWNPOINTS[0][1], 10)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # add background image
    screen.blit(bg_lawn_image, (0,0))
    
    # add "dropshadow" to increase sprite visibility
    dropshadow.draw()

    # Draw the Peashooter
    for plant in main_player.plants:
        plant.draw()

    asyncio.run(zombie.update())
    zombie.draw()

    # for row in range(rows):
    #     for col in range(cols):
    #         rect = pygame.Rect(col * grid_size, row * grid_size, grid_size, grid_size)

    #         # Check if the mouse is hovering over the cell
    #         if hover_row == row and hover_col == col:
    #             pygame.draw.rect(screen, HOVER_GRAY, rect)
    #         elif grid[row][col] == 0:
    #             pygame.draw.rect(screen, GRAY, rect)
    #         else:
    #             pygame.draw.rect(screen, BLACK, rect)

    pygame.display.flip()
