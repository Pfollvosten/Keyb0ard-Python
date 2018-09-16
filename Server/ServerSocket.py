# ServerSocket.py

import socket, pickle, threading

class ServerSocket(threading.Thread):

    HOST = '192.168.178.28'
    PORT = 50007

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        print("Server setup!")
        while True:
            s.listen(1)
            conn, addr = s.accept()
            print ('Connected by', addr)
            #receive the data and unpickle it
            data = conn.recv(4096)
            data_variable = pickle.loads(data)
            print ('Data received from client')
            read_data()
    except:
        print("Error")    
    finally:
        conn.close()

    def read_data(self, data):
        from MainServer import keyboard as key_controller
        
        for id in range(data.len()):
            if data[id]:
                key_controller.create_key_stroke(id)