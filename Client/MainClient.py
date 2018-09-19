# MainClient.py

from ClientSocket import ClientSocket
from GPIOReader import GPIOReader

client_sock = ClientSocket()

gpio = GPIOReader()
gpio.start()