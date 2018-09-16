# MainServer.py

from KeyboardController import KeyboardController
keyboard = KeyboardController()
keyboard.start()

from ServerSocket import ServerSocket
server_sock = ServerSocket()
server_sock.start()

from GUI import GUI
gui = GUI()
server_sock.start()