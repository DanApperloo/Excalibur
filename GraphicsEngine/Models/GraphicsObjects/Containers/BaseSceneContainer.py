class BaseSceneContainer(object):

    # Can only be one base container initialised at a time--------------------------------------------------------------#
    __singleton = None

    def __init__(self, type):
        self.type = type

    def setSingleton(self):
        if BaseSceneContainer.__singleton is None:
            BaseSceneContainer.__singleton = self
        else:
            raise Exception('BaseSceneContainer cannot set Singleton because it already exists.')

    def removeSingleton(self):
        if BaseSceneContainer.__singleton is not None:
            BaseSceneContainer.__singleton = None
        else:
            raise Exception("BaseSceneContainer cannot remove Singleton because it doesn't exist.")

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

