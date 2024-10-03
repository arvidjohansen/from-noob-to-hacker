import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BACKGROUND_COLOR = (0, 0, 0)
SQUARE_COLOR = (255, 255, 255)
SQUARE_SIZE = 50
MOVE_SPEED = 1
GRAVITY_CONSTANT = 9.8 / 15

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# The position of the square
square_pos = [WIDTH / 2, HEIGHT / 2]
is_falling = False
falling_time = 0.0
falling_speed = 0.0
time_jump_start = 0.0

clock = pygame.time.Clock()

def jump():
    square_pos[1] -= 10
    global is_falling
    is_falling = True
    global time_jump_start
    time_jump_start = pygame.time.get_ticks()
    global falling_speed
    falling_speed = GRAVITY_CONSTANT
    print("set jump time start to: ", time_jump_start)

def handle_gravity():
    # global square_pos
    square_pos[1] += falling_speed


while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current state of the keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_pos[0] -= MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        square_pos[0] += MOVE_SPEED
    if keys[pygame.K_UP]:
        square_pos[1] -= MOVE_SPEED
    if keys[pygame.K_DOWN]:
        square_pos[1] += MOVE_SPEED
    if keys[pygame.K_SPACE]:
        jump()

    handle_gravity()

    # Make sure the square doesn't move off the screen
    square_pos[0] = max(0, min(WIDTH - SQUARE_SIZE, square_pos[0]))
    square_pos[1] = max(0, min(HEIGHT - SQUARE_SIZE, square_pos[1]))

    # Fill the background
    screen.fill(BACKGROUND_COLOR)

    # Draw the square
    pygame.draw.rect(screen, SQUARE_COLOR, pygame.Rect(square_pos[0], square_pos[1], SQUARE_SIZE, SQUARE_SIZE))

    # Flip the display
    pygame.display.flip()