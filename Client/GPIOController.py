from gpiozero import Button
import threading
from time import sleep

class GPIOController(threading.Thread):
    
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

    buttons = [
        Button(26),
        Button(19),
        Button(13),
        Button(6),
        Button(21),
        Button(20),
        Button(16),
        Button(12),
    ]

    def read_input_forever(self):
        while True:
            for x in self.buttons:
                if x.ispressed:
                    print("pressed ", x.pin)
                    ClientSocket.client_sock.send_data(self.pressed_data)