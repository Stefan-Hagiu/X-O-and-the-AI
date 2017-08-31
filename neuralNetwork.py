from cmath import e


class neuralNetwork:

    def sigmoid(self, value):
        return 1/(1 + (e ** (-value)))

    def feedInputs(self, inputList):
        todo = 1

    def returnAnswer(self):
        todo = 1

    def __init__(self, numberOfInputs, inputList, numberOfHiddenLayers, neuronsPerHiddenLayer, numberOfOutputs):
        self.numberOfInputs = numberOfInputs
        self.inputList = inputList
        self.numberOfHiddenLayers = numberOfHiddenLayers
        self.neuronsPerHiddenLayer = neuronsPerHiddenLayer
        self.numberOfOutputs = numberOfOutputs
        todo = 1