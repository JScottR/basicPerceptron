import random
import math

def randomValue():
    return math.floor(random.random()*2) 

def randomWeight():
    return random.uniform(-1,1)

class inputNodes:
    # should be either 0 or 1 
    value = 1
    ## weight value
    weight = -1

def init(nodeA,nodeB,nodeC):
    nodeA.value = randomValue()
    nodeA.weight = randomWeight()
    nodeB.value =  randomValue()
    nodeB.weight = randomWeight()
    nodeC.value =  randomValue()
    nodeC.weight = randomWeight()

def printNodes(nodeA,nodeB,nodeC,nodeD):
    print(nodeA.value)
    print(nodeA.weight)
    print(nodeB.value)
    print(nodeB.weight)
    print(nodeC.value)
    print(nodeC.weight)
    print(nodeD.value)
    print(nodeD.weight)

def newValues(nodeA,nodeB,nodeC):
    nodeA.value = randomValue()
    nodeB.value = randomValue()
    nodeC.value = randomValue()

nodeA = inputNodes()
nodeB = inputNodes()
nodeC = inputNodes()
nodeD = inputNodes()

init(nodeA,nodeB,nodeC)
printNodes(nodeA,nodeB,nodeC,nodeD)
