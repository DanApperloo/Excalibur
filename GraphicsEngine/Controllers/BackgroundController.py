from GraphicsEngine.Models.GraphicsObjects.Containers.FlatImagesModel import FlatImagesModel

class BackgroundController(object):

    @classmethod
    def createBackground(cls, params):
        if FlatImagesModel.canCreate() is True:
            background  = FlatImagesModel(params[0], params[1], True)
            background.initialise()
        else:
            raise Exception('BackgroundController cannot create the FlatImagesModel because a SceneContainer still exists.')

    @classmethod
    def deleteBackground(cls):
        if FlatImagesModel.canDelete() is True:
            FlatImagesModel.getSingleton().cleanUp()
        else:
            raise Exception("BackgroundController cannot delete the FlatImagesModel because it doesn't exist")