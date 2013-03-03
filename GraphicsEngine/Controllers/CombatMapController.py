from GraphicsEngine.Models.GraphicsObjects.Containers.CombatMapModel import CombatMapModel

class CombatMapController(object):

    @classmethod
    def createCombatMap(cls, params):
        if CombatMapModel.canCreate() is True:
            combatMap = CombatMapModel(params[0], params[1], params[2])
            combatMap.initialise()
            combatMap.generateMap('MapINPUT')
            combatMap.placeCharacters('CHARACTERPANEL')
            combatMap.showMap()
            combatMap.showPattern()
        else:
            raise Exception('CombatMapController cannot create the CombatMapModel because a SceneContainer still exists.')

    @classmethod
    def deleteCombatMap(cls):
        if CombatMapModel.canDelete() is True:
            CombatMapModel.getSingleton().cleanUp()
        else:
            raise Exception("CombatMapController cannot delete the CombatMapModel because it doesn't exist")