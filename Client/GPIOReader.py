# GPIOReader.py

from threading import Thread
from gpiozero import Button
from time import sleep

class GPIOReader(Thread):

    pressed = [False] * 8

    buttons = [
        Button(26),
        Button(19),
        Button(13),
        Button(6),
        Button(21),
        Button(20),
        Button(16),
        Button(12)
        ]

    def run(self):
        from MainClient import sock
        while True:
            sleep(0.05)     # Scanning 20 times/s for input
            # scanning every button 
            for but in range(len(self.buttons)):
                if self.buttons[but].is_pressed:
                    self.pressed[but] = True
                    print("pressed button: " , but)
                else:
                    self.pressed[but] = False
            sock.send_data(self.pressed_data)