import keyboard
import threading
from time import sleep

class KeyboardController:
    print("hi")

    def __init__(self):
        file = open("./btnmap.txt" , "r")
        lines = file.readlines()

        for l in range(8):
            self.button_map[l] = lines[l]
        file.close()
    
    def write_button_map():
        file = open("./btnmap.txt" , "w")

    

    button_map = [
        "w",
        "a",
        "s",
        "d",
        "1",
        "2",
        "3",
        "4"
    ]

    def create_key_stroke(self, button_id):
        keyboard.parse_hotkey_combinations(self.button_map[button_id])