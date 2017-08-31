from cmath import e
from numpy import dot

'''
 
 !!!!inputList has to be a 1-column vertical matrix!!!!
    The input values should be wide apart. For example, if an empty square is represented as a 0, the same square should
    be later represented as 10000 if a player makes a move in that spot
 
 weightsMatrix will be structured as follows:
    -it will be a 3-dimensional matrix ( [][][] )
    -the first field indicates the current layer of connections
    -the values of the second and third field will contain the following matrix:
        w11 w21 ... wn1
        w12 w22 ... wn2
        .
        .
        .
        w1n w2n ... wnn
        
    Example: If I wanted to access the element of the x th row and y th column of the matrix between the i th and 
    the i+1 th layers of neurons, I would write weightsMatrix[i][x][y].
    All of the values in this matrix will be between -1 and 1.
'''

class neuralNetwork:

    def sigmoid(self, value):
        return 1/(1 + (e ** (-value)))

    def feedInputs(self, inputList):
        todo = 1

    def returnAnswer(self):
        todo = 1

    def __init__(self, inputList, numberOfHiddenLayers, neuronsPerHiddenLayer, numberOfOutputs, weightsMatrix):

        self.currentValues = inputList
        self.numberOfHiddenLayers = numberOfHiddenLayers
        self.neuronsPerHiddenLayer = neuronsPerHiddenLayer
        self.numberOfOutputs = numberOfOutputs
        self.weightsMatrix = weightsMatrix

        if self.weightsMatrix == []:
            self.generateRandomWeightsMatrix()

        self.propagateThroughNetwork()
        todo = 1

    def generateRandomWeightsMatrix(self):
        todo = 1

    def propagateThroughNetwork(self):
        for i in range (0, self.numberOfHiddenLayers + 1):
            self.currentValues = dot(self.weightsMatrix[i], self.currentValues)