# KeyboardController.py

### import and setup
import json
import keyboard
from blinkstick import blinkstick
led = blinkstick.find_first()
from yeelight import Bulb
bulb = Bulb("192.68.178.40")
from threading import Thread


def execute_key(btn_id):
    """
    execute previously saved keystroke recordings
    """
    with open('btnmap.json', encoding='utf-8') as file:
        data = json.load(file)
        key_data = data["btnmap"][btn_id]
        
        # Keyboard
        if key_data["key_comb"]:
            key = Thread(target=keyboard_exec , args=(key_data["key_comb"],))
            key.start()
        # # Yeelight
        # if key_data["yeelight"]:
        #     key = Thread(target=yeelight_exec , args=(key_data["yeelight"],))
        #     key.start()
        # #Blinkstick
        if key_data["blinkstick"]:
            key = Thread(target=blinkstick_exec , args=(key_data["blinkstick"],))
            key.start()
        
        file.close()


def keyboard_exec(key_comb):
    keyboard.send(key_comb)

def yeelight_exec(yee):
    bulb.turn_on()

def blinkstick_exec(blk):
    if blk["action"] == "pulse":
        led.pulse(red=blk["color"][0], green=blk["color"][1], blue=blk["color"][2])
    elif blk["action"] == "blink":
        pass