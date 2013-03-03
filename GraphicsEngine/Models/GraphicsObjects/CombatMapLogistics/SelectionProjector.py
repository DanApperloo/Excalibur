from Utilities.LoggingUtilities.LoggingUtil import *
from GraphicsEngine.Models.GraphicsObjects.CombatMapLogistics.SquareProjector import SquareProjector
from GraphicsEngine.Models.GraphicsObjects.Drawables.SpriteDrawable import SpriteDrawable

class SelectionProjector(SquareProjector):
    """Controls the move-able pointer."""

    logger = LoggingUtil('SelectionProjector')

    # -----------------------------------------------------------------------------------------------------------------#
    SELECTOR_IMAGE = "Selection_Box.png"
    SELECTOR_TYPE = 4
    # -----------------------------------------------------------------------------------------------------------------#

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, sceneManagerIn, rootNode, rowIndex, columnIndex, name = "DefaultSelectionProjector"):
        self.logger.logDebug("Constructor called for SelectionProjector: {0}".format(name))
        self.name = name
        SquareProjector.__init__(self, sceneManagerIn, rootNode, rowIndex, columnIndex)
        self.pointer = None

    # Initialises the selector at a given position and turns its visibility to false-----------------------------------#
    def initialize(self, xpos, ypos, namePrefix, mapBlock):
        SquareProjector.initialize(self, xpos, ypos, namePrefix)
        self.projectionType = self.SELECTOR_TYPE
        self.projectionImage = self.SELECTOR_IMAGE
        self.tieToMapBlock(mapBlock)
        self.pointer = SpriteDrawable(self.sceneManager, self.mapBlock.getNode())
        self.pointer.initialize(namePrefix, 'Pointer')
        self.pointer.setPosition((0, 5, 0))
        self.pointer.setVisible(False)

    # Shows both the selector and the pointer--------------------------------------------------------------------------#
    def showAll(self):
        self.showPointer()
        self.showSelector()

    def setProjectionType(self, projectionType):
        pass

    def getProjectionType(self):
        pass

    # Hides both the selector and the pointer--------------------------------------------------------------------------#
    def hideAll(self):
        self.hidePointer()
        self.hideSelector()

    # Shows just the pointer-------------------------------------------------------------------------------------------#
    def showPointer(self):
        self.pointer.setVisible(True)

    # Hides just the pointer-------------------------------------------------------------------------------------------#
    def hidePointer(self):
        self.pointer.setVisible(False)

    # Shows just the selector------------------------------------------------------------------------------------------#
    def showSelector(self):
        SquareProjector.show(self)

    # Hides just the selector------------------------------------------------------------------------------------------#
    def hideSelector(self):
        SquareProjector.hide(self)

    # Releases any used resources by the projector---------------------------------------------------------------------#
    def cleanUp(self):
        self.logger.logDebug("Releasing resources for SelectionProjector '{0}'".format(self.name))
        del self.name
        self.pointer.cleanUp()
        del self.pointer
        SquareProjector.cleanUp(self)