import pygame
import numpy as np

# Define the properties of the sound
sample_rate = 44100  # Hertz
duration = 1.0  # seconds
frequency = 440.0  # Hertz

# Generate the time array
#t = np.arange(int(sample_rate * duration)) / sample_rate

def sine(frequency, t, sample_rate=sample_rate) -> np.ndarray:
    # samples = (np.sin(2 * np.pi * np.arange(sample_rate * duration) * frequency / sample_rate)).astype(np.float32)
    # t = np.arange(int(sample_rate * duration)) / sample_rate
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    wave = (wave * 32767).astype(np.int16)

    yield wave

# Generate the sine wave
# wave = 0.5 * np.sin(2 * np.pi * frequency * t)


# Convert to 16-bit PCM
# wave = (wave * 32767).astype(np.int16)

# Initialize the mixer
pygame.mixer.init(sample_rate, -16, 1, 512)

# Create a Sound object
sound = pygame.mixer.Sound(wave)

# Play the sound
sound.play()