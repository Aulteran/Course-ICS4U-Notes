import pygame
import sys
import math

# Define the projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        # Load the image and get its rect
        self.image = pygame.image.load("CCA\\assets\\images\\projectiles\\pea.png")
        self.rect = self.image.get_rect()
        # Set the initial position and angle
        self.rect.centerx = x
        self.rect.centery = y
        self.angle = angle
        # Set the speed based on the angle
        self.speedx = 10 * math.cos(math.radians(self.angle))
        self.speedy = -10 * math.sin(math.radians(self.angle))

    def update(self):
        # Move the projectile by adding the speed to the rect
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Remove the projectile if it goes off the screen
        if self.rect.left > 800 or self.rect.right < 0 or self.rect.top > 600 or self.rect.bottom < 0:
            self.kill()

# Initialize pygame and create the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Projectile Example")

# Create a group to store the projectiles
projectiles = pygame.sprite.Group()

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        # Quit the game if the user closes the window
        if event.type == pygame.QUIT:
            running = False
        # Fire a projectile if the user presses the space bar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Get the mouse position and calculate the angle
                mouse_x, mouse_y = pygame.mouse.get_pos()
                angle = math.degrees(math.atan2(mouse_y - 300, mouse_x - 400))
                # Create a new projectile and add it to the group
                projectile = Projectile(400, 300, angle)
                projectiles.add(projectile)

    # Update the sprites
    projectiles.update()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the sprites
    projectiles.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit pygame
pygame.quit()
# Quit the program
sys.exit()
