import socket
import threading


class Client:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        print("[CLIENT] Starting...")
        self.socket.connect(('192.168.1.8', 10000))
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        while True:
            data = self.socket.recv(1024)
            if not data:
                break
            print(data)

    def sendMsg(self):
        while True:
            self.socket.send(bytes(input(""), 'utf-8'))


client = Client()
