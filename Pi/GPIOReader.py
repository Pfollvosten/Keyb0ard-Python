# GPIOReader.py

from gpiozero import Button
buttons = [
    [Button(26, bounce_time=0.5), False, 0],
    [Button(19, bounce_time=0.5), False, 0],
    [Button(13, bounce_time=0.5), False, 0],
    [Button(6, bounce_time=0.5),  False, 0],
    [Button(21, bounce_time=0.5), False, 0],
    [Button(20, bounce_time=0.5), False, 0],
    [Button(16, bounce_time=0.5), False, 0],
    [Button(12, bounce_time=0.5), False, 0]
]

def read_keys():
    """
    scanning every button if pressed. Gets called from ClientSocket.run()
    """
    for b in buttons:
        # send out 1 stroke then block it for 300ms
        if b[0].is_pressed:
        #     if b[2] == 0:
            b[1] = True
        #     elif b[1]:
        #         print("blocking....")
        #         b[1] = False
        #         b[2] += 1
        #         if b[2] >= 30:
        #             ("more than 300ms")
        #             b[1] = True
        else:
            b[1] = False
        #     b[2] = 0
    # return pressed state for every button as a list            
    return list([bu[1] for bu in buttons])