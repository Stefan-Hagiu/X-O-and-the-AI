from windowTemplate import *
from gameMenu import *

class MainMenu (WindowTemplate):

    gameMenu = None

    def __init__(self, programWindow):
        super(MainMenu, self).__init__(programWindow)

    def loadUI(self):
        aIButton = Button(self._thisWindow, text="VS AI", command=self.enterAIMenu)
        aIButton.pack(fill = X)

        twoPlayerModeButton = Button(self._thisWindow, text="2P Mode", command=self.enterTwoPlayerMode)
        twoPlayerModeButton.pack(fill = X)

        optionsButton = Button(self._thisWindow, text="Options", command=self.enterOptions)
        optionsButton.pack(fill=X)

        exitButton = Button(self._thisWindow, text="Exit", command=sys.exit)
        exitButton.pack(fill=X)

    def enterAIMenu(self):
        todo = 1

    def enterTwoPlayerMode (self):
        MainMenu.gameMenu = GameMenu(self.programWindow)
        self.stop()

    def enterOptions (self):
        todo = 1