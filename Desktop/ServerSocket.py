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
            self.sock.listen(1)
            print("Waiting for connection...")
            conn, addr = self.sock.accept()
            print ('Connected by', addr)
            while True:
                #receive the data and unpickle it
                data_binary = conn.recv(1024)
                data_variable = pickle.loads(data_binary)
                print ('Data received from client. Data is: \n', data_variable)
                
                self.read_data(data_variable)
        except:
            print("Server Error")
        finally:
            print("Server shutdown")
            conn.close()

    def read_data(self, data):
        """
        Analyze the pressed keys and trigger according keys
        """
        from MainServer import key_controller
        
        for id in range(len(data)):
            if data[id]:
                key_controller.create_key_stroke(id)