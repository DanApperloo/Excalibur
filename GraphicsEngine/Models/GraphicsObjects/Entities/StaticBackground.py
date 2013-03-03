import ogre.gui.CEGUI as CEGUI

class StaticBackground(object):

    def __init__(self, imageName, attachToWindowModeName):
        self.imageName = imageName
        self.attachTo = attachToWindowModeName
        self.background = None

    def initialise(self):
        # Here we will use a StaticImage as the root, then we can use it to place a background image
        self.background = CEGUI.WindowManager.getSingleton().createWindow("TaharezLook/StaticImage", self.attachTo + "/backgroundWND")
        # Set position and size
        self.background.setPosition(CEGUI.UVector2(self.__ceguiRealDim(0), self.__ceguiRealDim(0)))
        self.background.setSize(CEGUI.UVector2(self.__ceguiRealDim(1), self.__ceguiRealDim(1)))
        # Disable frame and standard background
        self.background.setProperty("FrameEnabled", "false")
        self.background.setProperty("BackgroundEnabled", "false")
        # Set the background image
        self.background.setProperty("Image", "set:" + self.imageName + " image:full_image")

    def getBackground(self):
        return self.background

    # Utility function to transform co-ordinates for CEGUI-------------------------------------------------------------#
    def __ceguiRealDim (self, x ) :
        return CEGUI.UDim((x),0)

    def cleanUp(self):
        if self.background is not None:
            CEGUI.WindowManager.getSingleton().destroyWindow(self.background)