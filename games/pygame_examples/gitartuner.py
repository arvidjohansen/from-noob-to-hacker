import pygame
import pyaudio
import numpy as np

# Pygame initialization
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guitar Tuner")

# Pyaudio initialization
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)


def detect_frequency(data):
    # Convert audio input to numpy array
    audio_data = np.frombuffer(data, dtype=np.int16)

    # Compute the Fast Fourier Transform (FFT) of the audio data
    fft_data = np.fft.fft(audio_data)

    # Compute the frequencies corresponding to each FFT bin
    freqs = np.fft.fftfreq(len(fft_data), 1.0 / RATE)

    # Find the index of the peak frequency
    peak_index = np.argmax(np.abs(fft_data))

    # Convert the index to the corresponding frequency
    peak_freq = freqs[peak_index]

    # Convert frequency to note
    return frequency_to_note(peak_freq)


def frequency_to_note(frequency):
    # Map frequency to the nearest note
    notes = ["E", "A", "D", "G", "B", "E"]
    frequencies = [82.41, 110.00, 146.83, 196.00, 246.94, 329.63]
    min_index = np.argmin(np.abs(np.array(frequencies) - frequency))
    return notes[min_index]


def draw_text(text, x, y, font_size=36):
    font = pygame.font.SysFont(None, font_size)
    rendered_text = font.render(text, True, (255, 255, 255))
    screen.blit(rendered_text, (x, y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    data = stream.read(CHUNK)
    note = detect_frequency(data)

    screen.fill((0, 0, 0))
    draw_text("Guitar Tuner", 10, 10)
    draw_text("Detected Note: {}".format(note), 10, 50)
    pygame.display.flip()

pygame.quit()
stream.stop_stream()
stream.close()
audio.terminate()
