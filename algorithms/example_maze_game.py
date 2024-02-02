import pygame
import random

# Define constants for the width and height of each grid location
WIDTH = 20
HEIGHT = 20

# Define constants for grid dimensions
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Define some colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the AI and goal
ai = [0, 0]
goal = [GRID_WIDTH-1, GRID_HEIGHT-1]

# Initialize Pygame
pygame.init()

# Set up some variables for the screen
WINDOW_SIZE = [GRID_WIDTH * WIDTH, GRID_HEIGHT * HEIGHT]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the window
pygame.display.set_caption("Maze Game")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Move the AI randomly
    direction = random.choice(['up', 'down', 'left', 'right'])
    if direction == 'up' and ai[1] > 0:
        ai[1] -= 1
    elif direction == 'down' and ai[1] < GRID_HEIGHT - 1:
        ai[1] += 1
    elif direction == 'left' and ai[0] > 0:
        ai[0] -= 1
    elif direction == 'right' and ai[0] < GRID_WIDTH - 1:
        ai[0] += 1

    # Check if the AI has reached the goal
    if ai == goal:
        done = True

    # Draw the grid
    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):
            color = WHITE
            if [column, row] == ai:
                color = BLUE
            elif [column, row] == goal:
                color = GREEN
            pygame.draw.rect(screen, color,
                             [WIDTH * column, HEIGHT * row, WIDTH, HEIGHT])

    # Limit frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()