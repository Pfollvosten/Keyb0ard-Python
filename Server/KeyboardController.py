# KeyboardController.py

import keyboard
import threading
import json
from time import sleep

class KeyboardController(threading.Thread):
    
    button_map = [list()] * 8

    def read_key_input(self, button_id):
        """
        records all keystrokes done until the user presses escape.
        """
        hotkey = keyboard.record(until='escape', suppress=False, trigger_on_release=False)
        self.button_map[button_id] = hotkey
        return "TBI"

    def create_key_stroke(self, button_id):
        """
        execute previously saved keystroke recordings
        """
        keyboard.play(self.button_map[button_id], speed_factor=0)

    def read_btnmap(self):
        """
        read button assignments from btnmap.json and assign it to var self.button_map (list)*8
        """
        print("TBI")

    def write_btnmap(self):
        print("TBI")