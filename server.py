import socket
import threading


class Server:
    SERVER = socket.gethostbyname(socket.gethostname())
    PORT = 10000
    ENCODING = 'utf-8'
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        self.socket.bind((self.SERVER, self.PORT))
        print("Server is staring...")
        self.socket.listen(1)
        print("Listening...")

    def run(self):
        while True:
            conn, addr = self.socket.accept()
            conn.send(bytes('***** Welcome to chat-room *****\n', self.ENCODING))
            conn.send(bytes('What is your name?', self.ENCODING))
            client_name = conn.recv(64).decode(self.ENCODING)
            while True:
                if not self.name_exists(client_name):
                    break
                conn.send(
                    bytes('That name already exists, please pick another one', self.ENCODING))
                client_name = conn.recv(64).decode(self.ENCODING)
            cThread = threading.Thread(target=self.handler, args=(conn, addr))
            cThread.daemon = True
            cThread.start()
            print(f"{client_name} connected")
            self.connections.append((conn, client_name))

    def handler(self, client, address):
        user_connected = True
        while user_connected:
            try:
                data = client.recv(64)
                message = data.decode(self.ENCODING)
                message = f'[{self.client_name(client)}] {message}'
                print(message)
                data = message.encode(self.ENCODING)
                for connection in self.connections:
                    conn, name = connection
                    if conn is not client:
                        conn.send(data)
                if not data:
                    break
            except ConnectionError:
                user_connected = False
                print(
                    f'[SERVER] Client {self.client_name(client)} disconnected! ')

    def client_name(self, connection):
        for client in self.connections:
            conn, name = client
            if conn is connection:
                return name

    def name_exists(self, name):
        for connection in self.connections:
            conn, username = connection
            if username == name:
                return True
        return False


server = Server()
server.run()
