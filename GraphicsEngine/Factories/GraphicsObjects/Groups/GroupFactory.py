from GraphicsEngine.Factories.GraphicsObjects.AbstractGraphicsObjectFactory import AbstractGraphicsObjectFactory
from GraphicsEngine.Models.GraphicsObjects.Groups.MapBlockGroup import MapBlockGroup
from GraphicsEngine.Models.GraphicsObjects.Groups.ProjectorGroup import ProjectorGroup
from GraphicsEngine.Models.GraphicsObjects.Groups.SpriteDrawableGroup import SpriteDrawableGroup

class GroupFactory(AbstractGraphicsObjectFactory):

    @classmethod
    def createCombatMapBlockGroup(cls, inputLayout, mapDimensions, parentName):
        return MapBlockGroup(
            cls.sceneManager,
            cls.rootNode,
            inputLayout,
            mapDimensions,
            "{0} - MapBlockGroup".format(parentName)
        )

    @classmethod
    def createCombatBlockHighlightingGroup(cls, mapDimensions, parentName):
        return ProjectorGroup(
            cls.sceneManager,
            cls.rootNode,
            mapDimensions,
            "{0} - ProjectorGroup".format(parentName)
        )

    @classmethod
    def createCombatSpriteDrawableGroup(cls, mapDimensions):
        return SpriteDrawableGroup(
            cls.sceneManager,
            cls.rootNode,
            mapDimensions
        )
