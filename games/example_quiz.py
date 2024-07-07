import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 54

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font for displaying the letter
font = pygame.font.Font(None, FONT_SIZE)

# Game is started when first letter is pressed

is_started = False

# The current letter the user needs to type
current_letter = 'A'

# The time the game started
start_time = time.time()


def draw_elapsed_time():
    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Render the elapsed time
    # format elapsed_time to 2 decimal places

    # time_image = font.render("{:.2f}".format(elapsed_time), True, TEXT_COLOR)
    if is_started:
        time_image = font.render("{:.2f}".format(elapsed_time), True, TEXT_COLOR)
    else:
        time_image = font.render("Ready? Start typing to begin", True, TEXT_COLOR)
    # Draw the elapsed time
    screen.blit(time_image, (0, 0))


def start_timer():
    # Start the timer
    global start_time
    start_time = time.time()


def draw_letter():
    # Render the letter
    letter_image = font.render(current_letter, True, TEXT_COLOR)

    # Calculate the position to center the letter on the screen
    x = (WIDTH - letter_image.get_width()) / 2
    y = (HEIGHT - letter_image.get_height()) / 2

    # Draw the letter
    screen.blit(letter_image, (x, y))

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Check if the key pressed was the current letter
            if not is_started:
                start_timer()
                is_started = True
            if event.unicode.upper() == current_letter:
                # Move on to the next letter
                current_letter = chr(ord(current_letter) + 1)
                if current_letter > 'Z':
                    # The user has typed all the letters, so end the game
                    end_time = time.time()
                    print('Time taken:', end_time - start_time)
                    pygame.quit()
                    sys.exit()

    # Fill the background
    screen.fill(BACKGROUND_COLOR)

    # Draw the current letter
    draw_letter()
    draw_elapsed_time()

    # Flip the display
    pygame.display.flip()