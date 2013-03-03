# Constants defining the size of each tile orientation
import ogre.renderer.OGRE as ogre
import Storage.Constants as Constant
from GraphicsEngine.Models.GraphicsObjects.Containers.BaseSceneContainer import BaseSceneContainer
from GraphicsEngine.Models.GraphicsObjects.CombatMapLogistics.ProjectorGroup import ProjectorGroup
from GraphicsEngine.Models.GraphicsObjects.CombatMapLogistics.SquareProjector import SquareProjector
from GraphicsEngine.Models.GraphicsObjects.Entities.MapBlockGroup import MapBlockGroup
from GraphicsEngine.Models.GraphicsObjects.Drawables.SpriteDrawableGroup import SpriteDrawableGroup

class CombatMapModel(BaseSceneContainer):
    """CombatMap is used to interact with and store information used in the combat map"""

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, sceneManagerIn, inputLayout, meshsIn):
        """Creates a combat map model.

        Required Parameters:
        sceneManagerIn - the SceneManager, used to create nodes
        inputLayout - the 3 dimensional array depicting the map layout
        meshsIn - a list of meshes to use in the map
        """
        BaseSceneContainer.__init__(self, self.__class__)
        self.sceneManager = sceneManagerIn
        # 3 dimensional array depicting block layout of map
        self.layout = inputLayout
        # Create List of all texture files used in map
        self.meshsUsed = meshsIn
        # Create groups for the entities
        self.projectors = None
        self.mapBlocks = None
        self.sprites = None
        # Save as Singleton
        CombatMapModel.setSingleton(self)

    # Initialises the combat map---------------------------------------------------------------------------------------#
    def initialise(self):
        """Initialises the graphics objects and sets up the combat map."""
        self.cameraPosition = Constant.INITIAL_CAMERA_POSITION
        self.sceneManager.ambientLight = Constant.COMBAT_SCENE_AMBIENT_LIGHT
        self.rotationalNode = self.sceneManager.getRootSceneNode().createChildSceneNode("Rotation Node", (0, 0, 0))

    # Generates the base
    def generateMap(self, mapLayout):
        # Create the selection projectors
        self.projectors = ProjectorGroup(self.sceneManager, self.rotationalNode, (len(self.layout[0]), len(self.layout)))
        self.projectors.initialise()

        # Create the MapBlock Version of the CombatMapModel
        self.mapBlocks = MapBlockGroup(self.sceneManager, self.rotationalNode, self.layout, self.meshsUsed, (len(self.layout[0]), len(self.layout)))
        self.mapBlocks.initialise()

        # Tie the projectors to the map blocks
        self.projectors.tieToMapBlocks(self.mapBlocks.getBlockArray())

    def placeCharacters(self, characterTray):
        # Set up the sprites
        self.sprites = SpriteDrawableGroup(self.sceneManager, self.rotationalNode, (Constant.MAP_WIDTH, Constant.MAP_HEIGHT))
        self.sprites.createSprite("TestUnique", "Link", 8, 7)
        self.sprites.createSprite("TestUnique2", "Mario", 7, 9)

    def showPattern(self):
        self.projectors.addPattern(Constant.MOVEMENT, SquareProjector.ATTACK_BOX, (6, 6))
        self.projectors.addPattern(Constant.ATTACK, SquareProjector.MOVE_BOX)
        self.projectors.movePattern(ProjectorGroup.UP)
        self.projectors.movePattern(ProjectorGroup.UP)
        self.projectors.addPattern(Constant.MOVEMENT, SquareProjector.TARGET_BOX)
        self.projectors.movePattern(ProjectorGroup.UP)
        self.projectors.movePattern(ProjectorGroup.UP)
        # Create the selection pointer
        self.projectors.createPointer()
        self.projectors.getPointer().showAll()

#    def showEffectPattern(self):
#        self.projectors.

    def showMap(self):
        self.mapBlocks.showAll()
        self.sprites.showAll()

    def hideMap(self):
        self.mapBlocks.hideAll()
        self.sprites.hideAll()

    # Frees any used resources of the combat map-----------------------------------------------------------------------#
    def cleanUp(self):
        # Free the tile projector
        self.projectors.cleanUp()
        del self.projectors
        # Free the map blocks
        self.mapBlocks.cleanUp()
        del self.mapBlocks
        # Free the character sprites
        self.sprites.cleanUp()
        del self.sprites
        # Free the used scene nodes
        self.sceneManager.getRootSceneNode().removeAndDestroyChild(self.rotationalNode.getName())
        del self.rotationalNode
        # Unlink the scene singleton so that other scenes may be used
        self.removeSingleton()