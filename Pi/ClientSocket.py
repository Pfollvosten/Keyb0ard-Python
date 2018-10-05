# ClientSocket.py

import socket, pickle
from threading import Thread
from time import sleep

HOST = '192.168.178.28'
PORT = 50007

def run_in_thread(fn):
    def run(*k, **kw):
        t = Thread(target=fn, args=k, kwargs=kw)
        t.start()
    return run

@run_in_thread
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