from GraphicsEngine.Factories.GraphicsObjects.CombatMapLogistics.ProjectorFactory import ProjectorFactory
from Utilities.LoggingUtilities.LoggingUtil import *
from Utilities.GraphicsUtilities.GraphicsUtility import GraphicsUtility
import copy as copy
from GraphicsEngine.Models.GraphicsObjects.CombatMapLogistics.Pattern import Pattern
from GraphicsEngine.Models.GraphicsObjects.CombatMapLogistics.SquareProjector import SquareProjector
from GraphicsEngine.Models.GraphicsObjects.CombatMapLogistics.SelectionProjector import SelectionProjector

class ProjectorGroup(object):
    """Stores the entire block square projector array."""

    logger = LoggingUtil('ProjectorGroup')

    # Class Variables--------------------------------------------------------------------------------------------------#
    LEFT = [-1,0]
    RIGHT = [1,0]
    UP = [0,1]
    DOWN = [0,-1]
    # -----------------------------------------------------------------------------------------------------------------#

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, sceneManagerIn, rootNode, mapDimensions, name = "DefaultProjectorGroup"):
        """Creates the movement square projector class which stores the array of projectors that display the
        movement options.

        Required Parameters:
        rootNode - the root node of the combat map
        mapDimensions - a 2 dimension tuple or list used consisting of the width and length of the combat map [x, y]
        """
        self.logger.logDebug("Constructor called for ProjectorGroup: {0}".format(name))
        self.name = name
        self.root = rootNode
        self.sceneManager = sceneManagerIn
        # Map Dimensions
        self.xDim = mapDimensions[0]
        self.yDim = mapDimensions[1]
        # Projector array and attached Map Blocks
        self.projectorArray = [[]]
        self.mapBlocks = None
        # Patterns
        self.workingTypeArray = [[]]
        self.patterns = []
        self.patternsTop = None
        # Pointer
        self.floatingPointer = None
        self.canPointerLeaveBasePattern = None
        self.pointerPosition = []

    # Initialises the projector array----------------------------------------------------------------------------------#
    def initialize(self):
        self.logger.logDebug("Initializing ProjectorGroup '{0}'".format(self.name))
        for rowIndex in range(self.xDim):
            for columnIndex in range(self.yDim):
                position = GraphicsUtility.getBlockCenterCoord(rowIndex, columnIndex, self.xDim, self.yDim)
                projector = ProjectorFactory.createBlockHighlighter(self, rowIndex, columnIndex, self.name)
                self.projectorArray[rowIndex].append(projector)
                self.projectorArray[rowIndex][columnIndex].initialize(position['x'], position['y'])
            self.projectorArray.append([])
        self.projectorArray.pop()

    # Creates a pointer at the specified position----------------------------------------------------------------------#
    def createPointerAtPosition(self, arrayPosition):
        self.logger.logDebug("Creating Pointer at position X:{0} Y:{1}".format(arrayPosition[0], arrayPosition[1]))
        if self.mapBlocks is not None:
            realPosition = GraphicsUtility.getBlockCenterCoord(arrayPosition[0], arrayPosition[1], self.xDim, self.yDim)
            self.floatingPointer = ProjectorFactory.createPointerAtPosition(arrayPosition[0], arrayPosition[1], self.name)
            self.floatingPointer.initialize(realPosition['x'], realPosition['y'], 'Pointer', self.mapBlocks[arrayPosition[0]][arrayPosition[1]])
            self.pointerPosition = [arrayPosition[0], arrayPosition[1]]
        else:
            raise Exception('Cannot create movable selector because no Map Blocks are tied to the Square Projector Group.')

    # Moves the selector to a different block--------------------------------------------------------------------------#
    def movePointer(self, direction):
        self.logger.logDebug("Moving Pointer in direction X:{0} Y:{1}".format(direction[0], direction[1]))
        if self.floatingPointer is not None:
            xPos = self.pointerPosition[0] + direction[0]
            yPos = self.pointerPosition[1] + direction[1]
            if self.canPointerLeaveBasePattern or self.positionInPattern(xPos, yPos):
                self.removePointer()
                self.createPointerAtPosition((xPos, yPos))
        else:
            raise Exception('Cannot move selector because it does not exist.')

    # Create pointer at the center of the base pattern-----------------------------------------------------------------#
    def createPointer(self, position = None):
        if self.patternsTop is None:
            if position is None:
                location = (6,6)
            else:
                location = position
            self.createPointerAtPosition(location)
            self.canPointerLeaveBasePattern = True
        else:
            self.canPointerLeaveBasePattern = False
            self.createPointerAtPosition(self.patterns[self.patternsTop].getPosition())


    # Returns the selector---------------------------------------------------------------------------------------------#
    def getPointer(self):
        return self.floatingPointer

    # Makes the selector visible---------------------------------------------------------------------------------------#
    def showPointer(self):
        self.logger.logDebug("Showing Pointer")
        self.floatingPointer.showAll()

    # Hides the selector-----------------------------------------------------------------------------------------------#
    def hidePointer(self):
        self.logger.logDebug("Hiding Pointer")
        self.floatingPointer.hideAll()

    # Removes the selector from the map--------------------------------------------------------------------------------#
    def removePointer(self):
        self.floatingPointer.cleanUp()
        self.floatingPointer = None

    # Ties the projector array to an equivalently sized Map Block array------------------------------------------------#
    def tieToMapBlocks(self, mapBlocksIn):
        self.logger.logDebug("Tying MapBlocks to Projectors in ProjectorGroup '{0}'".format(self.name))
        if self.mapBlocks is None:
            self.mapBlocks = mapBlocksIn
            for rowIndex in range(self.xDim):
                for columnIndex in range(self.yDim):
                    self.projectorArray[rowIndex][columnIndex].tieToMapBlock(self.mapBlocks[rowIndex][columnIndex])
        else:
            raise Exception('Cannot tie projectors to new Map Blocks because they are already tied in.')

    # Unties the projector array from its Map Block array in-case it needs to be switched out----------------------------#
    def untieMapBlocks(self):
        self.logger.logDebug("Untying MapBlocks to Projectors in ProjectorGroup '{0}'".format(self.name))
        if self.floatingPointer is not None:
            self.mapBlocks = None
            for rowIndex in range(self.xDim):
                for columnIndex in range(self.yDim):
                    self.projectorArray[rowIndex][columnIndex].untieMapBlock()
        else:
            raise Exception('Cannot untie projectors when a Selection Pointer still exists.')

    # Returns the projector at a given coordinate----------------------------------------------------------------------#
    def getProjectorAt(self, xpos, ypos):
        return self.projectorArray[xpos][ypos]

    def refreshPatterns(self):
        self.logger.logDebug("Refreshing patterns in ProjectorGroup '{0}'".format(self.name))
        for row in range(self.xDim):
            for column in range(self.yDim):
                self.projectorArray[row][column].hide()
                self.projectorArray[row][column].setProjectionType(self.workingTypeArray[row][column])
                self.projectorArray[row][column].show()

    def addTopLayerToWorkingArray(self):
        layer = self.patterns[self.patternsTop].getPatternLayer()
        for row in range(self.xDim):
            for column in range(self.yDim):
                if layer[row][column] is not SquareProjector.NO_TYPE:
                    self.workingTypeArray[row][column] = copy.deepcopy(layer[row][column])

    def removeTopLayerFromWorkingArray(self):
        topLayer = self.patterns[self.patternsTop].getPatternLayer()
        for row in range(self.xDim):
            for column in range(self.yDim):
                if topLayer[row][column] is not SquareProjector.NO_TYPE:
                    self.workingTypeArray[row][column] = self.recursivelyRollback(self.patternsTop, row,column)

    def recursivelyRollback(self, index, row, column):
        lowerLayer = self.patterns[index - 1].getPatternLayer()
        if (index - 1) != 0 and lowerLayer[row][column] is SquareProjector.NO_TYPE:
            underBlock = self.recursivelyRollback(index - 1, row, column)
        else:
            underBlock = lowerLayer[row][column]
        return copy.deepcopy(underBlock)

    def addPattern(self, pattern, boxType, origin = None):
        self.logger.logDebug("Adding pattern to working block array in Projector Group '{0}'".format(self.name))
        if self.patternsTop is None:
            self.patternsTop = 0
            self.patterns.append(Pattern((self.xDim, self.yDim), SquareProjector.NO_TYPE))
            self.patterns[self.patternsTop].initialize(origin, pattern, boxType, False)
            self.workingTypeArray = self.patterns[self.patternsTop].getPatternLayer()
        else:
            self.patternsTop = self.patternsTop + 1
            self.patterns.append(Pattern((self.xDim, self.yDim), SelectionProjector.NO_TYPE))
            if origin is not None:
                position = origin
            else:
                position = self.patterns[self.patternsTop - 1].getPosition()
            self.patterns[self.patternsTop].initialize(position, pattern, boxType, True)
            self.addTopLayerToWorkingArray()
        self.refreshPatterns()

    def removePattern(self):
        self.logger.logDebug("Removing pattern from working block array in Projector Group '{0}'".format(self.name))
        if self.patternsTop == 0:
            self.patterns.pop().cleanUp()
            self.patternsTop = None
            for row in range(self.xDim):
                for column in range(self.yDim):
                    self.projectorArray[row][column].hide()
            self.refreshPatterns()
        elif self.patternsTop > 0:
            self.removeTopLayerFromWorkingArray()
            self.patterns.pop().cleanUp()
            self.patternsTop = self.patternsTop - 1
            self.refreshPatterns()
        else:
            raise Exception("No patterns left to remove.")

    def movePattern(self, direction):
        self.logger.logDebug("Attempting to move pattern in direction X:{0} Y:{1}".format(direction[0], direction[1]))
        if self.patterns[self.patternsTop].isMovable():
            pattern = self.patterns[self.patternsTop]
            patternShape = pattern.getShape()
            patternBlockType = pattern.getBlockType()
            xPos = pattern.getPosition()[0] + direction[0]
            yPos = pattern.getPosition()[1] + direction[1]
            if self.positionInPattern(xPos, yPos, -1):
                self.removePattern()
                self.addPattern(patternShape, patternBlockType, (xPos, yPos))

    # Returns true if the position is in the base pattern, false otherwise---------------------------------------------#
    def positionInPattern(self, xpos, ypos, offset = 0):
        if self.patternsTop is not None:
            if self.patterns[self.patternsTop + offset].getPatternLayer()[xpos][ypos] is not 0:
                return True
            else:
                return False
        else:
            return False

    # Releases any used resources--------------------------------------------------------------------------------------#
    def cleanUp(self):
        self.logger.logDebug("Releasing resources for ProjectorGroup '{0}'".format(self.name))
        del self.name
        for rowIndex in range(self.xDim):
            for columnIndex in range(self.yDim):
                self.projectorArray[rowIndex][columnIndex].cleanUp()
        del self.projectorArray
        del self.workingTypeArray
        del self.patterns
        del self.patternsTop
        if self.floatingPointer is not None: self.removePointer()
        self.root = None
        self.sceneManager = None