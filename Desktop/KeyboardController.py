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
        # Keyboard ### if not empty nor deactivated
        if key_data["key_comb"] and data["settings"]["active-mods"]["keyboard"]:
            keyboard_exec(key_data["key_comb"])
        # Yeelight ### if not empty nor deactivated
        if key_data["yeelight"] and data["settings"]["active-mods"]["yeelight"]:
            yeelight_exec(key_data["yeelight"])
        #Blinkstick ### if not empty nor deactivated
        if key_data["blinkstick"] and data["settings"]["active-mods"]["blinkstick"]:
            blinkstick_exec(key_data["blinkstick"])
        
        file.close()

# decorator for runnning in thread
def run_in_thread(fn):
    def run(*k, **kw):
        t = Thread(target=fn, args=k, kwargs=kw)
        t.start()
    return run

@run_in_thread
def keyboard_exec(key_comb):
    keyboard.send(key_comb)

@run_in_thread
def yeelight_exec(yee):
    bulb.turn_on()
    bulb.set_rgb(yee["color"][0], yee["color"][1], yee["color"][2])

@run_in_thread
def blinkstick_exec(blk):
    if blk["action"] == "pulse":
        led.pulse(red=blk["color"][0], green=blk["color"][1], blue=blk["color"][2])
    elif blk["action"] == "color":
        led.set_color(red=blk["color"][0], green=blk["color"][1], blue=blk["color"][2])