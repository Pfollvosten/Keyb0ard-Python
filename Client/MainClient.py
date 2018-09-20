# MainClient.py

from ClientSocket import ClientSocket
sock = ClientSocket()
sock.setName("t_sock")
sock.start()

from GPIOReader import GPIOReader
gpio = GPIOReader()