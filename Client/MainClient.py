# MainClient.py

from ClientSocket import ClientSocket
sock = ClientSocket()

from GPIOReader import GPIOReader
gpio = GPIOReader()
gpio.start()