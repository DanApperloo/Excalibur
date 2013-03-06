from Utilities.GraphicsUtilities.GraphicsUtility import GraphicsUtility
from GraphicsEngine.Factories.GraphicsObjects.Drawables.SpriteDrawableFactory import SpriteDrawableFactory

class SpriteDrawableGroup(object):

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, sceneManagerIn, rootNode, mapDimensions):
        self.sceneManager = sceneManagerIn
        self.rotationalNode = rootNode
        self.xDim = mapDimensions[0]
        self.yDim = mapDimensions[1]
        self.spriteArray = [[]]
        for rowIndex in range(self.xDim):
            for columnIndex in range(self.yDim):
                self.spriteArray[rowIndex].append(None)
            self.spriteArray.append([])
        self.spriteArray.pop()

    # Creates a sprite at the specified location if one doesnt exist there---------------------------------------------#
    def createSprite(self, name, sprites, xpos, ypos):
        if self.spriteArray[xpos][ypos] is None:
            position = GraphicsUtility.getBlockCenterCoord(xpos, ypos, self.xDim, self.yDim)
            self.spriteArray[xpos][ypos] = SpriteDrawableFactory.createCombatMapSprite(self, name, sprites)
            self.spriteArray[xpos][ypos].initialize()
            self.spriteArray[xpos][ypos].setPosition((position['x'], 1, position['y']))
        else:
            raise Exception('Cannot create character in {0!s}:{1!s} because a character already exists there.'.format(xpos, ypos))

    # Hides the sprites------------------------------------------------------------------------------------------------#
    def hideAll(self):
        for rowIndex in range(self.xDim):
            for columnIndex in range(self.yDim):
                if self.spriteArray[rowIndex][columnIndex] is not None:
                    self.spriteArray[rowIndex][columnIndex].setVisible(False)

    # Shows the sprites------------------------------------------------------------------------------------------------#
    def showAll(self):
        for rowIndex in range(self.xDim):
            for columnIndex in range(self.yDim):
                if self.spriteArray[rowIndex][columnIndex] is not None:
                    self.spriteArray[rowIndex][columnIndex].setVisible(True)

    # Removes a sprite from the array----------------------------------------------------------------------------------#
    def removeSprite(self, xpos, ypos):
        if self.spriteArray[xpos][ypos] is not None:
            self.spriteArray[xpos][ypos].cleanUp()
            self.spriteArray[xpos][ypos] = None

    # Releases any used resources--------------------------------------------------------------------------------------#
    def cleanUp(self):
        for rowIndex in range(self.xDim):
            for columnIndex in range(self.yDim):
                self.removeSprite(rowIndex, columnIndex)
        del self.spriteArray
        self.root = None
        self.sceneManager = None