# GPIOReader.py

from gpiozero import Button

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

def read_keys():
    """
    scanning every button if pressed. Gets called from ClientSocket.run
    """
    for but in range(len(buttons)):
        if buttons[but].is_pressed:
            pressed[but] = True
            print("pressed button: " , but)
        else:
            pressed[but] = False
    return pressed

# def read_keys(self):
#     import random
#     ran = random.randint(0,7)
#     self.pressed = [False] * 8
#     self.pressed[ran] = True
#     return self.pressed