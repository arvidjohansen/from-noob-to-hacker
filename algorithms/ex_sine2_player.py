import pygame
import numpy as np

# Define the properties of the sound
sample_rate = 44100  # Hertz
duration = 1.0  # seconds
frequency = 440.0  # Hertz

def generate_sine_wave(frequency, duration, sample_rate):
    # Generate the time array
    t = np.arange(int(sample_rate * duration)) / sample_rate

    # Generate the sine wave
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    # Convert to 16-bit PCM
    wave = (wave * 32767).astype(np.int16)

    return wave

# Initialize Pygame and its mixer
pygame.init()
pygame.mixer.init(sample_rate, -16, 1)

sound = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # When a key is pressed, generate a sine wave and play it
            wave = generate_sine_wave(frequency, duration, sample_rate)
            sound = pygame.mixer.Sound(wave)
            sound.play(-1)  # Play the sound indefinitely
        elif event.type == pygame.KEYUP:
            # When the key is released, stop playing the sound
            if sound is not None:
                sound.stop()
    # pygame.update()

pygame.quit()