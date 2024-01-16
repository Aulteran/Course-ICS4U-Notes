'''
Author: Aadil Hussain
Built on: Python 3.11.7
'''

import pygame, random, asyncio
from pygame import Surface
import sys
import csv

# For your culminating assignment, you will be incorporating all the techniques learned in the course over the semester.
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

bg_lawn_image = pygame.image.load('CCA\\assets\images\Lawn.png')

# Define colors
AMBIENT_PVZ_BG_COLOR = (127, 202, 159)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
HOVER_GRAY = (150, 150, 150)

# # Grid properties
# grid_size = min(WIDTH, HEIGHT) // 8  # Size of each cell
# rows = 6
# cols = 8

# # Create a 2D array to represent the grid
# grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Peashooter class
class Peashooter():
    def __init__(self, x, y, image_path = "CCA\\assets\images\plants\peashooter.png"):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (60,100))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# zombie class
class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, image_path = "CCA\\assets\images\zombies\normal.png"):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load("CCA\\assets\images\zombies\\normal.png")
        self.image = pygame.transform.scale(self.image, (70,100))
        self.hp = 100
    
    def damaged(self, damage_dealt):
        self.hp -= damage_dealt

    async def update(self):
        self.x -= self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class DropShadow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("CCA\\assets\images\\black.jpg")
        self.img = pygame.transform.scale(self.img, (750,500))
        self.img.set_alpha(100)
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))


# Create a Peashooter instance
plants = [
    Peashooter(60, 20),  
    Peashooter(60, 90),  
    Peashooter(60, 160)
]

zombies = [
    Zombie(500, 110, speed = 50)
]

dropshadow = DropShadow(30,30)

async def update_zombies(currrent_zombie:Zombie):
    await asyncio.sleep(1)
    currrent_zombie.update()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # # Get mouse position
    # mouse_x, mouse_y = pygame.mouse.get_pos()
    # hover_row = mouse_y // grid_size
    # hover_col = mouse_x // grid_size

    # Draw the grid
    # screen.fill(AMBIENT_PVZ_BG_COLOR)
    screen.blit(bg_lawn_image, (0,0))
    
    dropshadow.draw()

    # Draw the Peashooter
    for peashooter in plants:
        peashooter.draw()

    for zombie in zombies:
        update_zombies(zombie)
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
