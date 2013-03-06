from GraphicsEngine.Factories.GraphicsObjects.AbstractGraphicsObjectFactory import AbstractGraphicsObjectFactory
from GraphicsEngine.Models.GraphicsObjects.Entities.MapBlock import MapBlock

class MapBlockFactory(AbstractGraphicsObjectFactory):

    meshFilesByIndex = {1:"cube1.mesh", 2:"cube2.mesh", 3:"cube3.mesh", 4:"cube4.mesh", 5:"cube5.mesh"}

    @classmethod
    def createCombatMapBlock(cls, mapBlockGroup, meshIndex, staticPosition, xpos, ypos, zpos, parentName):
        return MapBlock(
            cls.sceneManager,
            cls.rootNode,
            mapBlockGroup,
            cls.meshFilesByIndex[meshIndex],
            staticPosition,
            xpos,
            ypos,
            zpos,
            "{0} - MapBlock X:{1} Y:{2}".format(parentName, staticPosition[0], staticPosition[1])
        )