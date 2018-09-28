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
    ret = []
    for but in range(len(buttons)):
        with buttons[but] as b:
            # send out 1 stroke then block it for 300ms
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
            ret.append(b[1])
    ret = list(ret)
    print(ret)
    return ret
    # return list([b[1] for b in buttons])
    
# def read_keys():
#     """
#     scanning every button if pressed. Gets called from ClientSocket.run
#     """
#     for but in range(len(buttons)):
#         if buttons[but].is_pressed:
#             pressed[but] = True
#             print("pressed button: " , but)
#         else:
#             pressed[but] = False
#     return pressed