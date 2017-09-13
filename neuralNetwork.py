from cmath import e
from numpy import dot, asarray
import random

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
    
 The number of hidden layers should be at least 1
'''

class neuralNetwork:

    def sigmoid(self, value):
        return 1/(1 + (e ** (-value)))

    def generateWeightsMatrixFromParents(self, firstFather, secondFather):
        self.weightsMatrix = []
        for i in range (0, len(firstFather.weightsMatrix)):
            self.weightsMatrix.append([])
            for j in range (0, len(firstFather.weightsMatrix[i])):
                self.weightsMatrix[i].append([])
                for k in range (0, len(firstFather.weightsMatrix[i][j])):
                    self.weightsMatrix[i][j].append((firstFather.weightsMatrix[i][j][k]+secondFather.weightsMatrix[i][j][k])/2)
        print(self.weightsMatrix)
        return self.weightsMatrix

    def __init__(self, numberOfInputs, numberOfHiddenLayers, neuronsPerHiddenLayer, numberOfOutputs, weightsMatrix):

        self.numberOfInputs = numberOfInputs
        self.numberOfHiddenLayers = numberOfHiddenLayers
        self.neuronsPerHiddenLayer = neuronsPerHiddenLayer
        self.numberOfOutputs = numberOfOutputs
        self.weightsMatrix = weightsMatrix

        self.currentValues = []

        if self.weightsMatrix == []:
            self.generateRandomWeightsMatrix()

    def answer(self, inputList):
        self.currentValues = inputList
        self.propagateThroughNetwork()
        currentIndex=0
        for i in self.currentValues:
            if i == max(self.currentValues):
                return currentIndex
            currentIndex += 1

    def generateRandomWeightsMatrix(self):
        random.seed(a=None)
        self.weightsMatrix.append(self.generateMatrix(self.neuronsPerHiddenLayer, self.numberOfInputs))
        for i in range(0,self.numberOfHiddenLayers-1):
            self.weightsMatrix.append(self.generateMatrix(self.neuronsPerHiddenLayer, self.neuronsPerHiddenLayer))
        self.weightsMatrix.append(self.generateMatrix(self.numberOfOutputs, self.neuronsPerHiddenLayer))

    @staticmethod
    def generateMatrix(height, width):
        returnMatrix = []
        for i in range (0, height):
            returnMatrix.append([])
            for j in range (0, width):
                returnMatrix[i].append(random.random() - random.random())
        return returnMatrix

    def propagateThroughNetwork(self):
        for i in range (0, self.numberOfHiddenLayers + 1):
            self.currentValues = dot(self.weightsMatrix[i], self.currentValues)
            for j in self.currentValues:
                j = self.sigmoid(j)

    @staticmethod
    def transformInput(input, gameState):
        for i in range (0, len(input)):
            if input[i]=="X":
                input[i]=10000*gameState
            elif input[i]=="O":
                input[i]=-10000*gameState
            else:
                input[i]=10