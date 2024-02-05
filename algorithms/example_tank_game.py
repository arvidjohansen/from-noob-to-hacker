


import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Duck Hunt Tank Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the clock
clock = pygame.time.Clock()


def load_image(name:str, scale_to=1.0) -> pygame.Surface:
    """loads an image from the file 
    and scales it (optionally) to the given size.
    
    Keyword arguments:
    name -- string, name of the image file
    scale_to -- float, the scale factor (default 1.0)
    Return: pygame.Surface, the image
    """    
    img = pygame.image.load(name)
    if scale_to != 1.0:
        img = pygame.transform.scale(img, (
            int(img.get_width() * scale_to), 
            int(img.get_height() * scale_to)))
    return img

def draw_fps(pos_x=0, pos_y=0, size=36) -> None:
    """Draws the current frames per second on the screen

    Keyword arguments:
    pos_x -- int, x position of the text (default 0)
    pos_y -- int, y position of the text (default 0)
    size -- int, size of the text (default 36)
    Return: None
    """
    
    font = pygame.font.Font(None, size)
    text = font.render(f'FPS: {round(clock.get_fps(),2)}', True, (255, 255, 0))
    screen.blit(text, (pos_x, pos_y))


# Set up tank
tank_image = load_image('tank2.png', 0.5)
tank_rect = tank_image.get_rect()
tank_speed = 5
tank_angle_speed = 2
tank_angle = 0

# Set up projectile
bullet_image = load_image('bullet.png', 0.1)

bullet_rect = bullet_image.get_rect()
bullet_speed = 10
bullet_active = False

# Set up duck
duck_image = load_image('duck.png', 0.1)
duck_rect = duck_image.get_rect()
duck_speed = 3
duck_active = False

# Set up explosion
explosion_image = load_image('explosion.png', 0.1)
explosion_rect = explosion_image.get_rect()
explosion_active = False

# Set up clock
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Tank movement
    if keys[pygame.K_w]:
        tank_rect.y -= tank_speed
    if keys[pygame.K_s]:
        tank_rect.y += tank_speed
    if keys[pygame.K_a]:
        tank_rect.x -= tank_speed
    if keys[pygame.K_d]:
        tank_rect.x += tank_speed

    # Tank rotation
    if keys[pygame.K_LEFT]:
        tank_angle -= tank_angle_speed
    if keys[pygame.K_RIGHT]:
        tank_angle += tank_angle_speed

    # Fire bullet
    if keys[pygame.K_SPACE] and not bullet_active:
        bullet_rect.x = tank_rect.x + tank_rect.width // 2
        bullet_rect.y = tank_rect.y + tank_rect.height // 2
        bullet_active = True
    # Fire bullet
    if keys[pygame.K_r]:
        bullet_active = False

    # Update bullet position
    if bullet_active:
        angle_rad = math.radians(tank_angle)
        bullet_rect.x += int(bullet_speed * math.cos(angle_rad))
        bullet_rect.y -= int(bullet_speed * math.sin(angle_rad))

        # Check if bullet hits duck
        if bullet_rect.colliderect(duck_rect):
            explosion_rect.x = duck_rect.x
            explosion_rect.y = duck_rect.y
            explosion_active = True
            duck_active = False
            bullet_active = False

    # Update duck position
    if not duck_active:
        if random.randint(0, 100) < 1:
            duck_rect.x = random.randint(0, width)
            duck_rect.y = random.randint(0, height // 2)
            duck_active = True

    if duck_active:
        duck_rect.y += duck_speed

        # Check if duck reaches top half of the window
        if duck_rect.y > height // 2:
            duck_active = False

    # Draw everything on the screen
    screen.fill(black)
    rotated_tank = pygame.transform.rotate(tank_image, tank_angle)
    screen.blit(rotated_tank, tank_rect)

    if bullet_active:
        screen.blit(bullet_image, bullet_rect)

    if duck_active:
        screen.blit(duck_image, duck_rect)

    if explosion_active:
        screen.blit(explosion_image, explosion_rect)
        explosion_active = False

    pygame.display.flip()
    clock.tick(30)
