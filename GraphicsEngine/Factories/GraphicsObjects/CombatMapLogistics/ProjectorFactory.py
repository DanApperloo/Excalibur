from GraphicsEngine.Factories.GraphicsObjects.AbstractGraphicsObjectFactory import AbstractGraphicsObjectFactory
from GraphicsEngine.Models.GraphicsObjects.CombatMapLogistics.SquareProjector import SquareProjector
from GraphicsEngine.Models.GraphicsObjects.CombatMapLogistics.SelectionProjector import SelectionProjector

class ProjectorFactory(AbstractGraphicsObjectFactory):

    @classmethod
    def createBlockHighlighter(cls, projectorGroup, rowIndex, columnIndex, parentName):
        return SquareProjector(
            cls.sceneManager,
            cls.rootNode,
            projectorGroup,
            rowIndex,
            columnIndex,
            "{0} - SquareProjector X:{1} Y:{2}".format(parentName, rowIndex, columnIndex)
        )

    @classmethod
    def createPointerAtPosition(cls, xpos, ypos, parentName):
        return SelectionProjector(
            cls.sceneManager,
            cls.rootNode,
            xpos,
            ypos,
            "{0} - SelectionProjector X:{1} Y:{2}".format(parentName, xpos, ypos)
        )
