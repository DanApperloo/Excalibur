from GraphicsEngine.Factories.GraphicsObjects.AbstractGraphicsObjectFactory import AbstractGraphicsObjectFactory
from GraphicsEngine.Models.GraphicsObjects.Drawables.SpriteDrawable import SpriteDrawable

class SpriteDrawableFactory(AbstractGraphicsObjectFactory):

    @classmethod
    def createCombatMapSprite(cls, spriteGroup, name, textureName):
        return SpriteDrawable(
            cls.sceneManager,
            cls.rootNode,
            spriteGroup,
            name,
            textureName
        )

    @classmethod
    def createPointerSprite(cls, nodeToAttachTo, name, textureName):
        return SpriteDrawable(
            cls.sceneManager,
            nodeToAttachTo,
            None,
            name,
            textureName
        )