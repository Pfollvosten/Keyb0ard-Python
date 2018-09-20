# GPIOReader.py

from threading import Thread
from gpiozero import Button
from time import sleep

class GPIOReader(Thread):

    def __init__(self):
        self.pressed = [False] * 8

        self.buttons = [
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
        sleep(0.01)
        while True:
            for but in range(len(self.buttons)):
                if self.buttons[but].is_pressed:
                    self.pressed[but] = True
                    
                    from MainClient import sock
                    sock.send_data(self.pressed_data)
                else:
                    self.pressed[but] = False

        # valid = None    # Tastenposition
        # invalid = 0     # Anzahl der invalid Tasten
        # cnt = 0         # for-Zaehler
        # state = 0       # Status
        # while True:
        #     invalid = 0
        #     cnt = 0
        #     for x in buttons:
        #         # Vier Zustaende pruefen
        #         if state == 0:
        #             print("state 0")
        #         # state 0 Keine Taste gedrueckt
        #         if x.is_pressed:
        #             # Taste gedrueckt, das ist die valid Taste
        #             valid = x.pin
        #             state = 1
        #         elif state == 1:
        #             print("state 1")
        #         # state 1 EINE valid-Taste gedrueckt, keine invalid Taste gedrueckt
        #         if x.is_pressed and x.pin == valid and invalid == 0:
        #             # valid gedrueckt, kein invalid, unveraendert
        #             state = 1
        #         elif not x.is_pressed and x.pin == valid and invalid == 0:
        #             # valid losgelssen, kein invalid
        #             valid = None
        #             state = 0
        #         elif x.is_pressed and x.pin != valid:
        #             # valid immer noch gedrueckt (abernicht diese Taste), plus invalid
        #             invalid = invalid + 1
        #             state = 2