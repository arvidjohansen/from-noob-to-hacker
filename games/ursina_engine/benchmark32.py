import pygame
import numpy as np
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
NUM_PARTICLES = 200
PARTICLE_RADIUS = 5
MAX_VELOCITY = 5
FORCE_TRANSFER_RATIO = 5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Generate initial positions, velocities, and forces for particles using NumPy
positions = np.random.rand(NUM_PARTICLES, 2) * np.array([WIDTH, HEIGHT])
velocities = (np.random.rand(NUM_PARTICLES, 2) - 0.5) * MAX_VELOCITY
forces = np.zeros((NUM_PARTICLES, 2))

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
    
    # Check for collisions between particles using NumPy
    for i in range(NUM_PARTICLES):
        for j in range(i + 1, NUM_PARTICLES):
            dx = positions[i, 0] - positions[j, 0]
            dy = positions[i, 1] - positions[j, 1]
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance < 2 * PARTICLE_RADIUS:
                # Collide particles
                normal_x = dx / distance
                normal_y = dy / distance
                tangent_x = -normal_y
                tangent_y = normal_x
                
                # Compute velocities along normal and tangent directions
                v1_normal = np.dot(velocities[i], [normal_x, normal_y])
                v1_tangent = np.dot(velocities[i], [tangent_x, tangent_y])
                v2_normal = np.dot(velocities[j], [normal_x, normal_y])
                v2_tangent = np.dot(velocities[j], [tangent_x, tangent_y])
                
                # Compute new velocities after collision
                velocities[i] = (1 - FORCE_TRANSFER_RATIO) * v1_normal * np.array([normal_x, normal_y]) + \
                                v2_normal * np.array([normal_x, normal_y]) + \
                                v1_tangent * np.array([tangent_x, tangent_y])
                velocities[j] = (1 - FORCE_TRANSFER_RATIO) * v2_normal * np.array([normal_x, normal_y]) + \
                                v1_normal * np.array([normal_x, normal_y]) + \
                                v2_tangent * np.array([tangent_x, tangent_y])
    
    # Draw particles
    for pos in positions:
        pygame.draw.circle(screen, (255, 255, 255), pos.astype(int), PARTICLE_RADIUS)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
