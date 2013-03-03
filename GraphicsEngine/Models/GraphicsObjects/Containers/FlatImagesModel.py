from GraphicsEngine.Models.GraphicsObjects.Containers.BaseSceneContainer import BaseSceneContainer
from GraphicsEngine.Models.GraphicsObjects.Entities.StaticBackground import StaticBackground
import ogre.gui.CEGUI as CEGUI

class FlatImagesModel(BaseSceneContainer):

    def __init__(self, modeName, guiSheet, useStaticBackground = False):
        BaseSceneContainer.__init__(self, self.__class__)
        self.modeName = modeName
        self.GUISheet = guiSheet
        self.useStaticBackground = useStaticBackground
        self.staticBackground = None
        self.images = []
        BaseSceneContainer.setSingleton(self)

    # Initialises the mode by loading images---------------------------------------------------------------------------#
    def initialise(self):   # TODO If Image doesn't exist, currently just doesnt show. Needs to error out.
        if self.useStaticBackground is True:
            # Load an image to use as a background
            imageName = self.modeName + "/BackgroundImage" # Must correspond to the file described in GraphicsEngineMain
            self.staticBackground = StaticBackground(imageName, self.modeName)
            self.staticBackground.initialise()
            self.GUISheet.addChildWindow(self.staticBackground.getBackground())
        # TODO Do more things with sprites that can move

    # Cleans up any resources used by the mode-------------------------------------------------------------------------#
    def cleanUp(self):
        if self.useStaticBackground is True:
            self.GUISheet.removeChildWindow(self.staticBackground.getBackground())
            self.staticBackground.cleanUp()
        self.removeSingleton()
