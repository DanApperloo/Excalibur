from Storage.BasicStorage import BasicStorage
from GraphicsEngine.Controllers.ScreenFlowController import ScreenFlowController

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
    def initialise(self):
        self.scene.initialise()
        self.gui.initialise()
        self.gui.registerHandlers()
        ScreenFlowController.createScreenFlow(self.nextModes)

    # Cleans up used resources-----------------------------------------------------------------------------------------#
    def cleanUp(self):
        self.gui.cleanUp()
        self.scene.cleanUp()
        ScreenFlowController.removeScreenFlow()