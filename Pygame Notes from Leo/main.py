import pygame
import random
# Use opengameart.org for assets

from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN,
                           QUIT, RLEACCEL)  # KEYDOWN - press on the key

pygame.init()  # Instantiate pygame
pygame.mixer.init () # Initialize mixer object

# Create variables for game window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

sensitivity = 5

# Set up the game window
#screen = pygame.display.set_mode((500,500))  # Pass in pixel dimensions as tuple
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Establish classes
class Player(pygame.sprite.Sprite):  # Pass in parent class

  def __init__(self):
    super(Player, self).__init__()
    # Create surface with a tuple for len and widddd
    #self.surf = pygame.Surface((75, 25))
    self.surf = pygame.image.load("CCA\Pygame Notes Leo\Images\jet.png").convert()
    #self.surf.fill((255, 255, 255))
    self.surf.set_colorkey((255,255,255), RLEACCEL) # Key out background of image
    self.rect = self.surf.get_rect()  # Grab position of surface

  def update(self, pressed_keys):
    if pressed_keys[K_UP]:
      self.rect.move_ip(0, -1 * sensitivity)  # Move in place by however many pixels
      move_up_sound.play()
    if pressed_keys[K_DOWN]:
      self.rect.move_ip(0, 1 * sensitivity)
      move_down_sound.play()
    if pressed_keys[K_LEFT]:
      self.rect.move_ip(-1 * sensitivity, 0)
    if pressed_keys[K_RIGHT]:
      self.rect.move_ip(1 * sensitivity, 0)

    # Keep player on screen
    if self.rect.left < 0:
      self.rect.left = 0
    if self.rect.right > SCREEN_WIDTH:
      self.rect.right = SCREEN_WIDTH
    if self.rect.top <= 0:
      self.rect.top = 0
    if self.rect.bottom >= SCREEN_HEIGHT:
      self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):

  def __init__(self):
    super(Enemy, self).__init__()
    self.surf = pygame.Surface((20, 10))
    self.surf.fill((255,255,255))
    self.rect = self.surf.get_rect(center = 
                                   (random.randint(0, SCREEN_WIDTH + 50), 
                                     random.randint(0, SCREEN_HEIGHT)))
    self.speed = random.randint(1,5)

  def update(self):
    self.rect.move_ip(-self.speed, 0)

    if self.rect.left < 0:  # If lefthand side of rectangle is to the left of the screen
      self.kill()

class Cloud(pygame.sprite.Sprite):

  def __init__(self):
    super(Cloud, self).__init__()
    self.surf = pygame.image.load('CCA\Pygame Notes Leo\Images\cloud.png').convert()
    self.surf.set_colorkey((0,0,0), RLEACCEL)
    # Randomly generate coordinates
    self.rect = self.surf.get_rect(center = (
      random.randint(SCREEN_WIDTH + 10, SCREEN_WIDTH + 50),
      random.randint(0, SCREEN_HEIGHT))
    )

  def update(self):
    self.rect.move_ip(-1,0)
    if self.rect.left < 0:
      self.kill() 

# Add a clock element
clock = pygame.time.Clock()

# Add music
pygame.mixer.music.load('CCA\Pygame Notes Leo\Sounds\Sky_dodge_theme.ogg')
pygame.mixer.music.play(-1)  # Parameter: number of times to play; -1 -> loop forever

move_up_sound = pygame.mixer.Sound('CCA\Pygame Notes Leo\Sounds\Jet_up.ogg')
move_down_sound = pygame.mixer.Sound('CCA\Pygame Notes Leo\Sounds\Jet_down.ogg')
collission_sound = pygame.mixer.Sound('CCA\Pygame Notes Leo\Sounds\Boom.ogg')

move_down_sound.set_volume(0.6)
move_up_sound.set_volume(0.6)
collission_sound.set_volume(1.0)

# Add a custom event for cloud
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Adding a custom event
ADDENEMY = pygame.USEREVENT + 1  # Use 1 to identify particular event
pygame.time.set_timer(ADDENEMY, 500)  # Arguments: What to happen, how often
# Called outside of game loop; fire a custom event every 250 ms

player_1 = Player()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()

all_sprites.add(player_1)

running = True

while running:
  # Check for Handle Events
  for event in pygame.event.get():

    # Did the user hit a key?
    if event.type == KEYDOWN:
      # Was it the escape key?
      if event.key == K_ESCAPE:
        running = False

    elif event.type == pygame.QUIT:
      running = False

    elif event.type == ADDENEMY:
      # Create a new enemy
      new_enemy = Enemy()
      enemies.add(new_enemy)
      all_sprites.add(new_enemy)

    elif event.type == ADDCLOUD:
      new_cloud = Cloud()
      clouds.add(new_cloud)
      all_sprites.add(new_cloud)

  # Check user input
  pressed_keys = pygame.key.get_pressed()

  # Pass in pressed keys
  player_1.update(pressed_keys)

  # Update enemies
  enemies.update()

  # Update clouds
  clouds.update()
  
  # Draw stuff
  screen.fill((135, 205, 235))  # RGB - Sky Blue

  #surf_center = ((SCREEN_WIDTH - surf.get_width()) / 2,(SCREEN_HEIGHT - surf.get_height()) / 2)

  #Draw items on the screen
  for entity in all_sprites:
    screen.blit(entity.surf, entity.rect)
  #screen.blit(player_1.surf, player_1.rect)

    if pygame.sprite.spritecollideany(player_1, enemies):
      move_up_sound.stop()
      move_down_sound.stop()
      pygame.time.delay(50)
      collission_sound.play()
      pygame.time.delay(1000)
      player_1.kill()
      print("Game Over!")
      running = False
  
  # Parameters: onto what, colour, location, radius
  #pygame.draw.circle(screen, (0,0,255), (250,250), 75)

  pygame.display.flip()  # Update the full display to the screen

  clock.tick(60)

pygame.mixer.music.stop()

pygame.quit()