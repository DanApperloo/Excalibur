import ogre.renderer.OGRE as ogre
from GraphicsEngine.Models.GraphicsObjects.Drawables.Drawable import Drawable

class SpriteDrawable(Drawable):
    """Holds and controls the Graphics for Sprites"""

    def __init__(self, sceneManager, parentNode):
        """Base Constructor of Drawable"""
        Drawable.__init__(self, sceneManager, parentNode)
        self.sprite = None
        self.spriteSet = None

    def initialize(self, name, textureName):
        """Create the sprite and attach it to a scene node

        Keyword Arguments:
        name -- The unique name of the sprite
        textureName -- The location/name of the resource to use for the node

        """
        self.spriteSet = self.sceneManager.createBillboardSet(name + " Sprite")
        self.spriteSet.setDefaultDimensions(2.5, 2.5)
        self.spriteSet.setMaterialName(textureName)
        self.spriteSet.setBillboardOrigin(ogre.BillboardOrigin.BBO_BOTTOM_CENTER)
        self.spriteSet.setBillboardRotationType(ogre.BillboardRotationType.BBR_VERTEX)
        # self.spriteSet.setBillboardType(ogre.BillboardType.BBT_POINT)
        self.spriteSet.setBillboardType(ogre.BillboardType.BBT_ORIENTED_COMMON)
        self.spriteSet.setCommonDirection(ogre.Vector3(0, 1, 0))
        self.spriteSet.setCastShadows(False)
        self.sprite = self.spriteSet.createBillboard(0, 0, 0)
        self.createNode(name)
        self.attachObject(self.spriteSet)
        self.setVisible(False)

    def setPosition(self, position):
        """Implements Base class method"""
        Drawable.setPosition(self, position)

    def isVisible(self):
        """Returns if the sprite is visible or not"""
        return self.spriteSet.isVisible()

    def setVisible(self, visible):
        """Sets if the sprite is visible"""
        self.spriteSet.setVisible(visible)

    def setMaterial(self, materialName):
        self.spriteSet.setMaterialName(materialName)

    def getRotation(self):
        """Returns the rotation of the sprite's surface"""
        return self.spriteSet.getBillboard(0).getRotation()

    def cleanUp(self):
        self.sceneManager.destroyBillboardSet(self.spriteSet)
        Drawable.cleanUp(self)