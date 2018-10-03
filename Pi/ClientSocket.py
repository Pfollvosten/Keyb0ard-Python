# ClientSocket.py

import socket, pickle
from threading import Thread
from time import sleep

HOST = '192.168.178.28'
PORT = 50007

def run_as_thread(func):
    def wrap(data):
        t = Thread(target=func , args=data)
        t.setName("t_client_send")
        t.start()
    return wrap

@run_as_thread
def send_data(data):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        data_bin = pickle.dumps(data)
        sock.send(data_bin)
        # print("Data sent")
    except:
        print("client send error")
    finally:
        sock.close()