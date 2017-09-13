from windowTemplate import *
from AITrainer import AITrainer

class VsAIMenu(WindowTemplate):
    def __init__(self, programWindow):
        super(VsAIMenu, self).__init__(programWindow)
        aITrainer = AITrainer(1000)
        
    def loadUI(self):
        self.startTrainingButton = Button(self._thisWindow, text="Start training neural networks",
                                          command=self.startTrainingNeuralNet())
        self.startTrainingButton.grid(row = 0, column = 0)

        self.stopTrainingButton = Button(self._thisWindow, text="Stop training neural networks", state=DISABLED,
                                         command=self.stopTrainingNeuralNet())
        self.stopTrainingButton.grid(row=1, column=0)

    def startTrainingNeuralNet(self):
        todo=1

    def stopTrainingNeuralNet(self):
        todo=1