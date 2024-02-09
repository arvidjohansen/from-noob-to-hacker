import pygame
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
positions = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_PARTICLES)]
velocities = [(random.uniform(-MAX_VELOCITY, MAX_VELOCITY), random.uniform(-MAX_VELOCITY, MAX_VELOCITY)) for _ in range(NUM_PARTICLES)]

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update particle positions
    for i in range(NUM_PARTICLES):
        positions[i] = (positions[i][0] + velocities[i][0], positions[i][1] + velocities[i][1])
    
    # Check for collisions with walls and update velocities
    for i in range(NUM_PARTICLES):
        if positions[i][0] < 0 or positions[i][0] > WIDTH:
            velocities[i] = (-velocities[i][0], velocities[i][1])
        if positions[i][1] < 0 or positions[i][1] > HEIGHT:
            velocities[i] = (velocities[i][0], -velocities[i][1])
    
    # Draw particles
    for position in positions:
        pygame.draw.circle(screen, (255, 255, 255), (int(position[0]), int(position[1])), PARTICLE_RADIUS)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
