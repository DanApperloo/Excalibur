class ScreenFlowModel(object):

    # Only one flow path loaded at a time------------------------------------------------------------------------------#
    __singleton = None

    def __init__(self, flow):
        self.flowPaths = flow
        ScreenFlowModel.__singleton = self

    @classmethod
    def getSingleton(cls):
        return cls.__singleton

    @classmethod
    def cleanUp(cls):
        cls.__singleton = None
