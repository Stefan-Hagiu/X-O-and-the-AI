class TicTacToeBoard:
    def __init__(self):
        self.playerToMove = 1
        self.playerPiece = {0:"nothing", 1:"X", 2:"O"}
        self.numberOfPlacedPieces = 0

        self.lastMoveWasValid = 1

        self.boardWidth = 3
        self.boardHeight = 3
        self.gameBoard = [["empty" for width in range (self.boardWidth + 1)] for height in range (self.boardHeight + 1)]

    def move(self, x, y):

        if x < 1 or x > 3 or y < 1 or y > 3:
            self.lastMoveWasValid = 0
            return "Invalid Move"

        if (self.gameBoard[x][y] == "empty"):
            self.gameBoard[x][y] = self.playerPiece[self.playerToMove]
            self.playerToMove = (self.playerToMove ^ 3)
            self.numberOfPlacedPieces += 1
        else:
            self.lastMoveWasValid = 0
            return "Invalid move"

        self.lastMoveWasValid = 1

        if self.playerOneWon():
            return "Player 1 won"

        if self.playerTwoWon():
            return "Player 2 won"

        if self.numberOfPlacedPieces == self.boardHeight * self.boardWidth:
            return "Tie"
        return "Player " + (self.playerToMove ^ 3).__str__() + " moved"

    def playerOneWon(self):
        currentPlayerPiece = self.playerPiece[1]
        for height in range (1, 4):
            if (self.gameBoard[height][1] == currentPlayerPiece
                and self.gameBoard[height][2] == currentPlayerPiece
                and self.gameBoard[height][3] == currentPlayerPiece):
                return 1

        for width in range (1, 4):
            if (self.gameBoard[1][width] == currentPlayerPiece
                and self.gameBoard[2][width] == currentPlayerPiece
                and self.gameBoard[3][width] == currentPlayerPiece):
                return 1

        if (self.gameBoard[1][1] == currentPlayerPiece
            and self.gameBoard[2][2] == currentPlayerPiece
            and self.gameBoard[3][3] == currentPlayerPiece):
            return 1

        if (self.gameBoard[1][3] == currentPlayerPiece
            and self.gameBoard[2][2] == currentPlayerPiece
            and self.gameBoard[3][1] == currentPlayerPiece):
            return 1
        return 0

    def playerTwoWon(self):
        currentPlayerPiece = self.playerPiece[2]
        for height in range(1, 4):
            if (self.gameBoard[height][1] == currentPlayerPiece
                and self.gameBoard[height][2] == currentPlayerPiece
                and self.gameBoard[height][3] == currentPlayerPiece):
                return 1

        for width in range(1, 4):
            if (self.gameBoard[1][width] == currentPlayerPiece
                and self.gameBoard[2][width] == currentPlayerPiece
                and self.gameBoard[3][width] == currentPlayerPiece):
                return 1

        if (self.gameBoard[1][1] == currentPlayerPiece
            and self.gameBoard[2][2] == currentPlayerPiece
            and self.gameBoard[3][3] == currentPlayerPiece):
            return 1

        if (self.gameBoard[1][3] == currentPlayerPiece
            and self.gameBoard[2][2] == currentPlayerPiece
            and self.gameBoard[3][1] == currentPlayerPiece):
            return 1
        return 0

    def returnInputForAi(self):
        returnState = []
        for height in range(1, len(self.gameBoard)):
            for width in range(1, len(self.gameBoard[height])):
                returnState.append([])
                returnState[3*(height-1)+(width-1)].append(self.gameBoard[height][width])
        return returnState
