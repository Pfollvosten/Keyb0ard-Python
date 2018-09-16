# ClientSocket.py

import socket, pickle, threading

class ClientSocket(threading.Thread):

    HOST = '192.168.178.28'
    PORT = 50007

    def send_data(self, data):
        try:
            # Create a socket connection.
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.HOST, self.PORT))
            # Pickle the object and send it to the server
            data_string = pickle.dumps(data)
            s.send(data_string)
        except:
            print("Error")
        finally:
            s.close()
            print ('Data Sent to Server')