import ogre.renderer.OGRE as ogre
import ogre.gui.CEGUI as CEGUI
import ogre.io.OIS as OIS
from Storage.RuntimeStorage import RuntimeStorage
from Utilities.GraphicsUtilities.GraphicsUtility import GraphicsUtility

CONTROL_ACTIONS = ['NONE', 'CHANGE_MODE']

# Below is a hack, unsure why
def _PointHack(x, y):
    return CEGUI.Vector2(x, y)
CEGUI.Point = _PointHack

# FrameActionCenter Class----------------------------------------------------------------------------------------------#
class FrameActionCenter(ogre.FrameListener , OIS.KeyListener, OIS.MouseListener):
    """The Main FrameListener for the game. Controls all input and sends to UI."""

    # Constructor------------------------------------------------------------------------------------------------------#
    def __init__(self, keyboardIn, mouseIn):
        """
        Constructor for FrameActionCenter. Requires Keyboard and Mouse OIS objects.

        Parameters:
        keyboardIn -- OIS Keyboard object to read
        mouseIn -- OIS Mouse object to read
        """
        ogre.FrameListener.__init__(self)
        OIS.KeyListener.__init__(self)
        OIS.MouseListener.__init__(self)
        self.mouse = mouseIn
        self.keyboard = keyboardIn
        self.mouse.setEventCallback(self)
        self.keyboard.setEventCallback(self)
        self.controlAction = CONTROL_ACTIONS[0]
        self.shutdownRequested = False
        self.changeModeRequested = False

    # Private Helper Method to capture all Input into system-----------------------------------------------------------#
    def capture(self):
        self.mouse.capture()
        self.keyboard.capture()

    # Private Helper Method to convert OIS Input to UI Input-----------------------------------------------------------#
    def convertOISMouseButtonToCegui(self, buttonID):
        if buttonID ==0:
            return CEGUI.LeftButton
        elif buttonID ==1:
            return CEGUI.RightButton
        elif buttonID ==2:
            return CEGUI.MiddleButton
        elif buttonID ==3:
            return CEGUI.X1Button
        else:
            return CEGUI.LeftButton

    # Handle Frame Starting--------------------------------------------------------------------------------------------#
    def frameStarted(self, evt):
        return ogre.FrameListener.frameStarted(self, evt)

    # Handle Frame Ending---Exit if required---------------------------------------------------------------------------#
    def frameEnded(self, evt):
        if self.shutdownRequested:
            return False
        else:
            return ogre.FrameListener.frameEnded(self, evt)

    # Handle Key Pressed and send event to UI---Deals with all Non-UI based key interaction first----------------------#
    def keyPressed(self, arg):
        print "KeyDown: " + str(arg.key)
        if arg.key == OIS.KC_ESCAPE:
            self.shutdownRequested = True
        if arg.key == OIS.KC_M:
            self.changeModeRequested = True
        if arg.key == OIS.KC_S or arg.key == OIS.KC_W:
            traversalList = RuntimeStorage.storage['UITraversalList']
            mod = len(traversalList)
            if mod is not 0:
                if arg.key == OIS.KC_S:
                    increment = 1
                else:
                    increment = -1
                newElementIndex = (RuntimeStorage.storage['UITraversalIndex'] + increment) % mod
                RuntimeStorage.storage['UITraversalIndex'] = newElementIndex
                focusedElement = RuntimeStorage.storage['UITraversalList'][newElementIndex]
                GraphicsUtility.putPointerOnElement(focusedElement)
        if arg.key == OIS.KC_N:
            CEGUI.System.getSingleton().injectMouseButtonDown(self.convertOISMouseButtonToCegui(id))
        CEGUI.System.getSingleton().injectKeyDown(arg.key)
        CEGUI.System.getSingleton().injectChar(arg.text)
        return True

    # Handle Key Released and send event to UI-------------------------------------------------------------------------#
    def keyReleased(self, arg):
        print "KeyUp: " + str(arg.key)
        CEGUI.System.getSingleton().injectKeyUp(arg.key)
        CEGUI.System.getSingleton().injectMouseButtonUp(self.convertOISMouseButtonToCegui(id))

    # Handle Mouse Moved but don't send event to UI--------------------------------------------------------------------------#
    def mouseMoved(self, arg):
        return True

    # Handle Mouse Pressed but don't send event to UI------------------------------------------------------------------------#
    def mousePressed(self, arg, id):
        return True

    # Handle Mouse Released but don't send event to UI-----------------------------------------------------------------------#
    def mouseReleased(self, arg, id):
        return True