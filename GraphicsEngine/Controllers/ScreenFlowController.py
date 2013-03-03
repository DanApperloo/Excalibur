from GraphicsEngine.Models.Flow.ScreenFlowModel import ScreenFlowModel

class ScreenFlowController(object):

    @classmethod
    def createScreenFlow(cls, params):
        if ScreenFlowModel.getSingleton() is None:
            ScreenFlowModel(params)
        else:
            raise Exception('The new ScreenFlowModel could not be loaded as one already exists.')

    @classmethod
    def removeScreenFlow(cls):
        if ScreenFlowModel.getSingleton() is not None:
            ScreenFlowModel.cleanUp()
        else:
            raise Exception("The ScreenFlowModel could not be deleted since it doesn't exist.")
