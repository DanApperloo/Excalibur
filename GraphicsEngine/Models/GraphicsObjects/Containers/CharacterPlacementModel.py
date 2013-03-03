# Constants defining the size of each tile orientation
import ogre.renderer.OGRE as ogre
import Storage.Constants as Constant
from Utilities.LoggingUtilities.LoggingUtil import *
from GraphicsEngine.Models.GraphicsObjects.Containers.BaseSceneContainer import BaseSceneContainer
from GraphicsEngine.Models.GraphicsObjects.CombatMapLogistics.ProjectorGroup import ProjectorGroup
from GraphicsEngine.Models.GraphicsObjects.CombatMapLogistics.SquareProjector import SquareProjector
from GraphicsEngine.Models.GraphicsObjects.Entities.MapBlockGroup import MapBlockGroup
from GraphicsEngine.Models.GraphicsObjects.Drawables.SpriteDrawableGroup import SpriteDrawableGroup

class CharacterPlacementModel(BaseSceneContainer):
    """CombatMap is used to interact with and store information used in the combat map"""

    logger = LoggingUtil('CharacterPlacementModel')

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, sceneManagerIn, inputLayout, meshIn, name = "DefaultCharacterPlacementModel"):
        """Creates a combat map model.

        Required Parameters:
        sceneManagerIn - the SceneManager, used to create nodes
        inputLayout - the 2 dimensional array depicting the placement layout
        meshIn - the mesh to use for the placement blocks
        """
        self.logger.logDebug("Constructor called for CharacterPlacementModel: {0}".format(name))
        self.name = name
        BaseSceneContainer.__init__(self, self.__class__)
        self.sceneManager = sceneManagerIn
        # 3 dimensional array depicting block layout of map
        self.layout = inputLayout
        # Create List of all texture files used in map
        self.mesh = meshIn
        # Create groups for the entities
        self.projectors = None
        self.mapBlocks = None
        self.sprites = None
        # Save as Singleton
        CharacterPlacementModel.setSingleton(self)

    # Initialises the combat map---------------------------------------------------------------------------------------#
    def initialize(self):
        """Initialises the graphics objects and sets up the combat map."""
        self.logger.logDebug("Initializing CharacterPlacementModel '{0}'".format(self.name))
        self.cameraPosition = Constant.INITIAL_CAMERA_POSITION
        self.sceneManager.ambientLight = Constant.COMBAT_SCENE_AMBIENT_LIGHT
        self.rotationalNode = self.sceneManager.getRootSceneNode().createChildSceneNode("Rotation Node", (0, 0, 0))

    # Generates the base
    def generatePlacementGrid(self):
        # Create the selection projectors
        self.projectors = ProjectorGroup(self.sceneManager, self.rotationalNode, (len(self.layout[0]), len(self.layout)))
        self.projectors.initialize()

        # Create the MapBlock Version of the CombatMapModel
        self.mapBlocks = MapBlockGroup(self.sceneManager, self.rotationalNode, self.layout, [self.mesh], (len(self.layout[0]), len(self.layout)))
        self.mapBlocks.initialize()

        # Tie the projectors to the map blocks
        self.projectors.tieToMapBlocks(self.mapBlocks.getBlockArray())

    def showPlacementGrid(self):
        self.logger.logDebug("Showing Placement Grid")
        if self.mapBlocks is not None: self.mapBlocks.showAll()
        if self.sprites is not None: self.sprites.showAll()

    def hidePlacementGrid(self):
        self.logger.logDebug("Hiding Placement Grid")
        if self.mapBlocks is not None: self.mapBlocks.hideAll()
        if self.sprites is not None: self.sprites.hideAll()

    # Frees any used resources of the combat map-----------------------------------------------------------------------#
    def cleanUp(self):
        self.logger.logDebug("Releasing resources for CharacterPlacementModel {0}".format(self.name))
        del self.name
        # Free the tile projector
        if self.projectors is not None: self.projectors.cleanUp()
        del self.projectors
        # Free the map blocks
        if self.mapBlocks is not None: self.mapBlocks.cleanUp()
        del self.mapBlocks
        # Free the character sprites
        if self.sprites is not None: self.sprites.cleanUp()
        del self.sprites
        # Free the used scene nodes
        self.sceneManager.getRootSceneNode().removeAndDestroyChild(self.rotationalNode.getName())
        del self.rotationalNode
        # Unlink the scene singleton so that other scenes may be used
        self.removeSingleton()