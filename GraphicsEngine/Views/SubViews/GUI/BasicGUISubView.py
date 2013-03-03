import ogre.gui.CEGUI as CEGUI
from Storage.RuntimeStorage import RuntimeStorage
from Utilities.GraphicsUtilities.GraphicsUtility import GraphicsUtility

# Constants------------------------------------------------------------------------------------------------------------#
TRAVERSABLE_KEYWORD = '-Clickable'

# Loads and initialises the GUI----------------------------------------------------------------------------------------#
class BasicGUISubView(object):
    """Loads and initialises the GUI layout"""

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, mode, guiSheet, schemeFile, layoutFile):
        self.modeName = mode
        self.scheme = schemeFile
        self.layout = layoutFile
        self.GUISheet = guiSheet
        self.windowManager = None
        self.ui = None
        self.elementTraversalList = list()

    # Initialises the mode---------------------------------------------------------------------------------------------#
    def initialise(self):
        self.windowManager = CEGUI.WindowManager.getSingleton()
        self.ui = self.windowManager.loadWindowLayout(self.layout, self.modeName + '/')
        GraphicsUtility.effectRecursiveChildWindow(self, self.ui, self.addToTraversalMethod())
        self.setMousePositionAndStore()
        self.GUISheet.addChildWindow(self.ui)

    # Load the initial Mouse Position or hide if no mouse required-----------------------------------------------------#
    def setMousePositionAndStore(self):
        # Store information for input access
        RuntimeStorage.storage['UITraversalList'] = self.elementTraversalList
        RuntimeStorage.storage['UITraversalIndex'] = 0
        # If there are elements to press
        if self.elementTraversalList:
            # Show the mouse cursor
            CEGUI.MouseCursor.getSingleton().show()
            firstElement = RuntimeStorage.storage['UITraversalList'][0]
            GraphicsUtility.putPointerOnElement(firstElement)
        else:
            # Hide mouse because there are no buttons to press
            CEGUI.MouseCursor.getSingleton().hide()

    # Per Child Window method that adds appropriate windows to list----------------------------------------------------#
    def addToTraversalMethod(self):
        # Defines a function to add the buttons to a traversable list
        def addToTraversal(self, addToList):
            if TRAVERSABLE_KEYWORD in str(addToList.getName()):
                self.elementTraversalList.append(addToList)
        # Returns the function
        return addToTraversal

    def registerHandlers(self):
        pass

    # Cleans up any resources used by BasicGUISubView--------------------------------------------------------------------------#
    def cleanUp(self):
        self.elementTraversalList = []
        RuntimeStorage.storage['UITraversalList'] = []
        self.GUISheet.removeChildWindow(self.ui)
        self.windowManager.destroyWindow(self.ui)