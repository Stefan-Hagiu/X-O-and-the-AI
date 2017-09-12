from tkinter import *


class WindowTemplate:

    def __init__(self, programWindow):
        self.programWindow = programWindow
        self._thisWindow = Frame(programWindow)
        self.loadUI()
        self._thisWindow.pack()

    def loadUI(self):
        print("Not ready yet")

    def stop(self):
        self._thisWindow.destroy()
