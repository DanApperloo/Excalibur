from Utilities.LoggingUtilities.LoggingUtil import *
from GraphicsEngine.Models.GraphicsObjects.Containers.BaseSceneContainer import BaseSceneContainer
from GraphicsEngine.Models.GraphicsObjects.Entities.StaticBackground import StaticBackground
import ogre.gui.CEGUI as CEGUI

class FlatImagesModel(BaseSceneContainer):

    logger = LoggingUtil('FlatImagesModel')

    def __init__(self, modeName, guiSheet, useStaticBackground = False, name = "DefaultFlatImagesModel"):
        self.logger.logDebug("Constructor called for FlatImagesModel: {0}".format(name))
        self.name = name
        BaseSceneContainer.__init__(self, self.__class__)
        self.modeName = modeName
        self.GUISheet = guiSheet
        self.useStaticBackground = useStaticBackground
        self.staticBackground = None
        self.images = []
        BaseSceneContainer.setSingleton(self)

    # Initialises the mode by loading images---------------------------------------------------------------------------#
    def initialize(self):   # TODO If Image doesn't exist, currently just doesnt show. Needs to error out.
        self.logger.logDebug("Initializing FlatImagesModel '{0}'".format(self.name))
        if self.useStaticBackground is True:
            # Load an image to use as a background
            imageName = self.modeName + "/BackgroundImage" # Must correspond to the file described in GraphicsEngineMain
            self.staticBackground = StaticBackground(imageName, self.modeName)
            self.staticBackground.initialize()
            self.GUISheet.addChildWindow(self.staticBackground.getBackground())
        # TODO Do more things with sprites that can move

    # Cleans up any resources used by the mode-------------------------------------------------------------------------#
    def cleanUp(self):
        self.logger.logDebug("Releasing resources for FlatImagesModel '{0}'".format(self.name))
        del self.name
        if self.useStaticBackground is True:
            self.GUISheet.removeChildWindow(self.staticBackground.getBackground())
            self.staticBackground.cleanUp()
        self.removeSingleton()
