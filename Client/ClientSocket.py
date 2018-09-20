# ClientSocket.py

import socket, pickle
from threading import Thread
from time import sleep

class ClientSocket(Thread):

    HOST = '192.168.178.28'
    PORT = 50007

    def __init__(self):
        # Create a socket connection.
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        super(ClientSocket, self).__init__()

    def run(self):
        try:
            from MainClient import gpio

            self.sock.connect((self.HOST, self.PORT))
            while True:
                sleep(0.05)
                data = gpio.read_keys()
                data_bin = pickle.dumps(data)
                self.sock.send(data_bin)
                print("Data sent to Server")
        except:
            print("client")
        finally:
            self.sock.close()