# ServerSocket.py

import socket, pickle
from threading import Thread

class ServerSocket(Thread):

    HOST = '192.168.178.28'
    PORT = 50007

    def run(self):
        Thread.daemon = True
        Thread.start(self)


        try:
            # create socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.HOST, self.PORT))
            print("Server setup!")
            while True:
                # listen for and accept 1 incoming connection
                s.listen(1)
                conn, addr = s.accept()
                print ('Connected by', addr)
                #receive the data and unpickle it
                data_binary = conn.recv(4096)
                data_variable = pickle.loads(data_binary)
                print ('Data received from client')
                # Analyze the pressed keys and trigger according keys
                self.read_data(data_variable)
        except:
            print("Error")
        finally:
            conn.close()

    def read_data(self, data):
        from MainServer import keyboard as key_controller
        
        for id in range(data.len()):
            if data[id]:
                key_controller.create_key_stroke(id)