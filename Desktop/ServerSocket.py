# ServerSocket.py

import socket, pickle
from threading import Thread

class ServerSocket(Thread):

    HOST = '192.168.178.28'
    PORT = 50007

    def __init__(self):
            # create socket object
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.HOST, self.PORT))
            print("Server setup!")
            super(ServerSocket, self).__init__()

    def run(self):
        try:
            # listen for and accept 1 incoming connection
            while True:
                self.sock.listen(1)
                print("Waiting for connection...")
                conn, addr = self.sock.accept()
                print ('Connected by', addr)
                #receive the data and unpickle it
                data_binary = conn.recv(1024)
                data_variable = pickle.loads(data_binary)
                # analyze and execute
                self.analyze_data(data_variable)
                conn.close()
        except:
            print("Server Error")
        finally:
            conn.close()
            print("Server shutdown")

    def analyze_data(self , data):
        for id in range(len(data)):
            if data[id]:
                from KeyboardController import execute_key
                execute_key(id)
                