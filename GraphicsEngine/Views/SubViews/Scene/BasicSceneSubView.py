import ogre.renderer.OGRE as ogre

# Base Class for all scene Modes. Stores default information for action handlers.--------------------------------------#
class BasicSceneSubView (object):
    """Base Class for scene modes"""

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, mode):
        self.modeName = mode

    # Initialises the scene mode. Meant to be over-ridden--------------------------------------------------------------#
    def initialize(self):
        pass

    # Cleans up all resources used by Basic Scene Mode-----------------------------------------------------------------#
    def cleanUp(self):
        pass
