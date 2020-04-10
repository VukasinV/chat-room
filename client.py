import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.8"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# sends message to the server


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send("Hello world")
chat = True
while chat:
    print("Message (to cancel type 'xx'): ")
    message_to_send = input()
    if message_to_send == 'xx':
        chat = False
        break
        print("You have exited the chat")
    send(message_to_send)
