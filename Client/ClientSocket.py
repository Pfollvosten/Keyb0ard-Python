# ClientSocket.py

import socket, pickle, threading

class ClientSocket(threading.Thread):

    HOST = '192.168.178.28'
    PORT = 50007

    def __init__(self):
        # Create a socket connection.
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def send_data(self, data):
        try:
            self.sock.connect((self.HOST, self.PORT))
            # Pickle the object and send it to the server
            data_string = pickle.dumps(data)
            self.sock.send(data_string)
        except:
            print("Error")
        finally:
            self.sock.close()
            print ('Data Sent to Server')