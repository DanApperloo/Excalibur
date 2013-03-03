from GraphicsEngine.Views.SubViews.Scene.BasicSceneSubView import *
from GraphicsEngine.Controllers.CombatMapController import CombatMapController

class CombatMapSubView(BasicSceneSubView):
    """Controls the combat map mode"""

    def __init__(self, nameIn, sceneManagerIn, inputLayout, meshsIn):
        BasicSceneSubView.__init__(self, nameIn)
        self.sceneManager = sceneManagerIn
        self.layout = inputLayout
        self.meshs = meshsIn

    def initialize(self):
        CombatMapController.createCombatMap((self.sceneManager, self.layout, self.meshs))

    def cleanUp(self):
        CombatMapController.deleteCombatMap()

    def __del__(self):
        self.sceneManager = None
        self.layout = None
        self.mesh = None

