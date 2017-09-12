from windowTemplate import *
from ticTacToe import TicTacToeBoard
from neuralNetwork import neuralNetwork
from threading import Thread


class GameMenu(WindowTemplate):

    def __init__(self, programWindow,player1Type, player2Type, enemyAI=neuralNetwork.__init__()):

        if player1Type == "":
            player1Type = "Human"
        if player2Type == "":
            player2Type = "Human"

        self.buttonList = []

        self._emptyImage = ImageTk.PhotoImage(Image.open("empty.png"))
        self._xImage = ImageTk.PhotoImage(Image.open("X.png"))
        self._yImage = ImageTk.PhotoImage(Image.open("O.png"))
        self.imageList = [self._emptyImage, self._xImage, self._yImage]

        self.game = TicTacToeBoard()
        self.aI = enemyAI
        self.player1Type = player1Type
        self.player2Type = player2Type
        self.gameRunning = 1


        super(GameMenu, self).__init__(programWindow)

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
        thread = Thread(target = self.gameThread)
        thread.start()

    def gameThread(self):
        playerToMove=1
        answer = ""
        while self.gameRunning:
            if playerToMove == 1:
                if self.player1Type == "AI":
                    answer = self.aI.answer(neuralNetwork.transformInput(self.game.returnInputForAi, playerToMove))
                    playerToMove^=3
            else:
                if self.player2Type == "AI":
                    answer = self.aI.answer(neuralNetwork.transformInput(self.game.returnInputForAi, playerToMove))
                    playerToMove^=3

    def buttonClick(self, event):
        x=0
        y=0
        for i in range (1, 4):
            for j in range (1, 4):
                if self.buttonList[i][j] == event.widget:
                    x=i
                    y=j
        self.makeMove(x, y)

    def makeMove(self, x, y):
        returnString = self.game.move(x, y)
        if returnString == "Player 1 moved" or returnString == "Player 1 won":
            self.buttonList[x][y].config(image=self.imageList[1])
        elif returnString == "Player 2 moved" or returnString == "Player 2 won":
            self.buttonList[x][y].config(image=self.imageList[2])

