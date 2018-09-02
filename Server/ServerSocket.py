import socket
import KeybaordController
import threading

class ServerSocket:

    #def __init__(self):
        #create TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #get server hostname
        local_hostname = socket.gethostname()
        #get fully qualified hostname
        local_fqdn = socket.getfqdn()
        #get the according IP adress
        ip_adress = socket.gethostbyname(local_hostname)
        #output setup message
        print("working on %s (%s) with %s" % (local_hostname, local_fqdn , ip_adress))
        #bind the socket to port 8765
        server_adress = (ip_adress , 8765)
        print("starting up on %s port %s" % server_adress)
        sock.bind(server_adress)

        #listen for one incoming connection at a time
        sock.listen(1)

    #   run_server_forever()

    #def run_server_forever():

        #wait for a connection
        print("waiting for a connection")
        connection , client_adress = sock.accept()

        try:
            #show who connected
            print("connection from ", client_adress)
            #recv the data in small chunks and print it
            while True:
                data = sock.recv(1024)
                if data:
                    #output recv data
                    print("DATA: %s" % data)
                else:
                    #no more data -- quit the loop
                    print("no more data.")
                    break
        finally:
            #cloean up the connection
            connection.close()