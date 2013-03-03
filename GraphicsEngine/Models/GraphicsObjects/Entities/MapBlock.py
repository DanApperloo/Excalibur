import ogre.renderer.OGRE as ogre
from GraphicsEngine.Models.GraphicsObjects.Drawables.EntityDrawable import EntityDrawable

class MapBlock(EntityDrawable):
    """MapBlock is used to store information for the Combat CombatMapModel tiles and draw them"""

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self, sceneManager, parentNode, meshFile, xpos, ypos, zpos = 0):
        """Creates an individual map block.

        Required Parameters:
        sceneManager - the OGRE Scene Manager
        parentNode - the root node for the parent combat map
        meshFile - the name of the map block's mesh
        xpos - the designed block layout X position
        ypos - the designed block layout Y position
        zpos - the designed block layout Z position (default = 0)
        """
        # BlockImageSet
        EntityDrawable.__init__(self, sceneManager, parentNode)
        self.mesh = meshFile
        # Level of Block and initial array position
        self.staticPosition = (xpos, ypos, zpos)
        # Stores the edited base materials so that they can be deleted
        self.workingMaterials = None

    # Initialises the map block----------------------------------------------------------------------------------------#
    def initialise(self):
        """Sets up the map block. Clones the used material so that it may be edited."""
        EntityDrawable.initialise(self, "{0!s}:{1!s} MapBlock".format(self.staticPosition[0], self.staticPosition[1]), self.mesh)
        self.setPosition((self.staticPosition[0], 0, self.staticPosition[1]))
        # Clones all materials to allow projections to appear
        self.workingMaterials = []
        for i in range(self.entity.getNumSubEntities()):
            realMaterial = self.entity.getSubEntity(i).getMaterial()
            newMaterial = realMaterial.clone("{0} {1!s}:{2!s}".format(realMaterial.getName(), self.staticPosition[0], self.staticPosition[1]))
            newMaterial.load()
            self.entity.getSubEntity(i).setMaterial(newMaterial)
            # Stores the new materials so that they can be deleted
            self.workingMaterials.append(newMaterial)

    def show(self):
        if not self.isVisble():
            self.setVisible(True)

    def hide(self):
        if self.isVisble():
            self.setVisible(False)

    # Returns the designed position of the map block-------------------------------------------------------------------#
    def getStaticPosition(self):
        return self.staticPosition

    # Frees any used resources-----------------------------------------------------------------------------------------#
    def cleanUp(self):
        for material in self.workingMaterials:
            # Remove the material from the manager so that it may be deleted
            ogre.MaterialManager.getSingleton().remove(material)
        del self.workingMaterials
        EntityDrawable.cleanUp(self)