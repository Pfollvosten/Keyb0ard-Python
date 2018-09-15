import socket
import time
import threading

class ClientSocket(threading.Thread):

    def __init__(self, port, ip):
        # create TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # get the according IP address "192.168.178.28"
        self.ip_address = ip
        # bind the socket to the port, and connect
        self.server_address = (self.ip_address, port)

        self.send_data("YEEET")

    def send_data(self, data):
        try:
            self.sock.connect(self.server_address)
            print ("connecting to %s" % (self.ip_address))
            self.sock.send(data)
        except:
            print("ERROR")
        finally:
            self.sock.close()