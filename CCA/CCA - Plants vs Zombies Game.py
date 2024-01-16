'''
Author: Aadil Hussain
Built on: Python 3.11.7
'''

import pygame, random
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

# Peashooter class
class Peashooter():
    def __init__(self, type, pos, max_health=100):
        self.face_img = pygame.image.load("CCA\\assets\images\plants\peashooter.png").convert()
        self.max_health = max_health
        self.health = max_health

        self.damage_cooldown = 30

    def rect(self):
        return pygame.Rect((self.pos[0]*24) + 56, (self.pos[1]*24) + 50, 16, 16)

    def update(self, draw_pos):
        self.damage_cooldown -= 1

    def draw(self, display, draw_pos):
        display.blit(self.img, draw_pos)

    def damage(self):
        if self.damage_cooldown <= 0:
            self.health -= 1
            self.damage_cooldown = 30
            random.choice(pygame.mixer.Sound("CCA\\assets\sounds\chomp.ogg")).play()


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("CCA\\assets\images\plants\peashooter.png")
        pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Sprite groups
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)
players.add(player)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Refresh display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# ... (previous code)

# Initialize game statistics
game_stats = {
    'score': 0,
    'level': 1,
    'lives': 3,
}

# Game loop (continued)
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Display score and level
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {game_stats["score"]}', True, WHITE)
    level_text = font.render(f'Level: {game_stats["level"]}', True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    # Refresh display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# ... (previous code)

# CSV file name
csv_file = 'game_stats.csv'

# Game loop (continued)
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Display score and level
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {game_stats["score"]}', True, WHITE)
    level_text = font.render(f'Level: {game_stats["level"]}', True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    # Refresh display
    pygame.display.flip()

    # Save game statistics to CSV
    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ['score', 'level', 'lives']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write game statistics
        writer.writerow(game_stats)

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
