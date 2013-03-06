from GraphicsEngine.Models.GraphicsObjects.Containers.CharacterPlacementModel import CharacterPlacementModel
from GraphicsEngine.Controllers.TransitionManager import TransitionManager

class CharacterPlacementController(object):

    @classmethod
    def createCharacterPlacement(cls, params):
        if CharacterPlacementModel.canCreate() is True:
            characterPlacement = CharacterPlacementModel(params[0], params[1], params[2])
            characterPlacement.initialize()
            characterPlacement.generatePlacementGrid()
            characterPlacement.showPlacementGrid()
        else:
            raise Exception('CharacterPlacementController cannot create the CharacterPlacementModel because a SceneContainer still exists.')

    @classmethod
    def getTransition(cls, transitionTypeKey):
        return TransitionManager.getSingleton().createTransitionFromTypeAndSource(transitionTypeKey, CharacterPlacementModel.getSingleton())

    @classmethod
    def deleteCharacterPlacement(cls):
        if CharacterPlacementModel.canDelete() is True:
            CharacterPlacementModel.getSingleton().cleanUp()
        else:
            raise Exception("CharacterPlacementController cannot delete the CharacterPlacementModel because it doesn't exist")