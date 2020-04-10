import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# need to keep track of clients, which means it needs to be a list of clients
# clients = []


def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected")
    connected = True
    while connected:
        # why we do need to recieve a header? and length of a message???
        msg_length = connection.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = connection.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{address}] {msg}")

    connection.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(
            target=handle_client, args=(connection, address))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.activeCount() - 1}")

# TODO: send message to all clients: check if you can access threading arguments
# and send message to that connection


def send_message(message):
    pass


print("[STARTING] server is starting...")
start()
