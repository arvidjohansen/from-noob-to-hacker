import math
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
SQUARE_HEIGHT = 100 # pixels per square
SQUARE_WIDTH = 100 # pixels per square
WIDTH = SQUARE_WIDTH * 10
HEIGHT = SQUARE_HEIGHT * 10
FPS = 10  # Frames per second
SPEED = 100  # Speed of the object

WHITE = (255,255,255) # player
BLACK = (0,0,0) # background

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the player
player_pos = [WIDTH // 2, HEIGHT // 2]

# Set up the clock
clock = pygame.time.Clock()

def draw_background():
    screen.fill(BLACK)  # Fill the screen with black

def draw_player():
    pygame.draw.rect(screen, WHITE, pygame.Rect(player_pos[0], player_pos[1], SQUARE_HEIGHT,SQUARE_WIDTH))  # Draw the object
    font = pygame.font.Font(None, 36)
    

def handle_movement(keys):
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= SPEED
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - SQUARE_WIDTH:
        player_pos[0] += SPEED  
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= SPEED
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - SQUARE_HEIGHT:
        player_pos[1] += SPEED
def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Object movement
    keys = pygame.key.get_pressed()
    handle_movement(keys)
# Game loop
while True:
    handle_input()
    draw_background()
    draw_player()
    pygame.display.flip()
    clock.tick(FPS)