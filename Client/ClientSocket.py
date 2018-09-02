import socket
import time
import threading

class ClientSocket:

    #def __init__(self):
        # create TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # get the according IP address
        ip_address = "192.168.178.28"
        # bind the socket to the port 23456, and connect
        server_address = (ip_address, 8765)  
        sock.connect(server_address)  
        print ("connecting to %s" % (ip_address))

        # define example data to be sent to the server
        temperature_data = ["15", "22", "21", "26", "25", "19"] 
        for entry in temperature_data:  
            print ("data: %s" % entry)
            new_data = str("temperature: %s\n" % entry).encode("utf-8")
            sock.sendall(new_data)

            # wait for two seconds
            time.sleep(2)
            

        # close connection
        sock.close()  


    def send_data(data)