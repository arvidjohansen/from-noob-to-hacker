# server.py
import socket
import threading

SERVER_HOST = "0.0.0.0"  # Listen on all available interfaces
SERVER_PORT = 7789
BUFFER_SIZE = 1024

clients = []  # Store client connections
grid = [[None for _ in range(100)] for _ in range(100)]  # Initialize the game grid


def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(BUFFER_SIZE)
            if data:
                # Broadcast the received data to all clients
                for c in clients:
                    c.send(data)
        except Exception as e:
            print(f"Exception: {e}")
            break


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    start_server()
