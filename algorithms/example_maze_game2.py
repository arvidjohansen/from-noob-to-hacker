import pygame

# Define constants for the width and height of each grid location
WIDTH = 20 * 5
HEIGHT = 20 * 5

# Define some colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)

# Define the maze
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

# Define the AI and goal
ai = [0, 9]
goal = [9, 9]
start = ai.copy()

# Define the AI's direction (0=up, 1=right, 2=down, 3=left)
direction = 1

# Initialize Pygame
pygame.init()

# Set up some variables for the screen
WINDOW_SIZE = [len(maze[0]) * WIDTH, len(maze) * HEIGHT]
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

    # Move the AI
    for _ in range(4):
        dx, dy = 0, 0
        if direction == 0:  # up
            dy = -1
        elif direction == 1:  # right
            dx = 1
        elif direction == 2:  # down
            dy = 1
        elif direction == 3:  # left
            dx = -1
    
        new_x, new_y = ai[0] + dx, ai[1] + dy
        if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] == 0:
            ai[0] = new_x
            ai[1] = new_y
            break
    
        # If we can't move in the current direction, turn left
        print(direction) 
        direction = (direction - 1) % 4
        #direction = (direction - 1)

    # Check if the AI has reached the goal
    if ai == goal:
        done = True

    # Draw the maze
    for row in range(len(maze)):
        for column in range(len(maze[0])):
            color = WHITE if maze[row][column] == 0 else BLACK
            if [column, row] == ai:
                color = BLUE
            elif [column, row] == goal:
                color = GREEN
            elif [column, row] == start:
                color = RED
            pygame.draw.rect(screen, color,
                             [WIDTH * column, HEIGHT * row, WIDTH, HEIGHT])

    # Limit frames per second
    clock.tick(30)

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()