from Utilities.LoggingUtilities.LoggingUtil import *
import copy as copy

class Pattern(object):

    logger = LoggingUtil('Pattern')

    def __init__(self, dimensions, default, name = "DefaultPattern"):
        self.logger.logDebug("Constructor called for Pattern: {0}".format(name))
        self.name = name
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

    def initialize(self, origin, patternIn, boxType, movable):
        self.active = True
        self.position = origin
        self.shape = copy.deepcopy(patternIn)
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
        return copy.deepcopy(self.shape)

    def getBlockType(self):
        return copy.deepcopy(self.blockType)

    def getPosition(self):
        return copy.deepcopy(self.position)

    def cleanUp(self):
        self.logger.logDebug("Cleaning resources for Pattern '{0}'".format(self.name))
        self.name = None
        del self.name
        self.xDim = None
        del self.xDim
        self.yDim = None
        del self.yDim
        self.defaultValue = None
        del self.defaultValue
        self.layer = None
        del self.layer
        self.shape = None
        del self.shape
        self.shape = None
        del self.blockType
        self.position = None
        del self.position
        self.movable = None
        del self.movable