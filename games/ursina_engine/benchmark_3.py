import pygame
import random
import math

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
particles = [{'position': (random.randint(0, WIDTH), random.randint(0, HEIGHT)),
              'velocity': (random.uniform(-MAX_VELOCITY, MAX_VELOCITY), random.uniform(-MAX_VELOCITY, MAX_VELOCITY))}
             for _ in range(NUM_PARTICLES)]

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update particle positions
    for particle in particles:
        particle['position'] = (particle['position'][0] + particle['velocity'][0],
                                particle['position'][1] + particle['velocity'][1])
    
    # Check for collisions with walls and update velocities
    for particle in particles:
        if particle['position'][0] < 0 or particle['position'][0] > WIDTH:
            particle['velocity'] = (-particle['velocity'][0], particle['velocity'][1])
        if particle['position'][1] < 0 or particle['position'][1] > HEIGHT:
            particle['velocity'] = (particle['velocity'][0], -particle['velocity'][1])
    
    # Check for collisions between particles
    for i in range(NUM_PARTICLES):
        for j in range(i + 1, NUM_PARTICLES):
            dx = particles[i]['position'][0] - particles[j]['position'][0]
            dy = particles[i]['position'][1] - particles[j]['position'][1]
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance < 2 * PARTICLE_RADIUS:
                # Collide particles
                normal_x = dx / distance
                normal_y = dy / distance
                tangent_x = -normal_y
                tangent_y = normal_x
                
                # Compute velocities along normal and tangent directions
                v1_normal = normal_x * particles[i]['velocity'][0] + normal_y * particles[i]['velocity'][1]
                v1_tangent = tangent_x * particles[i]['velocity'][0] + tangent_y * particles[i]['velocity'][1]
                v2_normal = normal_x * particles[j]['velocity'][0] + normal_y * particles[j]['velocity'][1]
                v2_tangent = tangent_x * particles[j]['velocity'][0] + tangent_y * particles[j]['velocity'][1]
                
                # Compute new velocities after collision
                particles[i]['velocity'] = (v2_normal * normal_x + v1_tangent * tangent_x,
                                            v2_normal * normal_y + v1_tangent * tangent_y)
                particles[j]['velocity'] = (v1_normal * normal_x + v2_tangent * tangent_x,
                                            v1_normal * normal_y + v2_tangent * tangent_y)
    
    # Draw particles
    for particle in particles:
        pygame.draw.circle(screen, (255, 255, 255), (int(particle['position'][0]), int(particle['position'][1])), PARTICLE_RADIUS)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
