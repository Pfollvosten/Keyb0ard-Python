import socket
import threading
import time

class ServerSocket(threading.Thread):

    def __init__(self, port):
        #create TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #get server hostname
        local_hostname = socket.gethostname()
        #get fully qualified hostname
        local_fqdn = socket.getfqdn()
        #get the according IP adress
        ip_adress = socket.gethostbyname(local_hostname)
        #output setup message
        print("working on %s (%s) with %s" % (local_hostname, local_fqdn , ip_adress))
        #bind the socket to port
        server_adress = (ip_adress , port)
        print("starting up on %s port %s" % server_adress)
        self.sock.bind(server_adress)
    
        self.run_server()

    def run_server(self):    
        #listen for one incoming connection at a time
        self.sock.listen(1)
        #wait for a connection
        print("waiting for a connection")

        try:
            connection , client_adress = self.sock.accept()
            #show who connected
            print("connection from ", client_adress)
            #recv the data in small chunks and print it
            while True:
                data = self.sock.recv(1024)
                if data:
                    #output recv data
                    print("DATA: %s" % data)
                else:
                    #no more data -- quit the loop
                    print("no more data.")
                    break
        except:
            print("ERROR")
        finally:
            #cloean up the connection
            connection.close()