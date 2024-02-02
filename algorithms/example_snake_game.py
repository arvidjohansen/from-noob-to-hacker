import math
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

DEBUG = True

# Set up some constants
SQUARE_HEIGHT = 100
SQUARE_WIDTH = 100
WIDTH, HEIGHT = SQUARE_WIDTH * 10, SQUARE_HEIGHT * 10  # Screen dimensions
FPS = 10  # Frames per second
SPEED = 100  # Speed of the object

color = (255,255,255) # initial color of object

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the object
object_pos = [WIDTH // 2, HEIGHT // 2]
apple_pos = [round(random.randint(0, WIDTH - SQUARE_WIDTH),-2), round(random.randint(0, HEIGHT - SQUARE_HEIGHT),-2)]
apples_eaten = 0
gun_angle = 90
gun_end_pos = [0,0]
cannonballs = []

# todo 
# write tail

# Set up the clock
clock = pygame.time.Clock()

def random_position():
    return [round(random.randint(0, WIDTH - SQUARE_WIDTH),-2), round(random.randint(0, HEIGHT - SQUARE_HEIGHT),-2)]
def draw_background():
    screen.fill((0, 0, 0))  # Fill the screen with black
def draw_score():
    # Apples eaten
    font = pygame.font.Font(None,128)
    text = font.render(str(apples_eaten),True,(255,255,255))
    text_pos = text.get_rect(center=(WIDTH - SQUARE_WIDTH, SQUARE_HEIGHT))
    screen.blit(text,text_pos)
def draw_object():
    # pygame.draw.circle(screen, (255, 255, 255), object_pos, 20)
    pygame.draw.rect(screen, color, pygame.Rect(object_pos[0], object_pos[1], SQUARE_HEIGHT,SQUARE_WIDTH))  # Draw the object

    if DEBUG:
         # Set up the font and render the position text
        font = pygame.font.Font(None, 36)
        text = font.render(f'{object_pos[0]},{object_pos[1]}', True, (0, 0, 0))

        # Calculate the position for the text
        text_pos = text.get_rect(center=(object_pos[0] + SQUARE_WIDTH // 2, object_pos[1] + SQUARE_HEIGHT // 2))

        # Draw the text
        screen.blit(text, text_pos)
def draw_gun():
    # pygame.draw.circle(screen, (255, 255, 255), object_pos, 20)
    # Draw the gun
    gun_length = 80
    gun_width = 10
    global gun_end_pos
    gun_end_pos = [object_pos[0] + gun_length * math.cos(math.radians(gun_angle)),
                   object_pos[1] - gun_length * math.sin(math.radians(gun_angle))]
    pygame.draw.line(screen, (255, 255, 255), (object_pos[0] + SQUARE_WIDTH//2, object_pos[1] ), gun_end_pos, gun_width)
def draw_apple():
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(apple_pos[0], apple_pos[1], SQUARE_HEIGHT,SQUARE_WIDTH))  # Draw the object
    if DEBUG:
         # Set up the font and render the position text
        font = pygame.font.Font(None, 36)
        text = font.render(f'{apple_pos[0]},{apple_pos[1]}', True, (0, 0, 0))

        # Calculate the position for the text
        text_pos = text.get_rect(center=(apple_pos[0] + SQUARE_WIDTH // 2, apple_pos[1] + SQUARE_HEIGHT // 2))

        # Draw the text
        screen.blit(text, text_pos)
def draw_fps():
    font = pygame.font.Font(None, 36)
    text = font.render(f'FPS: {round(clock.get_fps(),2)}', True, (255, 255, 0))
    screen.blit(text, (0, 0))
def draw_cannonballs():
    for cannonball in cannonballs:
        cannonball[0][0] += cannonball[1][0]
        cannonball[0][1] += cannonball[1][1]
        pygame.draw.circle(screen, (255, 255, 255), [int(x) for x in cannonball[0]], 10)
def shoot():
    # Called when space is pressed
    # Spawn a new canonball
    velocity = [5 * math.cos(math.radians(gun_angle)), -5 * math.sin(math.radians(gun_angle))]
    cannonballs.append([list(gun_end_pos), velocity])
def handle_input():
    global gun_angle
    for event in pygame.event.get():
        if DEBUG:
            print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Spawn a new cannonball
                shoot()

    # Object movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and object_pos[0] > 0:
        object_pos[0] -= SPEED
    if keys[pygame.K_RIGHT] and object_pos[0] < WIDTH - SQUARE_WIDTH:
        object_pos[0] += SPEED  
    if keys[pygame.K_UP] and object_pos[1] > 0:
        object_pos[1] -= SPEED
    if keys[pygame.K_DOWN] and object_pos[1] < HEIGHT - SQUARE_HEIGHT:
        object_pos[1] += SPEED
    # Gun rotation
    if keys[pygame.K_a]:
        gun_angle = (gun_angle + 2) % 360  # Rotate left
    if keys[pygame.K_d]:
        gun_angle = (gun_angle - 2) % 360  # Rotate right
    gun_angle = max(min(gun_angle, 180), 0)  # Limit angle between 0 (3 o'clock) and 180 (9 o'clock)
def update_color():
    global color
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
def collision_detection():
    # check if apple is eaten
    global apple_pos
    if DEBUG:
        print(object_pos, apple_pos)
    if object_pos[0] == apple_pos[0] and object_pos[1] == apple_pos[1]:
        print("apple eaten")
        global apples_eaten
        apples_eaten += 1
        apple_pos = random_position()
    # check if cannonball hits apple
    for c in cannonballs:
        if c[0] == apple_pos[0] and c[1] == apple_pos[1]:
            print("canonball inside apple!")
            apples_eaten += 1
            apple_pos = random_position()
            cannonballs.remove(c)

# Game loop
while True:
    # Event handling
    
    # update_color()
    handle_input()
    collision_detection()

    # Draw everything
    draw_background()
    draw_apple()
    draw_object()
    draw_gun()
    draw_cannonballs()
    draw_score()
    draw_fps()
    

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate    
    clock.tick(FPS)