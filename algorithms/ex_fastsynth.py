import numpy as np
import pygame
import multiprocessing as mp

# Constants
SAMPLE_RATE = 44100
DURATION = 0.5  # Duration of each note in seconds
NUM_KEYS = 8  # Number of keys to handle
KEY_MAP = {'a': 'C3', 's': 'D3', 'd': 'E3', 'f': 'F3', 'g': 'G3', 'h': 'A3', 'j': 'B3', 'k': 'C4'}

# Precompute waveforms for each note
NOTES = {'C3': 130.81, 'D3': 146.83, 'E3': 164.81, 'F3': 174.61, 'G3': 196.00, 'A3': 220.00, 'B3': 246.94, 'C4': 261.63}

def generate_wave(frequency, duration):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    waveform = np.sin(2 * np.pi * frequency * t)
    return waveform

# Precompute waveforms for each note
WAVEFORMS = {note: generate_wave(frequency, DURATION) for note, frequency in NOTES.items()}

def play_sound(note):
    pygame.mixer.Sound(WAVEFORMS[note]).play()

def main():
    # Initialize Pygame
    pygame.init()

    # Start the sound mixer
    pygame.mixer.init(SAMPLE_RATE, -16, 1, 1024)

    # Create a dictionary to keep track of key states
    key_state = {key: False for key in KEY_MAP.keys()}

    # Create a pool of worker processes for parallel sound playback
    pool = mp.Pool(processes=NUM_KEYS)

    display = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Synthesizer')


    running = True
    while running:
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key in KEY_MAP:
                    key_state[key] = True
                    pool.apply_async(play_sound, (KEY_MAP[key],))
            elif event.type == pygame.KEYUP:
                key = pygame.key.name(event.key)
                if key in KEY_MAP:
                    key_state[key] = False
        
        # Draw the keyboard
        display.fill((255, 255, 255))
        for i, key in enumerate(KEY_MAP.keys()):
            color = (255, 0, 0) if key_state[key] else (0, 0, 0)
            pygame.draw.rect(display, color, (i * 80, 0, 80, 480))
        pygame.display.flip()


        pygame.display.update()

        # Check for quit condition
        #if all(not state for state in key_state.values()):
        #    running = False

    # Clean up
    pygame.quit()

if __name__ == "__main__":
    main()
