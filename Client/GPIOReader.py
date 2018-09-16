import threading
from MainClient import client_sock

class GPIOReader(threading.Thread):
    
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

    client_sock.send_data(pressed_data)