from windowTemplate import *
from ticTacToe import TicTacToeBoard


class GameMenu(WindowTemplate):

    def __init__(self, programWindow):
        self.buttonList = []

        self._emptyImage = ImageTk.PhotoImage(Image.open("empty.png"))
        self._xImage = ImageTk.PhotoImage(Image.open("X.png"))
        self._yImage = ImageTk.PhotoImage(Image.open("O.png"))
        self.imageList = [self._emptyImage, self._xImage, self._yImage]

        super(GameMenu, self).__init__(programWindow)
        self.game = TicTacToeBoard()

    def loadUI(self):
        for i in range (0,4):
            self.buttonList.append([])
            for j in range (0,4):
                self.buttonList[i].append(Button(self._thisWindow))
        for i in range (1, 4):
            for j in range (1, 4):
                self.buttonList[i][j].config(image=self.imageList[0])
                self.buttonList[i][j].grid(row=i, column=j)
                self.buttonList[i][j].bind("<Button-1>", self.buttonClick)


    def buttonClick(self, event):
        x=0
        y=0
        for i in range (1, 4):
            for j in range (1, 4):
                if self.buttonList[i][j] == event.widget:
                    x=i
                    y=j
        returnString = self.game.move(x, y)
        if returnString == "Player 1 moved" or returnString == "Player 1 won":
            event.widget.config(image=self.imageList[1])
        elif returnString == "Player 2 moved" or returnString == "Player 2 won":
            event.widget.config(image=self.imageList[2])


