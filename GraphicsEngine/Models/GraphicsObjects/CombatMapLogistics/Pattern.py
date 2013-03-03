import copy as copy

class Pattern(object):

    def __init__(self, dimensions, default):
        self.xDim = dimensions[0]
        self.yDim = dimensions[1]
        self.defaultValue = default
        self.layer = self.cleanLayer()
        self.shape = None
        self.blockType = None
        self.position = None
        self.movable = None

    def cleanLayer(self):
        layer = [[]]
        for rowIndex in range(self.xDim):
            for columnIndex in range(self.yDim):
                layer[rowIndex].append(self.defaultValue)
            layer.append([])
        return layer

    def initialise(self, origin, patternIn, boxType, movable):
        self.active = True
        self.position = origin
        self.shape = patternIn
        self.blockType = boxType
        self.movable = movable
        for rowIndex in range(len(patternIn)):
            row = origin[0] - (len(patternIn) / 2) + rowIndex
            if 0 <= row < self.xDim:
                for columnIndex in range(len(patternIn[0])):
                    column = origin[1] - (len(patternIn[0]) / 2) + columnIndex
                    if 0 <= column < self.yDim:
                        if patternIn[rowIndex][columnIndex] == 1:
                            self.layer[row][column] = boxType

    def isMovable(self):
        return self.movable

    def getPatternLayer(self):
        return copy.deepcopy(self.layer)

    def getShape(self):
        return copy.copy(self.shape)

    def getBlockType(self):
        return self.blockType

    def getPosition(self):
        return self.position

    def cleanUp(self):
        del self.xDim
        del self.yDim
        del self.defaultValue
        del self.layer
        del self.shape
        del self.blockType
        del self.position
        del self.movable