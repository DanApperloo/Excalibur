from GraphicsEngine.Views.SubViews.GUI.BasicGUISubView import BasicGUISubView
from InputManaging.InputManager import InputManager
from InputManaging.ControlEvents import ControlEvents
from Utilities.GraphicsUtilities.GraphicsUtility import GraphicsUtility
import ogre.gui.CEGUI as CEGUI

class TestTransitionSubView(BasicGUISubView):

    # Class Constants--------------------------------------------------------------------------------------------------#
    GUI_LAYOUT = 'TestLayout.layout'
    # -----------------------------------------------------------------------------------------------------------------#

    def __init__(self, mode, guiSheet, schemeFile):
        BasicGUISubView.__init__(self, mode, guiSheet, schemeFile, TestTransitionSubView.GUI_LAYOUT)

    def registerHandlers(self):
            self.ui.getChild("TestLayout/ActionSelection").getChild("TestLayout/ActionSelection/Transition-Clickable").subscribeEvent(
                CEGUI.PushButton.EventClicked, self, 'transition'
            )
    #        self.ui.getChild("Second Demo Window").getChild("Second Demo Window/Button2-Clickable").subscribeEvent(
    #            CEGUI.PushButton.EventClicked, self, 'printFunction'
    #        )

    def transition(self, e):
        InputManager.getSingleton().setControlEvent(ControlEvents.TRANSITION_FORWARD)
