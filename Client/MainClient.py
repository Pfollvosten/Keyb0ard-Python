# MainClient.py

from ClientSocket import ClientSocket
sock = ClientSocket()

from GPIOReader import GPIOReader
t_gpio = GPIOReader()
t_gpio.setName("t_gpio")
t_gpio.start()