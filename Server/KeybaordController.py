import keyboard
import threading
from time import sleep

class KeyboardController:
    
    button_map = []
    
    def __init__(self):
        try:
            file = open("./btnmap.txt" , "r")
            lines = file.readlines()

            for l in range(8):
                self.button_map[l] = lines[l]
        finally:
            file.close()
    
    def create_key_stroke(self, button_id):
        keyboard.parse_hotkey_combinations(self.button_map[button_id])

    def read_key_input(self, button_id):
        self.button_map[button_id] = keyboard.read_hotkey
    
    def write_button_map(self):
        try:
            file = open("./btnmap.txt" , "w")
            file.writelines(self.button_map)
        finally:
            file.close()