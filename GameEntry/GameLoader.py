from GraphicsEngine.Engine.GraphicsEngineMain import *
from GameEngine.Engine.GameEngineMain import *
from InputManaging.InputManager import *
from InputManaging.ControlEvents import ControlEvents

# Controls the flow of the game as well as all of the main utilities---------------------------------------------------#
class GameLoader(object):
    """Controls the game loop and all of the control classes"""

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self):
        self.graphicsEngine = None
        self.gameEngine = None
        self.inputManager = None
        self.resourceLoader = None

    # Sets up the Graphics Engine--------------------------------------------------------------------------------------#
    def initialiseGraphicsEngine(self):
        """Sets up the Graphics Engine Singleton.

        The Graphics Engine controls the displaying of the game. Configures CEGUI and OGRE settings.
        """
        self.graphicsEngine = GraphicsEngineMain()

    # Sets up the Game Engine------------------------------------------------------------------------------------------#
    def initialiseGameEngine(self):
        """Sets up the Game Engine Singleton.

        The Game Engine controls all of the business logic of the game. Stores and controls all object metadata.
        """
        self.gameEngine = GameEngineMain()

    # Sets up the Input Manager----------------------------------------------------------------------------------------#
    def initialiseInputManager(self):
        """Sets up the Input Manager Singleton.

        The Input Manager controls the input to the game. Relays input into CEGUI and OGRE.
        Dependant of Graphics Engine.
        """
        if self.graphicsEngine is not None:
            try:
                self.inputManager = InputManager(self.graphicsEngine.root, self.graphicsEngine.window)
            except Exception, e:
                raise e
        else:
            raise Exception("Input Manager could not be initialised due to error in Graphics Engine.")

    # Runs the game loop-----------------------------------------------------------------------------------------------#
    def gameLoop(self):
        """Controls the repetitive game loop."""
        self.graphicsEngine.loadGameMode(Constant.ENTRY_EXIT_MODE)
        while self.graphicsEngine.render():
            self.inputManager.frameListener.capture()
            self.resolveControlEvent()
        # Clean up any left over resources
        self.graphicsEngine.gameModeList[Constant.INDEX_MODE_LIST[self.graphicsEngine.currentMode]].cleanUp()  # Cleans up active Game Modes

    def resolveControlEvent(self):
        if self.inputManager.getControlEvent() == ControlEvents.TRANSITION_FORWARD:
            TransitionManager.getSingleton().sendTransition(self.graphicsEngine.gameModeList[Constant.INDEX_MODE_LIST[self.graphicsEngine.currentMode]].getTransition())
            transition = TransitionManager.getSingleton().readTransition()
            self.graphicsEngine.gameModeList[Constant.INDEX_MODE_LIST[self.graphicsEngine.currentMode]].cleanUp()
            if transition.destination == 'IntroMode':
                self.graphicsEngine.currentMode = 0
            elif transition.destination == 'PlacementMode':
                self.graphicsEngine.currentMode = 1
            elif transition.destination == 'CombatMode':
                self.graphicsEngine.currentMode = 2
            self.graphicsEngine.loadGameMode(self.graphicsEngine.currentMode)
            self.inputManager.flushControlEvent()

    # Cleans up all resources being used-------------------------------------------------------------------------------#
    def cleanUp(self):
        if self.graphicsEngine is not None: self.graphicsEngine.cleanUp()
        if self.gameEngine is not None: self.gameEngine.cleanUp()
        if self.inputManager is not None: self.inputManager.cleanUp()
