from windowTemplate import *
from vsAIMenu import VsAIMenu
from gameMenu import GameMenu


class MainMenu (WindowTemplate):

    def __init__(self, programWindow):
        self.gameMenu = None
        self.vsAIMenu = None
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
        self.vsAIMenu = VsAIMenu(self.programWindow)
        self.stop()

    def enterTwoPlayerMode (self):
        self.gameMenu = GameMenu(self.programWindow, "Human", "Human", "")
        self.stop()

    def enterOptions (self):
        todo = 1