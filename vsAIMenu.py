from windowTemplate import *
from AITrainer import AITrainer

class VsAIMenu(WindowTemplate):
    def __init__(self, programWindow):

        super(VsAIMenu, self).__init__(programWindow)
        self.aITrainer = AITrainer(1000)
        
    def loadUI(self):
        self.startTrainingButton = Button(self._thisWindow, text="Start training neural networks")
        self.startTrainingButton.grid(row = 0, column = 0)

        self.stopTrainingButton = Button(self._thisWindow, text="Stop training neural networks", state=DISABLED)
        self.stopTrainingButton.grid(row=1, column=0)

        self.startTrainingButton.bind("<Button-1>", self.startTrainingNeuralNet)
        self.stopTrainingButton.bind("<Button-1>", self.stopTrainingNeuralNet)

    def startTrainingNeuralNet(self, event):
        self.startTrainingButton.config(state=DISABLED)
        self.stopTrainingButton.config(state=NORMAL)

    def stopTrainingNeuralNet(self, event):
        self.startTrainingButton.config(state=NORMAL)
        self.stopTrainingButton.config(state=DISABLED)