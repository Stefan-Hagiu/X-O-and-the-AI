from ticTacToe import TicTacToeBoard
from neuralNetwork import neuralNetwork

class AITrainer:
    def __init__(self, numberOfAIs):
        self.AIList = []
        self.numberOfAIs = numberOfAIs

    def crank(self):
        todo = 1

    def findWinner(self, ai1, ai2):
        gameWinner = 0
        turn = 1
        answer = 0
        gameBoardReturnString = ""
        gameBoard = TicTacToeBoard()
        while not gameWinner:
            aiInput = gameBoard.returnInputForAi()
            self.transformInput(aiInput, turn)
            if turn==1:
                answer=ai1.answer(aiInput)
            else:
                answer=ai2.answer(aiInput)
            gameBoardReturnString=gameBoard.move(answer/3,answer%3+1)
            if gameBoardReturnString == "Player 1 won":
                gameWinner=1
            elif gameBoardReturnString == "Player 2 won":
                gameWinner=2
            elif gameBoardReturnString == "Invalid move":
                if turn == 1:
                    gameWinner = 2
                elif turn == 2:
                    gameWinner = 1
            turn=turn^3

    def transformInput(self, input, gameState):
        for i in range (0, len(input)):
            if input[i]=="X":
                input[i]=10000*gameState
            elif input[i]=="O":
                input[i]=-10000*gameState