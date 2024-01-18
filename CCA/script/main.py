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

DATABASE_FILEPATH = 'CCA\\script\\database.csv'

# save data to csv
def save_stats(player:Player):
    with open(DATABASE_FILEPATH, 'a') as database_file:
        database_csv = csv.writer(database_file)
        database_csv.writerow([player.name, player.wallet, player.num_plants+1, player.zombies_killed, player.superzombies_killed, player.shots_made, player.shot_strength, player.shot_speed])

# detect collisions between sprites
def collision_detector(player:Player):
    objs_to_del = []
    for plant in player.plants:
        plant:Peashooter
        for zombie in plant.enemies:
            zombie:Zombie
            for shot in plant.shots:
                shot:Pea
                # check for zombie-pea collision
                zombie_pea_collision = pygame.sprite.collide_rect(zombie, shot)
                if zombie_pea_collision:
                    objs_to_del.append(shot)
                    zombie.hit_by_shot(shot.strength)
                    plant.shot_hit_zombie(shot)
                    plant.shooting = True
                    plant.shots.remove(shot)
                    
                # check for zombie-plant collision
                zombie_plant_collision = pygame.sprite.collide_rect(zombie, plant)
                if zombie_plant_collision:
                    plant.take_damage()
                    zombie.kill()
                    plant.enemies.remove(zombie)
                    del zombie
    
    for obj in objs_to_del:
        obj:pygame.sprite.Sprite()
        obj.kill()
        del obj

# build init player object
main_player = Player("Ault")
main_player.add_plant(PLANT_SPAWNPOINTS[main_player.num_plants])

ui_elements = pygame.sprite.Group()

dropshadow = DropShadow(30,30)
ui_elements.add(dropshadow)

clock = pygame.time.Clock() # FPS limiter required object
pygame.mixer.init()
pygame.mixer.music.load("CCA\script\\assets\music\grasswalk.mp3")
pygame.mixer.music.play(-1)

first_loop = True

# Main game loop
game_running = True
while True:

    # if quit, kill script
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game_running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # make electric fence
                print(NotImplementedError)
                print("This feature has been redacted")
            # show wallet balance on KBM B
            if event.key == pygame.K_b:
                main_player.show_balance()
            # add plants on KBM P
            if event.key == pygame.K_p:
                print(main_player.num_plants)
                if main_player.num_plants <= 5: # 5 not 6 bc index at 0
                    print(f"A plant costs $250\nYour Balance: ${main_player.wallet}")
                    if main_player.wallet >= 250:
                        main_player.add_plant(PLANT_SPAWNPOINTS[main_player.num_plants])
                        main_player.wallet -= 250
                        new_plant:Peashooter = main_player.plants[-1]
                        print(f"Purchased Plant {new_plant.plantID} for $250\nNew Balance: ${main_player.wallet}")
                    else: print("Purchase Failed.")
                else: print("Cannot add additional plants! 6 Plants Maximum")

            # Upgrades Menu on KBM U
            if event.key == pygame.K_u:
                main_player.upgrades_menu()
        if not game_running:
            break
    if not game_running:
            break
    
    # add background image
    screen.blit(PVZ_LAWN_IMG, (0,0))
    
    # add "dropshadow" to increase sprite visibility
    ui_elements.update()
    ui_elements.draw(screen)

    main_player.plantsgrouped.update()
    main_player.plantsgrouped.draw(screen)
    
    if first_loop:
        pygame.display.flip() # pygame window mainloop
        time.sleep(1)
        first_loop = False

    collision_detector(main_player)
 
    # plant management loop
    for plant in main_player.plants:
        '''loop to manage all attributes within peashooter'''
        plant:Peashooter

        # enemy management loop
        for enemy in plant.enemies:
            enemy:Zombie

            # when zombie dies
            if enemy.hp <= 0:
                # if zombie health <0, remove zomb from sys.mem
                if enemy.superzombie_status:
                    main_player.superzombies_killed += 1
                enemy.kill()
                plant.enemies.remove(enemy)
                del enemy
                # update player stats
                main_player.zombies_killed += 1
                # create replacement zombie
                plant.add_enem_zombie(ZOMBIE_SPAWNPOINTS[plant.plantID])
                main_player.wallet += 50
                print(f"Enemy Killed! +${50}\nNew Balance: ${main_player.wallet}")

        # if plant is supposed to be shooting, shoot
        if plant.enemies:
            plant.shoot(main_player)
            main_player.shots_made += 1

        # update and draw zombies
        plant.enemiesgrouped.update()
        plant.enemiesgrouped.draw(screen)

        # update and draw shots
        plant.shotsgrouped.update() # cant use any asyncio sleeps for smooth animation
        plant.shotsgrouped.draw(screen)

    pygame.display.flip() # pygame window mainloop
    clock.tick(144) # FPS limiter set to 144

save_stats(main_player)

sys.exit()
