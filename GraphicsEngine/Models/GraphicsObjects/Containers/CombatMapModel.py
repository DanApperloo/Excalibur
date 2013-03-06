# Constants defining the size of each tile orientation
from GraphicsEngine.Factories.GraphicsObjects.Groups.GroupFactory import GroupFactory
from GraphicsEngine.Models.GraphicsObjects.Groups.ProjectorGroup import ProjectorGroup
from Utilities.LoggingUtilities.LoggingUtil import *
import Storage.Constants as Constant
from GraphicsEngine.Models.GraphicsObjects.Containers.BaseSceneContainer import BaseSceneContainer
from GraphicsEngine.Models.GraphicsObjects.CombatMapLogistics.SquareProjector import SquareProjector

class CombatMapModel(BaseSceneContainer):
    """CombatMap is used to interact with and store information used in the combat map"""

    logger = LoggingUtil('CombatMapModel')

    inputMapping = {'CharacterPlacementIn':'charInitialPlacement'}

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, sceneManagerIn, inputLayout, meshsIn, name = "DefaultCombatMapModel"):
        """Creates a combat map model.

        Required Parameters:
        sceneManagerIn - the SceneManager, used to create nodes
        inputLayout - the 3 dimensional array depicting the map layout
        meshsIn - a list of meshes to use in the map
        """
        self.logger.logDebug("Constructor called for CombatMapModel: {0}".format(name))
        self.name = name
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
        self.charInitialPlacement = None
        # Save as Singleton
        CombatMapModel.setSingleton(self)

    # Initialises the combat map---------------------------------------------------------------------------------------#
    def initialize(self):
        """Initialises the graphics objects and sets up the combat map."""
        self.logger.logDebug("Initializing CombatMapModel '{0}'".format(self.name))
        self.cameraPosition = Constant.INITIAL_CAMERA_POSITION
        self.sceneManager.ambientLight = Constant.COMBAT_SCENE_AMBIENT_LIGHT
        self.rotationalNode = self.sceneManager.getRootSceneNode().createChildSceneNode("Rotation Node", (0, 0, 0))

    # Generates the base
    def generateMap(self, mapLayout):
        self.logger.logDebug("Generating Combat Map")
        # Create the selection projectors
        self.projectors = GroupFactory.createCombatBlockHighlightingGroup((len(self.layout), len(self.layout[0])), self.name)
        self.projectors.initialize()

        # Create the MapBlock Version of the CombatMapModel
        self.mapBlocks = GroupFactory.createCombatMapBlockGroup(self.layout, (len(self.layout), len(self.layout[0])), self.name)
        self.mapBlocks.initialize()

        # Tie the projectors to the map blocks
        self.projectors.tieToMapBlocks(self.mapBlocks.getBlockArray())

    def placeCharacters(self, characterTray):
        self.logger.logDebug("Placing characters")
        # Set up the sprites
        self.sprites = GroupFactory.createCombatSpriteDrawableGroup((len(self.layout[0]), len(self.layout)))
        self.sprites.createSprite("TestUnique", "dog", 8, 7)
        self.sprites.createSprite("TestUnique2", "pikachu", 7, 9)

    def showPattern(self):
        self.projectors.addPattern(Constant.MOVEMENT, SquareProjector.ATTACK_BOX, (6, 6))
        self.projectors.addPattern(Constant.ATTACK, SquareProjector.MOVE_BOX)
        self.projectors.movePattern(ProjectorGroup.UP)
        self.projectors.movePattern(ProjectorGroup.UP)
        self.projectors.addPattern(Constant.MOVEMENT, SquareProjector.TARGET_BOX)
        self.projectors.movePattern(ProjectorGroup.DOWN)
        self.projectors.movePattern(ProjectorGroup.DOWN)
        self.projectors.movePattern(ProjectorGroup.DOWN)
        # Create the selection pointer
        self.projectors.createPointer()
        self.projectors.getPointer().showAll()

    def showMap(self):
        self.logger.logDebug("Showing CombatMapModel")
        self.mapBlocks.showAll()
        self.sprites.showAll()

    def hideMap(self):
        self.logger.logDebug("Hiding CombatMapModel")
        self.mapBlocks.hideAll()
        self.sprites.hideAll()

    # Frees any used resources of the combat map-----------------------------------------------------------------------#
    def cleanUp(self):
        self.logger.logDebug("Releasing resources for CombatMapMode {0}".format(self.name))
        del self.name
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