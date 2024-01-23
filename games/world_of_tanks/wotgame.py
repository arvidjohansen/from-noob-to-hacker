import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
SPEED = 1

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the tank image
tank = pygame.image.load('tank.png')

# Set the tank's starting position
tank_pos = [WIDTH // 2, HEIGHT // 2]

class Bullet:
    def __init__(self, pos):
        self.pos = list(pos)
        self.speed = 2
        self.state = 'flying'
        self.image = pygame.image.load('bullet.png')
        self.explosion_image = pygame.image.load('explosion.png')
        print('created bullet')

    def move(self):
        self.pos[0] += self.speed
        print(f'moved bullet to: {self.pos}')

    def check_collision(self, target):
        bullet_rect = pygame.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())
        target_rect = pygame.Rect(target[0], target[1], tank.get_width(), tank.get_height())
    
        if bullet_rect.colliderect(target_rect):
            self.explode()

    def explode(self):
        print(f'bullet exploded at {self.pos}')
        self.state = 'exploded'

bullets = []

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current key presses
    keys = pygame.key.get_pressed()

    # Move the tank
    if keys[pygame.K_LEFT]:
        tank_pos[0] -= SPEED
    if keys[pygame.K_RIGHT]:
        tank_pos[0] += SPEED
    if keys[pygame.K_UP]:
        tank_pos[1] -= SPEED
    if keys[pygame.K_DOWN]:
        tank_pos[1] += SPEED
    
    if keys[pygame.K_SPACE]:
        # Create the bullet at the top of the tank
        bullet_pos = [tank_pos[0] + tank.get_width() , tank_pos[1]]
        bullets.append(Bullet(bullet_pos))


    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(tank, tank_pos)

    # Update and draw bullets
    for bullet in bullets:
        if bullet.state == 'flying':
            bullet.move()
            bullet.check_collision(tank_pos)
            screen.blit(bullet.image, bullet.pos)
        elif bullet.state == 'exploded':
            screen.blit(bullet.explosion_image, bullet.pos)

    # Update the display
    pygame.display.flip()