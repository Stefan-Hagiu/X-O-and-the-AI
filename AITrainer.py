from ticTacToe import *
from neuralNetwork import *
from math import sqrt
from math import floor

class AITrainer:
    def __init__(self, numberOfAIs):
        self.AIList = []
        self.numberOfAIs = numberOfAIs
        self.numberOfSurvivingAIs = floor(sqrt(numberOfAIs))
        self.trainingStarted=0
        for i in range (0,self.numberOfAIs):
            self.AIList.append(neuralNetwork(9, 5, 9, 9, []))

    def train(self):
        self.trainingStarted=1
        while self.trainingStarted:
            self.crank()

    def stopTraining(self):
        self.trainingStarted=0

    def crank(self):
        newAIList = []
        winner = 0
        for k in range (0, floor(sqrt(len(self.AIList)))):
            for i in range (0, self.numberOfSurvivingAIs):
                for j in range (i+1, len(self.AIList)-1):
                    winner = max(self.findWinner(self.AIList[i],self.AIList[j]),self.findWinner(self.AIList[j],self.AIList[i]))
                    if winner==2:
                        self.AIList[i],self.AIList[j] = self.AIList[j],self.AIList[i]

        for i in range (0, self.numberOfSurvivingAIs):
            for j in range (i, self.numberOfSurvivingAIs):
                newAI=neuralNetwork(9, 5, 9, 9, [])
                newAI.generateWeightsMatrixFromParents(self.AIList[i],self.AIList[j])
                newAIList.append(newAI)

        while len(newAIList) < len(self.AIList):
            newAIList.append(neuralNetwork(9, 5, 9, 9, []))
        self.AIList = newAIList
        self.numberOfSurvivingAIs = floor(sqrt(len(self.AIList)))

    def initializeAI(self):
        newAI = neuralNetwork(9, 5, 9, 9, [])
        return newAI

    def findWinner(self, ai1, ai2):
        gameWinner = 0
        turn = 1
        answer = 0
        gameBoardReturnString = ""
        gameBoard = TicTacToeBoard()
        while not gameWinner:
            aiInput = gameBoard.returnInputForAi()
            transformInput(aiInput)
            if turn==1:
                answer=ai1.answer(aiInput)
            elif turn==2:
                answer=ai2.answer(aiInput)
            gameBoardReturnString=gameBoard.move(floor(answer/3)+1,answer%3+1)
            if gameBoardReturnString == "Player 1 won":
                gameWinner=1
            elif gameBoardReturnString == "Player 2 won":
                gameWinner=2
            elif gameBoardReturnString == "Tie":
                gameWinner=2
            elif gameBoardReturnString == "Invalid move":
                if turn == 1:
                    gameWinner = 2
                elif turn == 2:
                    gameWinner = 1
            turn=turn^3
        if gameWinner != turn:
            print(gameBoard.returnInputForAi())
        return gameWinner
