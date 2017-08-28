from windowTemplate import *

class GameMenu(WindowTemplate):

    def __init__(self, programWindow):
        super(GameMenu, self).__init__(programWindow)

    def loadUI(self):
        self.buttonList = [[Button(self._thisWindow) for i in range (0, 4)] for j in range (0, 4)]
        for i in range (1, 4):
            for j in range (1, 4):
                self.buttonList[i][j].grid(row=i, column=j)
