# MainServer.py

from ServerSocket import ServerSocket
t_sock = ServerSocket()
t_sock.setName("t_sock")
t_sock.start()

from KeyboardController import KeyboardController
key_controller = KeyboardController()

# from GUI import GUI
# t_gui = GUI()
# t_gui.setName("t_gui")
# t_gui.start()