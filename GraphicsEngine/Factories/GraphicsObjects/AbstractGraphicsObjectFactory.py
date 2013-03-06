class AbstractGraphicsObjectFactory(object):

    sceneManager = None
    rootNode = None

    @classmethod
    def setSceneManager(cls, sceneManagerIn):
        cls.sceneManager = sceneManagerIn
        cls.rootNode = sceneManagerIn.getRootSceneNode()