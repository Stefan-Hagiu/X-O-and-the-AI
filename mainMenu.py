from windowTemplate import *
from vsAIMenu import VsAIMenu
from gameMenu import GameMenu


class MainMenu (WindowTemplate):

    def __init__(self, programWindow):
        self.gameMenu = None
        self.vsAIMenu = None
        super(MainMenu, self).__init__(programWindow)

    def loadUI(self):
        self.aIButton = Button(self._thisWindow, text="VS AI", command=self.enterAIMenu)
        self.aIButton.pack(fill = X)

        self.twoPlayerModeButton = Button(self._thisWindow, text="2P Mode", command=self.enterTwoPlayerMode)
        self.twoPlayerModeButton.pack(fill = X)

        self.optionsButton = Button(self._thisWindow, text="Options", command=self.enterOptions)
        self.optionsButton.pack(fill=X)

        self.exitButton = Button(self._thisWindow, text="Exit", command=sys.exit)
        self.exitButton.pack(fill=X)

    def enterAIMenu(self):
        self.vsAIMenu = VsAIMenu(self.programWindow)
        self.stop()

    def enterTwoPlayerMode (self):
        self.gameMenu = GameMenu(self.programWindow, "Human", "Human", "")
        self.stop()

    def enterOptions (self):
        todo = 1
