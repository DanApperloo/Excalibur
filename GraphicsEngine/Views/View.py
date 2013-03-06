from Storage.BasicStorage import BasicStorage

# Controls the specifications and reactions for each game mode---------------------------------------------------------#
class View ( object ):
    """Controls the input reactions, UI layout and scene of the game mode"""

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, name, sceneMode, guiMode, nextModes):
        self.mode = name
        self.scene = BasicStorage.getSceneMode(sceneMode)
        self.gui = BasicStorage.getGUIMode(guiMode)
        self.nextModes = nextModes

    # Sets up the game mode with it's child modes----------------------------------------------------------------------#
    def initialize(self):
        self.scene.initialize()
        self.gui.initialize()
        self.gui.registerHandlers()

    def getTransition(self):
        return self.scene.getTransition(self.nextModes[0])

    # Cleans up used resources-----------------------------------------------------------------------------------------#
    def cleanUp(self):
        self.gui.cleanUp()
        self.scene.cleanUp()