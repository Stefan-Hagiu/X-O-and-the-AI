from tkinter import *

class windowTemplate:

    __thisWindow = None

    def __init__(self):
        self.thisWindow = Tk()
        self.thisWindow.wm_title("X, O and the AI ")
        self.run()

    def run(self):
        self.thisWindow.mainloop()