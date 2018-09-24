# GUI.py

from guizero import App, PushButton
from threading import Thread

class GUI(Thread):

    def map_key(self, keynumber):
        try:
            from MainServer import key_controller
        except:
            print("Error importing key_controller")
        finally:    
            self.buttons[keynumber].bg = "red"
            self.buttons[keynumber].text = "recording"
            parsed_comb = key_controller.read_key_input(keynumber)
            self.buttons[keynumber].text =parsed_comb
        

    def run(self):
        app = App(title="Keypad example", width=200, height=90, layout="grid")

        self.buttons = [
            PushButton(app, command=self.map_key, args=[0], text="1", grid=[0, 0]),
            PushButton(app, command=self.map_key, args=[1], text="2", grid=[1, 0]),
            PushButton(app, command=self.map_key, args=[2], text="3", grid=[2, 0]),
            PushButton(app, command=self.map_key, args=[3], text="4", grid=[3, 0]),
            PushButton(app, command=self.map_key, args=[4], text="5", grid=[0, 1]),
            PushButton(app, command=self.map_key, args=[5], text="6", grid=[1, 1]),
            PushButton(app, command=self.map_key, args=[6], text="7", grid=[2, 1]),
            PushButton(app, command=self.map_key, args=[7], text="8", grid=[3, 1])
        ]
        app.display()
        print("GUI set up!")