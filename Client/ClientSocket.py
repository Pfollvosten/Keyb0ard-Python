import socket
import time
import threading

class ClientSocket:

    def __init__(self):
        # create TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # get the according IP address
        self.ip_address = "192.168.178.28"
        # bind the socket to the port 23456, and connect
        self.server_address = (self.ip_address, 8765)  

    def send_data(self, data):
        self.sock.connect(self.server_address)
        print ("connecting to %s" % (self.ip_address))

        for entry in data:
            print("data: %s" % entry)
            new_data = str(entry).encode("utf-8")
            self.sock.sendall(new_data)

        self.sock.close()
