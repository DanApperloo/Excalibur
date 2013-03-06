import ogre.gui.CEGUI as CEGUI
import Storage.Constants as Constant

# Stores common Graphics and UI related functions----------------------------------------------------------------------#
class GraphicsUtility(object):
    """Stores common utility functions that are related to Graphics or UI"""

    # Puts the mouse on the middle of an element-----------------------------------------------------------------------#
    @classmethod
    def putPointerOnElement(cls, focusedElement):
        """Puts the mouse on the middle of the specified element."""
        # Determines X co-ordinate
        xPos = focusedElement.PixelRect.Position.d_x
        additionalX = focusedElement.getPixelSize().d_width / 2
        # Determines Y co-ordinate
        yPos = focusedElement.PixelRect.Position.d_y
        additionalY = focusedElement.getPixelSize().d_height / 2
        # Sets actual mouse position
        CEGUI.System.getSingleton().injectMousePosition(xPos + additionalX, yPos + additionalY)

    # Effects a window and its children recursively with a specified method---------------------------------------------#
    @classmethod
    def effectRecursiveChildWindow(cls, caller, window, method):
        """Recursively effect a window and its child windows with a given method and calling object"""
        for i in range(window.getChildCount()):
            addToList = window.getChildAtIdx(i)
            method(caller, addToList)
            cls.effectRecursiveChildWindow(caller, addToList, method)

    @classmethod
    def getBlockCenterCoord(cls, xpos, ypos, numOfBlocksInX, numOfBlocksInY):
        return {'x':Constant.BLOCK_WIDTH * xpos - numOfBlocksInX, 'y':Constant.BLOCK_WIDTH * ypos - numOfBlocksInY}