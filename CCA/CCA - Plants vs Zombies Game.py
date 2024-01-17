'''
Author: Aadil Hussain
Built on: Python 3.12.1
'''

import pygame, random, asyncio, math
import sys, csv
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

# Initialize screen/display
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
    
    def add_plant(self, spawn_coords):
        # create peashooter instance
        self.plants.append(Peashooter(spawn_coords[0], spawn_coords[1], self))
        self.num_plants += 1
        print(f"Created Plant ID {self.num_plants}")
        # create enemy zombie
        active_plant:Peashooter = self.plants[self.num_plants-1]
        active_plant.add_enem_zombie()


# Peashooter class
class Peashooter():
    def __init__(self, x, y, player:Player, plantID = 0, image_path = "CCA\\assets\\images\\plants\\peashooter.png"):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (60,100))
        self.enemies = []
        self.enemy_spawnpoint = ZOMBIE_SPAWNPOINTS[player.num_plants] # tuple (x, y)
        self.plantID = plantID
        if plantID == 0:
            self.plantID = player.num_plants
        self.shooting = False
        self.shots = []
        self.peashots = pygame.sprite.Group()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    
    def add_enem_zombie(self, spawnpoint=0):
        self.shooting = False
        if spawnpoint == 0:
            spawnpoint = self.enemy_spawnpoint
        self.enemies.append(Zombie(spawnpoint[0], spawnpoint[1], random.randint(10, 30)))
        print(f"Created Zombie {self.enemies[-1]}")
        self.shooting = True
    
    def shoot(self, spawnpoint=0):
        # if spawnpoint==0:
        #     spawnpoint = (self.x, self.y)
        # self.shots.append(Pea(spawnpoint[0], spawnpoint[1], 5))
        # print(f"Shot at zombie on row {self.plantID}")
        self.shots.append(Pea(400, 300, angle=0))
        self.peashots.add(self.shots[0])


class Pea(pygame.sprite.Sprite):
    def __init__(self, x, y, angle = 0, image_path = "CCA\\assets\\images\\projectiles\\pea.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.centerx = x-250 # correction from plant spawn coords
        self.rect.centery = y+10 # same as rect.centerx
        self.angle = angle
        self.speedx = 10 * math.cos(math.radians(self.angle))
        self.speedy = -10 * math.sin(math.radians(self.angle))
        self.fresh_shot = True # on first update of shot
    
    def update(self): # prior async
        # if self.fresh_shot:
        #     await asyncio.sleep(2)
        #     self.fresh_shot = False
        # await asyncio.sleep(0.005)
        # self.x += self.speed
        self.rect.x += self.speedx
        self.rect.y += self.speedy

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

# build init player object
main_player = Player("Ault")
main_player.add_plant(PLANT_SPAWNPOINTS[main_player.num_plants])

dropshadow = DropShadow(30,30)

cooldown = False
async def gen_rand_zombies(player:Player):
    # this generator doesnt work, blackscreens the whole program
    # will use diff method
    global cooldown
    if cooldown:    
        for plant in player.plants:
            print("found player")
            plant.add_enem_zombie()
    cooldown = True
    await asyncio.sleep(10)
    cooldown = False # need to fix

# asyncio.run(gen_rand_zombies(main_player))

clock = pygame.time.Clock()

# Main game loop
while True:
    clock.tick(FPS)

    # if quit, kill script
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # add background image
    screen.blit(PVZ_LAWN_IMG, (0,0))
    
    # add "dropshadow" to increase sprite visibility
    dropshadow.draw()

    # check zombie healths

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
            
            # update and draw zombies
            # asyncio.run(enemy.update())
            enemy.draw()

        # if plant is supposed to be shooting, shoot
        if plant.shooting:
            plant.shoot()
        plant.shooting = False
        
        # update and draw shots
        # for shot in plant.shots:
        #     shot:Pea
        #     asyncio.run(shot.update())
        #     shot.draw()
        plant.peashots.update() # cant use any asyncio sleeps for smooth animation
        plant.peashots.draw(screen)

        # draw plants
        plant.draw()

    pygame.display.flip() # pygame window mainloop

    clock.tick(60)
