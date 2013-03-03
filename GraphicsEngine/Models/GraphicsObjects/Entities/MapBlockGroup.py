import Storage.Constants as Constant
from Utilities.LoggingUtilities.LoggingUtil import *
from Utilities.GraphicsUtilities.GraphicsUtility import GraphicsUtility
from GraphicsEngine.Models.GraphicsObjects.Entities.MapBlock import MapBlock

class MapBlockGroup(object):

    logger = LoggingUtil('MapBlockGroup')

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, sceneManagerIn, rootNode, inputLayout, meshsIn, mapDimensions, name = 'DefaultMapBlockGroup'):
        """Creates the movement square projector class which stores the array of projectors that display the
        movement options.

        params:
        rootNode - the root node of the combat map
        mapDimensions - a 2 dimension tuple or list used consisting of the width and length of the combat map [x, y]
        """
        self.logger.logDebug("Constructor called from MapBlockGroup: {0}".format(name))
        self.name = name
        self.sceneManager = sceneManagerIn
        self.rotationalNode = rootNode
        # 3 dimensional array depicting block layout of map
        self.layout = inputLayout
        self.xDim = mapDimensions[0]
        self.yDim = mapDimensions[1]
        self.zPos = 0
        # Create List of all texture files used in map
        self.meshsUsed = meshsIn
        self.blockArray = [[]]

    # Initialises the projector array----------------------------------------------------------------------------------#
    def initialize(self):
        for x in range(self.xDim):
            for y in range(self.yDim):
                # Create the map block in this location and initialise
                position = GraphicsUtility.getBlockCenterCoord(x, y, self.xDim, self.yDim)
                self.blockArray[x].append(MapBlock(self.sceneManager, self.rotationalNode, self.meshsUsed[y % len(self.meshsUsed)], position['x'], position['y'], self.zPos, "{0} - MapBlock X:{1} Y:{2}".format(self.name, position['x'], position['y'])))
                self.blockArray[x][y].initialize()
            self.blockArray.append([])

    def hideAll(self):
        for x in range(self.xDim):
            for y in range(self.yDim):
                self.blockArray[x][y].hide()

    def showAll(self):
        for x in range(self.xDim):
            for y in range(self.yDim):
                self.blockArray[x][y].show()

    # Returns the map block array--------------------------------------------------------------------------------------#
    def getBlockArray(self):
        return self.blockArray

    # Releases any used resources--------------------------------------------------------------------------------------#
    def cleanUp(self):
        self.logger.logDebug("Releasing resources for MapBlockGroup '{0}'".format(self.name))
        del self.name
        for blockRow in self.blockArray:
            for block in blockRow:
                block.cleanUp()
        del self.blockArray
        del self.meshsUsed
        del self.layout
        self.sceneManager = None
        self.rotationalNode = None