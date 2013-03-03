from GraphicsEngine.Views.SubViews.GUI.BasicGUISubView import BasicGUISubView
from Utilities.GraphicsUtilities.GraphicsUtility import GraphicsUtility
import ogre.gui.CEGUI as CEGUI

class CombatMapMenuSubView(BasicGUISubView):

    # Class Constants--------------------------------------------------------------------------------------------------#
    GUI_LAYOUT = 'BattleMenu.layout'
    # -----------------------------------------------------------------------------------------------------------------#

    def __init__(self, mode, guiSheet, schemeFile):
        BasicGUISubView.__init__(self, mode, guiSheet, schemeFile, CombatMapMenuSubView.GUI_LAYOUT)

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
