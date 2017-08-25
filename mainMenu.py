from tkinter import *
from windowTemplate import windowTemplate

class mainMenu (windowTemplate):
    def __init__(self):
        super().__init__()

    def run(self):
        self.thisWindow.mainloop()