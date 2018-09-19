# GPIOReader.py

from threading import Thread
from MainClient import client_sock
from gpiozero import Buttons

class GPIOReader(threading.Thread):
    
    pressed_data = {
        1: False,
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False
    }

    buttons = [Buttons(16) * 8]

    client_sock.send_data(pressed_data)

    def run(self):
        for but in range(self.buttons.len):
            if self.buttons[but].ispressed:
                self.pressed_data[but] = True
