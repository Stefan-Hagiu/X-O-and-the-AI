from tkinter import *

class WindowTemplate:

    def __init__(self):
        _thisWindow = None
        self._thisWindow = Tk()
        self._thisWindow.wm_title("X, O and the AI ")
        self.loadUI()
        self.run()

    def run(self):
        self._thisWindow.mainloop()

    def loadUI(self):
        print("Not ready yet")