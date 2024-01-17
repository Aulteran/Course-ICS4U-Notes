'''
Author: Aadil Hussain
Built on: Python 3.12.1
'''

import pygame, time
import sys, csv
from tkinter import *
from objects import *

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

# Initialize screen/display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plants vs Zombies")

# Define colors
AMBIENT_PVZ_BG_COLOR = (127, 202, 159)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
HOVER_GRAY = (150, 150, 150)

# background Plants vs Zombies Img filepath loaded in pygame
PVZ_LAWN_IMG = pygame.image.load('CCA\script\\assets\\images\\Lawn.png')

# build init player object
main_player = Player("Ault")
main_player.add_plant(PLANT_SPAWNPOINTS[main_player.num_plants])

ui_elements = pygame.sprite.Group()

dropshadow = DropShadow(30,30)
ui_elements.add(dropshadow)

clock = pygame.time.Clock() # FPS limiter required object

first_run = True

# Main game loop
while True:

    # if quit, kill script
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # add background image
    screen.blit(PVZ_LAWN_IMG, (0,0))
    
    # add "dropshadow" to increase sprite visibility
    ui_elements.draw(screen)

    main_player.plantsgrouped.update()
    main_player.plantsgrouped.draw(screen)
    
    if first_run:
        pygame.display.flip() # pygame window mainloop
        time.sleep(1)
        first_run = False

    # zombie list
    zombies = []
    zombie:Zombie
 
    # plant management loop
    for plant in main_player.plants:
        '''loop to manage all attributes within peashooter'''
        plant:Peashooter

        # enemy management loop
        for enemy in plant.enemies:
            enemy:Zombie

            # if zombie health <0, remove zomb from sys.mem
            if enemy.hp <= 0:
                del enemy
                # create replacement zombie
                plant.add_enem_zombie(ZOMBIE_SPAWNPOINTS[plant.plantID])

        # if plant is supposed to be shooting, shoot
        if plant.shooting:
            plant.shoot()
        plant.shooting = False

        # update and draw zombies
        plant.enemiesgrouped.update()
        plant.enemiesgrouped.draw(screen)

        # update and draw shots
        plant.peashots.update() # cant use any asyncio sleeps for smooth animation
        plant.peashots.draw(screen)

    pygame.display.flip() # pygame window mainloop

    clock.tick(60)
