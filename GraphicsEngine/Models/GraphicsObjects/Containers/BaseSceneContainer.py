from Utilities.LoggingUtilities.LoggingUtil import *

class BaseSceneContainer(object):

    logger = LoggingUtil('BaseSceneContainer')

    # Can only be one base container initialised at a time--------------------------------------------------------------#
    __singleton = None

    def __init__(self, type):
        self.logger.logDebug("Constructor called for BaseSceneContainer of type: {0}".format(type))
        self.type = type

    def setSingleton(self):
        if BaseSceneContainer.__singleton is None:
            self.logger.logDebug("Setting singleton for SceneContainer")
            BaseSceneContainer.__singleton = self
        else:
            raise Exception('BaseSceneContainer cannot set Singleton because it already exists.')

    def removeSingleton(self):
        if BaseSceneContainer.__singleton is not None:
            self.logger.logDebug("Removing singleton for SceneContainer")
            BaseSceneContainer.__singleton = None
        else:
            raise Exception("BaseSceneContainer cannot remove Singleton because it doesn't exist.")

    def mapContainerOutput(self):
        return {'NoOutput':None}

    def mapContainerInput(self):
        return {'NoInput':None}

    @classmethod
    def getSingleton(cls):
        return cls.__singleton

    @classmethod
    def canCreate(cls):
        if cls.__singleton is None:
            return True
        else:
            return False

    @classmethod
    def canDelete(cls):
        if (cls.__singleton is None) or (cls.__singleton.type is not cls.getSingleton().__class__):
            return False
        else:
            return True

