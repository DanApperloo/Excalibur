class Drawable(object):
    """Base Class for any object that is drawn to scene and attached to nodes"""

    def __init__(self, sceneManager, parentNode, name):
        """Creates pointers to the Parent SceneManager and Parent Node

        Keyword Arguments:
        sceneManager -- The sceneManager to use to create entities under
        parentNode -- The Parent Node that this block will be a child of

        """
        self.sceneManager = sceneManager
        self.parentNode = parentNode
        self.node = self.parentNode.createChildSceneNode(name)

    def attachObject(self, attachee):
        """Attach an object to a node"""
        self.node.attachObject(attachee)
    
    def setPosition(self, position):
        """Sets the position of the block relative to the parent node

        Keyword Arguments:
        position -- A tuple consisting of the x, y, z co-ordinates

        """
        self.node.setPosition(position[0], position[1], position[2])

    def getPosition(self):
        """Returns the position of the block relative to the parent node"""
        return self.node.getPosition()

    def getNode(self):
        """Returns a pointer to the node in which the block is attached to"""
        return self.node

    def getParentNode(self):
        """Returns a pointer to the parent node"""
        return self.parentNode

    def getName(self):
        """Returns the name of the node"""
        return self.node.getName()

    def cleanUp(self):
        self.sceneManager.destroySceneNode(self.node)
        del self.node
        self.parentNode = None
        self.sceneManager = None

