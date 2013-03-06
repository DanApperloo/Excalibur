import ogre.renderer.OGRE as ogre
from GraphicsEngine.Models.GraphicsObjects.Drawables.Drawable import Drawable

class SpriteDrawable(Drawable):
    """Holds and controls the Graphics for Sprites"""

    def __init__(self, sceneManager, parentNode, spriteGroup, name, textureName):
        """Base Constructor of Drawable.
        Create the sprite and attach it to a scene node

        Keyword Arguments:
        sceneManager -- Reference to the OGRE sceneManager
        parentNode -- The parent node of the entity
        spriteGroup -- Reference to the parent SpriteDrawableGroup
        name -- The unique name of the sprite
        textureName -- The location/name of the resource to use for the node

        """
        Drawable.__init__(self, sceneManager, parentNode, name)
        self.spriteGroup = spriteGroup
        self.name = name
        self.textureName = textureName

    def initialize(self):
        self.spriteSet = self.sceneManager.createBillboardSet(self.name + " Sprite")
        self.spriteSet.setDefaultDimensions(2.5, 2.5)
        self.spriteSet.setMaterialName(self.textureName)
        self.spriteSet.setBillboardOrigin(ogre.BillboardOrigin.BBO_BOTTOM_CENTER)
        self.spriteSet.setBillboardRotationType(ogre.BillboardRotationType.BBR_VERTEX)
        # self.spriteSet.setBillboardType(ogre.BillboardType.BBT_POINT)
        self.spriteSet.setBillboardType(ogre.BillboardType.BBT_ORIENTED_COMMON)
        self.spriteSet.setCommonDirection(ogre.Vector3(0, 1, 0))
        self.spriteSet.setCastShadows(False)
        self.sprite = self.spriteSet.createBillboard(0, 0, 0)
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
        self.spriteGroup = None
        del self.spriteGroup
        del self.textureName
        del self.name
        self.sceneManager.destroyBillboardSet(self.spriteSet)
        Drawable.cleanUp(self)