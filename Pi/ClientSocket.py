# ClientSocket.py

import socket, pickle
from threading import Thread
from time import sleep

class ClientSocket:

    HOST = '192.168.178.28'
    PORT = 50007

    def run_as_thread(self, func):
        def wrap(data):
            t = Thread(self, target=func , args=data)
            t.setName("t_client_send")
            t.start()
        return wrap

    @run_as_thread
    def send_data(self , data):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.HOST, self.PORT))
            data_bin = pickle.dumps(data)
            self.sock.send(data_bin)
            # print("Data sent")
        except:
            print("client send error")
        finally:
            self.sock.close()