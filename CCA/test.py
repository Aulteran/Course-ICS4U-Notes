import pygame
import os

# Initialize pygame
pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

# Load the sprite images into a list
sprite_images = []
image = pygame.image.load("CCA\\assets\\images\\zombies\\normal.png")
image = pygame.transform.scale(image, (100,100))
sprite_images.append(image)

# Define the sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, position, images):
        # Call the parent class constructor
        super(MySprite, self).__init__()
        # Set the image and rect attributes
        self.images = images
        self.index = 0
        self.image = images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = position
        # Set the animation speed
        self.animation_speed = 4
        self.current_time = 0

    def update(self, dt):
        # Update the image based on the time elapsed
        self.current_time += dt
        if self.current_time >= self.animation_speed:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

# Create a sprite group and add the sprite object
sprite_group = pygame.sprite.Group()
sprite = MySprite((400, 300), sprite_images)
sprite_group.add(sprite)

# Main game loop
running = True
while running:
    # Get the time elapsed since the last frame
    dt = clock.tick(60) / 1000
    # Handle the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the sprite group
    sprite_group.update(dt)
    # Clear the screen
    screen.fill((0, 0, 0))
    # Draw the sprite group
    sprite_group.draw(screen)
    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
