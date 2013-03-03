from GraphicsEngine.Views.SubViews.GUI.BasicGUISubView import BasicGUISubView
from Utilities.GraphicsUtilities.GraphicsUtility import GraphicsUtility
import ogre.gui.CEGUI as CEGUI

class CharacterPlacementMenuSubView(BasicGUISubView):

    # Class Constants--------------------------------------------------------------------------------------------------#
    GUI_LAYOUT = 'CharacterPlacementMenu.layout'
    # -----------------------------------------------------------------------------------------------------------------#

    def __init__(self, mode, guiSheet, schemeFile):
        BasicGUISubView.__init__(self, mode, guiSheet, schemeFile, CharacterPlacementMenuSubView.GUI_LAYOUT)

    def registerHandlers(self):
    #        self.ui.getChild("Second Demo Window").getChild("Second Demo Window/Button1-Clickable").subscribeEvent(
    #            CEGUI.PushButton.EventClicked, GraphicsUtility, 'printFunction'
    #        )
    #        self.ui.getChild("Second Demo Window").getChild("Second Demo Window/Button2-Clickable").subscribeEvent(
    #            CEGUI.PushButton.EventClicked, self, 'printFunction'
    #        )
        pass

    def printFunction(self, e):
        print "I got Clicked as well!"

