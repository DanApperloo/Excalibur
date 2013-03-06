from GraphicsEngine.Models.GraphicsObjects.Drawables.Drawable import *

class EntityDrawable(Drawable):
    """Holds and controls the Graphics for 3d Images"""

    def __init__(self, sceneManager, parentNode, name, resourceName):
        """Base Constructor of Drawable.
        Create the block and attach it to a Scene Node

        Keyword Arguments:
        sceneManager -- Reference to the OGRE sceneManager
        parentNode -- The parent node of the entity
        name -- The unique name of the block
        resourceName -- The location/name of the resource to use for the node

        """
        Drawable.__init__(self, sceneManager, parentNode, name)
        self.entity = self.sceneManager.createEntity(name + " Entity", resourceName)
        self.attachObject(self.entity)
        self.setVisible(False)

    def setPosition(self, position):
        """Implements Base class method"""
        Drawable.setPosition(self, position)

    def isVisible(self):
        """Returns if the Entity is visible or not"""
        return self.getNode().getAttachedObject(0).isVisible()

    def setVisible(self, visible):
        """Sets if the Entity is visible"""
        self.getNode().getAttachedObject(0).setVisible(visible)

    def cleanUp(self):
        self.sceneManager.destroyEntity(self.entity)
        del self.entity
        Drawable.cleanUp(self)
