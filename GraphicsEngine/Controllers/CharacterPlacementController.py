from GraphicsEngine.Models.GraphicsObjects.Containers.CharacterPlacementModel import CharacterPlacementModel

class CharacterPlacementController(object):

    @classmethod
    def createCharacterPlacement(cls, params):
        if CharacterPlacementModel.canCreate() is True:
            characterPlacement = CharacterPlacementModel(params[0], params[1], params[2])
            characterPlacement.initialise()
            characterPlacement.generatePlacementGrid()
            characterPlacement.showPlacementGrid()
        else:
            raise Exception('CharacterPlacementController cannot create the CharacterPlacementModel because a SceneContainer still exists.')

    @classmethod
    def deleteCharacterPlacement(cls):
        if CharacterPlacementModel.canDelete() is True:
            CharacterPlacementModel.getSingleton().cleanUp()
        else:
            raise Exception("CharacterPlacementController cannot delete the CharacterPlacementModel because it doesn't exist")