from windowTemplate import *
from ticTacToe import *

class GameMenu(WindowTemplate):

    def __init__(self, programWindow):
        super(GameMenu, self).__init__(programWindow)
        self.game = TicTacToeBoard()

    def loadUI(self):
        self.buttonList = [[Button(self._thisWindow) for i in range (0, 4)] for j in range (0, 4)]
        for i in range (1, 4):
            for j in range (1, 4):
                self.buttonList[i][j].grid(row=i, column=j)
                self.buttonList[i][j].bind("<Button-1>", self.buttonClick)

    def buttonClick(self, event):
        for i in range (1, 4):
            for j in range (1, 4):
                if self.buttonList[i][j] == event.widget:
                    x=i
                    y=j
        returnString = self.game.move(x, y)
        print (returnString)

