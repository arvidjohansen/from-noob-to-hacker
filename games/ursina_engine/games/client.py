# client.py
import pygame
import socket
import threading

SERVER_HOST = "127.0.0.1"  # Change to the server's IP address
SERVER_PORT = 7789
BUFFER_SIZE = 1024

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
GRID_SIZE = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player_symbol = "😀"  # Change to your desired emoji

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(BUFFER_SIZE)
            if data:
                # Process received data (e.g., update game grid)
                pass
        except Exception as e:
            print(f"Exception: {e}")
            break


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Emoji Chat Game")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Draw the game grid
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            for x in range(0, SCREEN_WIDTH, GRID_SIZE):
                pygame.draw.rect(screen, BLACK, (x, y, GRID_SIZE, GRID_SIZE), 1)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
