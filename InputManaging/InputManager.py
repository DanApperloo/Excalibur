import ogre.io.OIS as OIS
from InputManaging.ControlEvents import ControlEvents
from InputManaging.FrameActionCenter import *

# Input Manager Class handles the Input from the screen at the highest level-------------------------------------------#
class InputManager(object):

    # Class Variables--------------------------------------------------------------------------------------------------#
    __singleton = None
    # -----------------------------------------------------------------------------------------------------------------#

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, OGRERoot, OGREWindow):
        self.__setUp(OGRERoot, OGREWindow)
        InputManager.__singleton = self

    # Initialises the Input Manager in the correct sequence------------------------------------------------------------#
    def __setUp(self, OGRERoot, OGREWindow):
        self._setupInputSystem(OGREWindow)
        self._tieInListeners(OGRERoot)

    # Initialises the OIS input system, ie. Keyboard and Mouse---------------------------------------------------------#
    def _setupInputSystem(self, window):
        windowHandle = window.getCustomAttributeInt("WINDOW")             # Retrieve a pointer to the Game Window
        paramList = [("WINDOW", str(windowHandle))]                       # Setup way for OIS to communicate with Window
        self.inputManager = OIS.createPythonInputSystem(paramList)        # Create OIS Input Manager to allow interaction
        # Now InputManager is initialized for use. Keyboard and Mouse objects must still be initialized separately
        try:
            # Enable Keyboard Input
            self.keyboard = self.inputManager.createInputObjectKeyboard(OIS.OISKeyboard, True)
            # Enable Mouse Input
            self.mouse = self.inputManager.createInputObjectMouse(OIS.OISMouse, True)
        except Exception, e:
            raise e

    # Registers Listeners into OGRE Root-------------------------------------------------------------------------------#
    def _tieInListeners(self, root):
        self.frameListener = FrameActionCenter(self.keyboard, self.mouse)  # Create the main Frame Listener
        root.addFrameListener(self.frameListener)                          # Attach the Listener to the OGRE Root

    def setControlEvent(self, controlEventIn):
        self.frameListener.setControlEvent(controlEventIn)

    def getControlEvent(self):
        return self.frameListener.getControlEvent()

    def flushControlEvent(self):
        self.frameListener.setControlEvent(ControlEvents.NO_EVENT)

    # Gets the instance of the class-----------------------------------------------------------------------------------#
    @classmethod
    def getSingleton(cls):
        if cls.__singleton is not None:
            return cls.__singleton
        else:
            raise Exception("InputManager is not initialised.\
             Please initialise InputManager before retrieving an instance.")

    # Cleans up resources----------------------------------------------------------------------------------------------#
    def cleanUp(self):
        InputManager.__singleton = None
        self.inputManager.destroyInputObjectKeyboard(self.keyboard)         # Delete OIS Keyboard
        self.inputManager.destroyInputObjectMouse(self.mouse)               # Delete OIS Mouse
        OIS.InputManager.destroyInputSystem(self.inputManager)              # Delete OIS Input Manager
        if self.frameListener is not None: del self.frameListener           # Delete Frame Listeners

