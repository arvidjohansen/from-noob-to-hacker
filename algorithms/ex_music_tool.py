# using pygame, its integrated audio module, and the keyboard to create a simple music tool.
# uses numpy to generate a sine wave and pygame to play it.

import pygame
import numpy as np
import sys
import time

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BACKGROUND_COLOR = (0, 0, 0)
SQUARE_COLOR = (255, 255, 255)
SQUARE_SIZE = 50

# Audio constant
SAMPLE_RATE = 44100
DURATION = 1.0 


# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def sine(frequency, duration, sample_rate=SAMPLE_RATE) -> np.ndarray:
    
    # samples = (np.sin(2 * np.pi * np.arange(sample_rate * duration) * frequency / sample_rate)).astype(np.float32)
    samples = np.sin(2 * np.pi * np.arange(sample_rate * duration) * frequency / sample_rate).astype(np.int32)
    # make the sound stereo
    # samples = np.array([samples, samples]).T.astype(np.float32)
    print(samples.shape)
    samples = np.ascontiguousarray([samples,samples]).T
    # samples = np.asarray([samples,samples]).T.astype(np.float32)
    return samples 

def square(frequency, duration, sample_rate=SAMPLE_RATE) -> np.ndarray:
    samples = (np.sign(np.sin(2 * np.pi * np.arange(sample_rate * duration) * frequency / sample_rate))).astype(np.float32)
    return samples

def square(frequency, duration, sample_rate=SAMPLE_RATE) -> np.ndarray:
    samples = (np.sign(np.sin(2 * np.pi * np.arange(sample_rate * duration) * frequency / sample_rate))).astype(np.float32)
    return np.ascontiguousarray(samples)

def to_sound(samples) -> pygame.mixer.Sound:
    sound = pygame.sndarray.make_sound(samples)
    return sound

def play_sound(frequency, duration):
    sound = to_sound(sine(frequency, duration))
    sound.play()


while True:
    # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        play_sound(440, 1)
    if keys[pygame.K_2]:
        play_sound(880, 1)