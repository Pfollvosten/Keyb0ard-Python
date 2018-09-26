# GPIOReader.py

from gpiozero import Button

pressed = [False] * 8
blocked = False
ticks_since = 0
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

# def read_keys():
#     """
#     scanning every button if pressed. Gets called from ClientSocket.run
#     """
#     ticks_since += 1 if blocked else ticks_since = 0

#     for but in range(len(buttons)):
#         if buttons[but].is_pressed and not blocked:
#             blocked = True
#             print("pressed button: " , but)
#             if ticks_since <= 250:
#                 blocked = True
#                 pressed[but] = True
#             if ticks_since >= 250 and ticks_since%50==0:
#                 pass
            
#         elif buttons[but].is_released:
#             pressed[but] = False
#             blocked = False
#     return pressed



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