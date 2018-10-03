# GPIOReader.py

from threading import Thread
from time import sleep

class GPIOReader(Thread):

    from gpiozero import Button

    buttons = [
        [Button(26), False, 0],
        [Button(19), False, 0],
        [Button(13), False, 0],
        [Button(6),  False, 0],
        [Button(21), False, 0],
        [Button(20), False, 0],
        [Button(16), False, 0],
        [Button(12), False, 0]
    ]

    def run(self):
        """
        scanning every button - 100x/s
        """
        sleep(0.01)

        for b in self.buttons:
            # send out 1 stroke then block it for 300ms
            if b[0].is_pressed:
                if b[2] == 0 and not b[1]:
                    b[1] = True
                else:
                    b[1] = False
                    b[2] += 1
                    if b[2] >= 30:
                        b[1] = True
            else:
                b[1] = False
                b[2] = 0
                
        # return pressed state for every button as a list  
        from ClientSocket import send_data   
        send_data([bu[1] for bu in self.buttons])