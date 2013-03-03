from GraphicsEngine.Models.GraphicsObjects.Drawables.Drawable import *

class EntityDrawable(Drawable):
    """Holds and controls the Graphics for 3d Images"""

    def __init__(self, sceneManager, parentNode):
        """Base Constructor of Drawable"""
        Drawable.__init__(self,sceneManager, parentNode)
        self.entity = None

    def initialise(self, name, resourceName):
        """Create the block and attach it to a Scene Node

        Keyword Arguments:
        name -- The unique name of the block
        resourceName -- The location/name of the resource to use for the node

        """
        self.entity =  self.sceneManager.createEntity(name + " Entity", resourceName)
        self.createNode(name)
        self.attachObject(self.entity)
        self.setVisible(False)

    def setPosition(self, position):
        """Implements Base class method"""
        Drawable.setPosition(self, position)

    def isVisble(self):
        """Returns if the Entity is visible or not"""
        return self.getNode().getAttachedObject(0).isVisible()

    def setVisible(self, visible):
        """Sets if the Entity is visible"""
        self.getNode().getAttachedObject(0).setVisible(visible)

    def cleanUp(self):
        self.sceneManager.destroyEntity(self.entity)
        del self.entity
        Drawable.cleanUp(self)
