import socket
import threading

# TODO: Every server should ask clienct for their name


class Client:
    SERVER = socket.gethostbyname(socket.gethostname())
    ENCODING = 'utf-8'
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    PORT = 10000

    def __init__(self):
        print("[CLIENT] Starting...")
        self.socket.connect((self.SERVER, self.PORT))
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        try:
            while True:
                data = self.socket.recv(64)
                print(data.decode(self.ENCODING))
        except ConnectionResetError:
            print("Chat room was closed")
            exit()

    def sendMsg(self):
        while True:
            message = input("")
            self.socket.send(bytes(message, self.ENCODING))


client = Client()
