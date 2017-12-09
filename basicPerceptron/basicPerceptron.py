import random
import math

alpha = 0.3

def randomValue():
    return math.floor(random.random()*2) 

def randomWeight():
    return random.uniform(-1,1)

class inputNodes:

    def __init__(self, value=1, weight= -1, name="node"):
        self.value = value
        self.weight = weight
        self.name = name
    def nodePrint(self):
        output = 'The value of ' + repr(self.name) + ' is ' + repr(self.value) + ' and the weight is ' + repr(self.weight)
        print(output)
    def weightPrint(self):
        output = 'The weight of ' + repr(self.name) + ' is ' +  repr(self.weight)
        print(output)
    def valuePrint(self):
        output = 'The value of ' + repr(self.name) + ' is ' +  repr(self.value)
        print(output)
        
def printNodes(nodeA,nodeB,nodeC,nodeD):
    nodeA.nodePrint()
    nodeB.nodePrint()
    nodeC.nodePrint()
    nodeD.nodePrint()

def newValues(nodeA,nodeB,nodeC):
    nodeA.value = randomValue()
    nodeB.value = randomValue()
    nodeC.value = randomValue()

def main(nodeA,nodeB,nodeC,nodeD):
    for i in range(0,8001):
        if nodeA.value == 1 and nodeC.value == 1:
            expectedOutput = 1
        else:
            expectedOutput = 0
        sumInputs = nodeA.weight*nodeA.value + nodeB.weight*nodeB.value + nodeC.weight*nodeC.value + nodeD.weight*nodeD.value
        output= 1/(1+math.exp(-sumInputs))
        if i % 250 == 0:
            printNodes(nodeA,nodeB,nodeC,nodeD)
            print(output)
        if(output != expectedOutput):
            nodeA.weight += (alpha * (expectedOutput - output) * (output*(1-output)) * nodeA.value)
            nodeB.weight += (alpha * (expectedOutput - output) * (output*(1-output)) * nodeB.value)
            nodeC.weight += (alpha * (expectedOutput - output) * (output*(1-output)) * nodeC.value)
        newValues(nodeA,nodeB,nodeC)


nodeA = inputNodes(randomValue(),randomWeight(),"nodeA")
nodeB = inputNodes(randomValue(),randomWeight(),"nodeB")
nodeC = inputNodes(randomValue(),randomWeight(),"nodeC")
nodeD = inputNodes(1,-1,"nodeD")

main(nodeA,nodeB,nodeC,nodeD)


