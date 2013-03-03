from GraphicsEngine.Views.SubViews.Scene.BasicSceneSubView import *
from GraphicsEngine.Controllers.BackgroundController import BackgroundController

# Controls any game mode that has a flat image as the screen-----------------------------------------------------------#
class BackgroundSubView(BasicSceneSubView):
    """Controls the static background scene mode"""

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, nameIn, guiSheet):
        BasicSceneSubView.__init__(self, nameIn)
        self.GUISheet = guiSheet

    # Initialises the mode by loading images---------------------------------------------------------------------------#
    def initialise(self):
        BackgroundController.createBackground((self.modeName, self.GUISheet))

    # Cleans up any resources used by the mode-------------------------------------------------------------------------#
    def cleanUp(self):
        BackgroundController.deleteBackground()

    def __del__(self):
        self.GUISheet = None


