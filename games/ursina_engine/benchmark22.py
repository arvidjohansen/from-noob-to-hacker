import pygame
import numpy as np
import random

# Constants
WIDTH, HEIGHT = 800, 600
NUM_PARTICLES = 100
PARTICLE_RADIUS = 5
MAX_VELOCITY = 5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Generate initial positions and velocities for particles using NumPy
positions = np.random.rand(NUM_PARTICLES, 2) * np.array([WIDTH, HEIGHT])
velocities = (np.random.rand(NUM_PARTICLES, 2) - 0.5) * MAX_VELOCITY

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update particle positions using NumPy
    positions += velocities
    
    # Check for collisions with walls and update velocities using NumPy
    out_of_bounds = np.logical_or(positions < 0, positions > np.array([WIDTH, HEIGHT]))
    velocities[out_of_bounds] *= -1
    
    # Draw particles
    for pos in positions:
        pygame.draw.circle(screen, (255, 255, 255), pos.astype(int), PARTICLE_RADIUS)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
