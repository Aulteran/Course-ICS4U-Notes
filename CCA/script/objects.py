'''
Author: Aadil Hussain
Built on: Python 3.12.1
'''

import pygame, random, math

# predefined default possible spawnpoints for zombies
PLANT_SPAWNPOINTS = [(60, 240), (60, 160), (60, 320), (60, 90), (60, 390), (60, 30)]
ZOMBIE_SPAWNPOINTS = [(720, 260), (720, 180), (720, 340), (720, 110), (720, 400), (720, 50)]

plants_vertically_ordered = [6, 4, 2, 1, 3, 5] # plant IDs top to bottom

UPGRADES_MENU_PROMPT = (
'''======|UPGRADES|======
1) Stronger Plant (2 Strength Levels)
2) Stronger Peashot (2 Strength Levels)
3) Faster Peashot (2 Speed Levels)
4) Go Back (EXIT MENU)
Please Select: ''')

# gets int/float inputs without error
def numQuery(prompt):
    try:
        return int(input(prompt))
    except(ValueError):
        print("invalid input, please enter a number")

# player class
class Player():
    def __init__(self, username='player', start_money=10000, start_plants=1):
        self.name = username
        self.wallet = start_money
        self.num_plants = 0 # max 6 plants
        self.plants = []
        self.plantsgrouped = pygame.sprite.Group()
        self.shot_strength = 1 # levels 1 to 3
        self.shot_speed = 1 # levels 1 to 3
        self.zombies_killed = 0
        self.superzombies_killed = 0
        self.shots_made = 0
    
    def add_plant(self, spawn_coords):
        if self.num_plants >= 6:
            print("Cannot add additional plants! 6 Plants Maximum")
            return
        # create peashooter instance
        self.plants.append(Peashooter(spawn_coords[0], spawn_coords[1], self))
        self.num_plants += 1
        print(f"Created Plant ID {self.num_plants}")
        active_plant:Peashooter = self.plants[self.num_plants-1]

        # add plant to sprite group for easy updates and drawings
        self.plantsgrouped.add(active_plant)

        # create enemy zombie
        active_plant.add_enem_zombie()
    
    def show_balance(self):
        print(f"USER WALLET\nBalance: {self.wallet}")
    
    def upgrades_menu(self):
        upgrade_choice = numQuery(UPGRADES_MENU_PROMPT)
        # upgrade plant strength
        if upgrade_choice == 1:
            print("Plants are numbered from top to bottom.")
            select_plant = input("Which plant would you like to upgrade?: ")
            plantID = plants_vertically_ordered[select_plant-1]
            plant_selected:Peashooter = self.plants[plantID]
            if plant_selected.strengthLevel == 1:
                cost = 200
                if self.wallet >= 200:
                    plant_selected.health = 200
                    plant_selected.strengthLevel = 2
            elif plant_selected.strengthLevel == 2:
                cost = 400
                if self.wallet >= cost:
                    plant_selected.health = 300
                    plant_selected.strengthLevel = 3
            print(f"Plant strength upgraded to Lvl{plant_selected.strengthLevel} for ${cost}\nNew Balance: {self.wallet}")
        # upgrade peashot strength
        if upgrade_choice == 2:
            if self.shot_strength == 1:
                cost = 100
                if self.wallet >= cost:
                    self.shot_strength = 2
                    self.wallet -= cost
                else: print(f"Can't afford. Need ${cost}")
            elif self.shot_strength == 2:
                cost = 300
                if self.wallet >= cost:
                    self.shot_strength = 3
                    self.wallet -= cost
                else: print(f"Can't afford. Need ${cost}")
            print(f"Peashots strength upgraded to Lvl{self.shot_strength} for ${cost}\nNew Balance: {self.wallet}")
        # upgrade peashot speed
        if upgrade_choice == 3:
            if self.shot_speed == 1:
                cost = 500
                if self.wallet >= cost:
                    self.shot_speed = 2
                    self.wallet -= cost
                else: print(f"Can't afford. Need ${cost}")
            elif self.shot_speed == 2:
                cost = 1000
                if self.wallet >= cost:
                    self.shot_speed = 3
                    self.wallet -= cost
                else: print(f"Can't afford. Need ${cost}")
            print(f"Peashots speed upgraded to Lvl{self.shot_speed} for ${cost}\nNew Balance: {self.wallet}")

# Peashooter class
class Peashooter(pygame.sprite.Sprite):
    def __init__(self, x, y, player:Player, plantID = 0, image_path = "CCA\\script\\assets\\images\\plants\\peashooter.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (60,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = x + 25
        self.rect.centery = y + 60
        self.enemies = []
        self.enemy_spawnpoint = ZOMBIE_SPAWNPOINTS[player.num_plants] # tuple (x, y)
        self.plantID = plantID
        if plantID == 0:
            self.plantID = player.num_plants
        self.shooting = False
        self.shots = []
        self.shotsgrouped = pygame.sprite.Group()
        self.enemiesgrouped = pygame.sprite.Group()
        self.strengthLevel = 1
        self.health = 100
    
    def add_enem_zombie(self, spawnpoint=0):
        if spawnpoint == 0:
            spawnpoint = self.enemy_spawnpoint
        self.enemies.append(Zombie(spawnpoint[0], spawnpoint[1]+15, random.uniform(0.5, 2)))
        self.enemiesgrouped.add(self.enemies[-1])
    
    def shoot(self, player:Player, spawnpoint=0):
        if spawnpoint==0:
            spawnpoint = (self.rect.centerx, self.rect.centery)
        self.shots.append(Pea(spawnpoint[0], spawnpoint[1], player))
        self.shotsgrouped.add(self.shots[0])
        self.shooting = False
    
    def shot_hit_zombie(self, shot):
        shot:Pea
        shot.kill()
        del shot
    
    def take_damage(self):
        self.health -= 50

class Pea(pygame.sprite.Sprite):
    def __init__(self, x, y, player:Player,  angle = 0,  image_path = "CCA\\script\\assets\\images\\projectiles\\pea.png"):
        pygame.sprite.Sprite.__init__(self)
        # Load, transform, and get rect of image
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        # Set init pos, speed, and angle
        self.rect.centerx = x + 30
        self.rect.centery = y + 20
        self.angle = angle

        # set shot speed
        if player.shot_speed == 1:
            self.speedconst = 2
        if player.shot_speed == 2:
            self.speedconst = 10
        if player.shot_speed == 3:
            self.speedconst = 15

        # Set speed based off angle, will prolly be 0 degrees for PvZ
        self.speedx = self.speedconst * math.cos(math.radians(self.angle))
        self.speedy = -(self.speedconst) * math.sin(math.radians(self.angle))

        # set shot strength
        if player.shot_speed == 1:
            self.strength = 30
        if player.shot_strength == 2:
            self.strength = 40
        if player.shot_strength == 3:
            self.strength = 50
    
    def update(self): 
        self.rect.x += self.speedx
        self.rect.y += self.speedy

# zombie class
class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, speed = 1, image_path = "CCA\\script\\assets\\images\\zombies\\normal.png"):
        pygame.sprite.Sprite.__init__(self)
        # Load, transform, and get rect of image
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect()
        # set init pos and speed
        self.rect.centerx = x
        self.rect.centery = y + 40
        self.speed = speed
        self.hp = 100
        self.superzombie_status = False
        # 1/5 chance make superzombie
        if random.randint(1,10) == 1:
            print("SUPERSTRENGTH ZOMBIE HAS SPAWNED!")
            self.speed = 2.5 # 30% speed boost
            self.hp *= 2 # 2x hp
            self.image = pygame.image.load("CCA\\script\\assets\\images\\zombies\\superzombie.png")
            self.image.convert()
            self.image = pygame.transform.scale(self.image, (70,100))
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y + 40
            self.superzombie_status = True
        
    def hit_by_shot(self, damage_dealt):
        self.hp -= damage_dealt

    def update(self):
        self.rect.x -= self.speed

# dropshadow to increase sprite visibility
class DropShadow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("CCA\\script\\assets\\images\\black.jpg")
        self.image = pygame.transform.scale(self.image, (750,525))
        self.image.set_alpha(100)
        self.rect = self.image.get_rect()
        self.rect.centerx = x + 375
        self.rect.centery = y + 250