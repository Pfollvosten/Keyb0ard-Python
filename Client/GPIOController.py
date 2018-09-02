from gpiozero import Button
import threading
from time import sleep
import ClientSocket

class GPIOController:
    

    pressed_data = [
        #false , false , false , false , false , false , false , false
    ]

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
                    ClientSocket.send_data(pressed_data)
