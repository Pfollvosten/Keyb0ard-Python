import ClientSocket
import GPIOController

gpio = GPIOController.GPIOController()
client_sock = ClientSocket.ClientSocket(8187 , "192.168.178.28")