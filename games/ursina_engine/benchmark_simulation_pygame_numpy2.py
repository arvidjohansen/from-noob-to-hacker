import pygame
import numpy as np
import random

# Constants
WIDTH, HEIGHT = 800, 600
NUM_PARTICLES = 1000
PARTICLE_RADIUS = 5
MAX_VELOCITY = 5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Generate initial positions and velocities for particles
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
    
    # Update particle positions
    positions += velocities
    
    # Check for collisions with walls and update velocities
    for i in range(NUM_PARTICLES):
        if positions[i, 0] < 0 or positions[i, 0] > WIDTH:
            velocities[i, 0] *= -1
        if positions[i, 1] < 0 or positions[i, 1] > HEIGHT:
            velocities[i, 1] *= -1
    
    # Draw particles
    for i in range(NUM_PARTICLES):
        pygame.draw.circle(screen, (255, 255, 255), (int(positions[i, 0]), int(positions[i, 1])), PARTICLE_RADIUS)
    
    pygame.display.flip()
    clock.tick(600)

pygame.quit()
