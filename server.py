import socket
import threading


class Server:
    SERVER = socket.gethostbyname(socket.gethostname())
    PORT = 10000
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        self.socket.bind((self.SERVER, self.PORT))
        self.socket.listen(1)

    def handler(self, client, address):
        while True:
            data = client.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                break

    def run(self):
        while True:
            print("[SERVER] Staring...")
            print("[SERVER] Listening...")
            conn, addr = self.socket.accept()
            cThread = threading.Thread(target=self.handler, args=(conn, addr))
            cThread.daemon = True
            cThread.start()
            self.connections.append(conn)


server = Server()
server.run()
