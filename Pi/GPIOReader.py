# GPIOReader.py

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

def read_keys():
    """
    scanning every button if pressed. Gets called from ClientSocket.run()
    """
    for but in range(len(buttons)):
        # with buttons[but] as b:
        b = buttons[but]
        # send out 1 stroke then block it for 300ms
        if b[0].is_pressed:
            if b[2] == 0:
                b[1] = True
            elif b[1]:
                b[1] = False
                b[2] += 1
                if b[2] >= 30:
                    b[1] = True
        elif b[0].is_released:
            b[1] = False
            b[2] = 0
    # return pressed state for every button as a list            
    return list([bu[1] for bu in buttons])