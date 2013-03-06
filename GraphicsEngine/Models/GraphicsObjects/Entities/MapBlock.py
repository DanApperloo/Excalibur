import ogre.renderer.OGRE as ogre
from Utilities.LoggingUtilities.LoggingUtil import *
from GraphicsEngine.Models.GraphicsObjects.Drawables.EntityDrawable import EntityDrawable

class MapBlock(EntityDrawable):
    """MapBlock is used to store information for the Combat CombatMapModel tiles and draw them"""

    logger = LoggingUtil('MapBlock')

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, sceneManager, parentNode, parentMapBlockGroup, meshFile, staticIn, xpos, ypos, zpos, name):
        """Creates an individual map block.

        Required Parameters:
        sceneManager - the OGRE Scene Manager
        parentNode - the root node for the parent combat map
        parentMapBlockGroup - the parent MapBlockGroup
        meshFile - the name of the map block's mesh
        xpos - the designed block layout X position
        ypos - the designed block layout Y position
        zpos - the designed block layout Z position
        """
        EntityDrawable.__init__(self, sceneManager, parentNode, name, meshFile)
        self.logger.logDebug("Constructor called for MapBlock: {0}".format(name))
        self.name = name
        self.parentMapBlockGroup = parentMapBlockGroup
        # BlockImageSet
        self.mesh = meshFile
        # Level of Block and initial array position
        self.realPosition = (xpos, ypos, zpos)
        self.staticPosition = staticIn
        # Clones all materials to allow projections to appear
        self.workingMaterials = []

    def __cloneMaterials(self):
        clones = []
        for i in range(self.entity.getNumSubEntities()):
            realMaterial = self.entity.getSubEntity(i).getMaterial()
            newMaterial = realMaterial.clone("{0} {1!s}:{2!s}".format(realMaterial.getName(), self.staticPosition[0], self.staticPosition[1]))
            newMaterial.load()
            self.entity.getSubEntity(i).setMaterial(newMaterial)
            # Stores the new materials so that they can be deleted
            clones.append(newMaterial)
        return clones

    def initialize(self):
        self.setPosition((self.realPosition[0], self.realPosition[2], self.realPosition[1]))
        self.workingMaterials = self.__cloneMaterials()

    def show(self):
        if not self.isVisible():
            self.setVisible(True)

    def hide(self):
        if self.isVisible():
            self.setVisible(False)

    # Returns the designed position of the map block-------------------------------------------------------------------#
    def getStaticPosition(self):
        return self.staticPosition

    # Frees any used resources-----------------------------------------------------------------------------------------#
    def cleanUp(self):
        self.logger.logDebug("Releasing resources for MapBlock '{0}'".format(self.name))
        del self.name
        for material in self.workingMaterials:
            # Remove the material from the manager so that it may be deleted
            ogre.MaterialManager.getSingleton().remove(material)
        del self.workingMaterials
        self.parentMapBlockGroup = None
        del self.parentMapBlockGroup
        EntityDrawable.cleanUp(self)