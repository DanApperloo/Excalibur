import ogre.renderer.OGRE as ogre
import ogre.gui.CEGUI as CEGUI
import os
from GraphicsEngine.Views.SubViews.GUI.BasicGUISubView import *
from GraphicsEngine.Views.SubViews.GUI.CharacterPlacementMenuSubView import *
from GraphicsEngine.Views.SubViews.GUI.CombatMapMenuSubView import *
from GraphicsEngine.Views.SubViews.Scene.BackgroundSubView import *
from GraphicsEngine.Views.SubViews.Scene.CombatMapSubView import *
from GraphicsEngine.Views.SubViews.Scene.CharacterPlacementSubView import *
from GraphicsEngine.Views.View import View
from Storage.BasicStorage import BasicStorage
import Storage.Constants as Constant

# Another fix for CEGUI to ensure we get a working parser...-----------------------------------------------------------#
if os.name == 'nt':
    CEGUI.System.setDefaultXMLParserName("ExpatParser")
else:
    CEGUI.System.setDefaultXMLParserName("TinyXMLParser")

# GraphicsEngineMain Class---------------------------------------------------------------------------------------------#
class GraphicsEngineMain(object):
    """GraphicsEngineMain Class. Sets up game window and loads initial stage. Holds all screen output systems."""

    # Class Variables--------------------------------------------------------------------------------------------------#
    __singleton = None
    # -----------------------------------------------------------------------------------------------------------------#

    # Constructor------------------------------------------------------------------------------------------------------#
    def __init__(self, pluginsPathIn = './Config/plugins.cfg', resourcePathIn = './Config/resources.cfg'):
        """
        GraphicsEngineMain Constructor. Initializes Ogre Root and Ogre ResourceGroupManager.
        Sets other Variables to NONE or Empty Lists.

        Parameters:
        pluginsPathIn -- A path to the plugins.cfg file.
        resourcePathIn -- A path to the resources.cfg file.
        """
        self.root = ogre.Root(pluginsPathIn)
        self.pluginsPath = pluginsPathIn
        self.resourcePath = resourcePathIn
        self.resourceGroupManager = ogre.ResourceGroupManager.getSingleton()
        self.gameModeList = {}
        self.__setUp()
        GraphicsEngineMain.__singleton = self

    # Sets up the graphics engine--------------------------------------------------------------------------------------#
    def __setUp(self):
        # Order IS important.
        self._loadResources(self.resourcePath)                          # Load resources
        self._chooseRenderEngine()                                      # Choose Render Engine
        self._baseSetup()                                               # Setup OGRE Root
        self._windowSetup()                                             # Setup Game Window
        self._initialiseResources()                                     # Initialise Resources
        self._setupCEGUI()                                              # Setup CEGUI system
        self._createCamera('Main Camera', Constant.INITIAL_CAMERA_POSITION, (0, 0, 0))     # Create main Camera and connect to viewpoint

    # Loads all resources into game------------------------------------------------------------------------------------#
    def _loadResources(self, resourcePath):
        config = ogre.ConfigFile()                                      # Load OGRE Config file
        config.load(resourcePath)                                       # Load Resources
        sectionIterator = config.getSectionIterator()                   # Iterate through resource file
        while sectionIterator.hasMoreElements():
            sectionName = sectionIterator.peekNextKey()
            settings = sectionIterator.getNext()
            for item in settings:
                # Store the resources in the appropriate locations
                self.resourceGroupManager.addResourceLocation(item.value, item.key, sectionName)

    # Restores or creates a new Render Engine--------------------------------------------------------------------------#
    def _chooseRenderEngine(self):
        # If the user has run before, use last Render Configuration, else use default OGRE dialog box to setup
        if not self.root.restoreConfig() and not self.root.showConfigDialog():
            # If user exits config, throw error and shutdown
            raise Exception("User canceled the config dialog -> Application.setupRenderSystem()")

    # Initialises OGRE Root and loads Plugins--------------------------------------------------------------------------#
    def _baseSetup(self):
        self.root.initialise(False)                                      # Initialise OGRE Root
        self.root.initialisePlugins()                                    # Load all Plugins

    # Creates the game window and sets SceneManager and RootSceneNode--------------------------------------------------#
    def _windowSetup(self):
        # Create the SceneManager which holds all information about 3D images to display
        self.sceneManager = self.root.createSceneManager("TerrainSceneManager")
        # Create the window to run the game in using pre-defined constants
        self.window = self.root.createRenderWindow(Constant.GAME_WINDOW_TITLE, Constant.GAME_WINDOW_HEIGHT, Constant.GAME_WINDOW_WIDTH, False)
        # Set Ambient Light to full, since we will not be using any built in shadows
        self.sceneManager.setAmbientLight(ogre.ColourValue(1, 1, 1))
        # Create the Root Scene Node at (0,0,0) as a starting place for all other objects
        self.rootSceneNode = self.sceneManager.getRootSceneNode()

    # Initialises all game resources-----------------------------------------------------------------------------------#
    def _initialiseResources(self):
        ogre.TextureManager.getSingleton().setDefaultNumMipmaps(5)
        self.resourceGroupManager.initialiseAllResourceGroups()           # Initialise Resources

    # Initialises the required CEGUI components------------------------------------------------------------------------#
    def _setupCEGUI(self):
        # Create the OGRE-CEGUI Renderer to allow GUI to be displayed on game window
        self.renderer = CEGUI.OgreCEGUIRenderer(self.window, ogre.RENDER_QUEUE_OVERLAY, False, 3000, self.sceneManager)
        # Store create and store CEGUI system, holds all CEGUI data
        self.system = CEGUI.System(self.renderer)
        CEGUI.Logger.getSingleton().loggingLevel = CEGUI.Insane            # Set Logging to maximum
        self.__loadAllGUISchemes()                                         # Load all game GUI Schemes, Used for modes
        # Set Mouse appearance
        CEGUI.System.getSingleton().setDefaultMouseCursor("TaharezLook", "MouseArrow")
        # Create a canvas to build the GUI on
        self.GUISheet = CEGUI.WindowManager.getSingleton().createWindow('DefaultWindow', 'root')
        CEGUI.System.getSingleton().setGUISheet(self.GUISheet)             # Load canvas into CEGUI System
        # Create the required Game Modes
        self.__createGameModes()
        self.imagesetManager = CEGUI.ImagesetManager.getSingleton()
        self.imagesetManager.createImagesetFromImageFile('Background/BackgroundImage', "BackgroundPicture2.tga")

    # Creates the default Camera---------------------------------------------------------------------------------------#
    def _createCamera(self, cameraName, position, lookAt, clipDistance = 5):
        self.camera = self.sceneManager.createCamera(cameraName)           # Create a camera
        self.camera.setPosition(position[0], position[1], position[2])     # Set it's position
        self.camera.lookAt(lookAt[0], lookAt[1], lookAt[2])                # Point it at location
        self.camera.setNearClipDistance(clipDistance)                      # Set the near clipping distance
        self.viewport = self.window.addViewport(self.camera)               # Add it to the viewport to enable
        self.viewport.setBackgroundColour(ogre.ColourValue(0, 0, 0))       # Set the background colour of screen to black

    # Loads the entry Mode---------------------------------------------------------------------------------------------#
    def loadGameMode(self, modeIndex):
        self.currentMode = modeIndex
        self.gameModeList[Constant.INDEX_MODE_LIST[self.currentMode]].initialize()  # Initialise the Game Mode

    # Private Helper Function --- Loads the GUI schemes----------------------------------------------------------------#
    def __loadAllGUISchemes(self):
        self.schemeList = ["TestMode.scheme"]                              # Loads the specified schemes
        for scheme in self.schemeList:
            CEGUI.SchemeManager.getSingleton().loadScheme(scheme)

    # Creates the game modes required----------------------------------------------------------------------------------#
    def __createGameModes(self):
        # Constructs and stores all of the possible Game Modes
        messageGUI = BasicGUISubView('MessageBox', self.GUISheet, 'TestMode', 'TestLayout.layout')
        combatGUI = CombatMapMenuSubView('CombatMenu', self.GUISheet, 'TestMode')
        characterPlacementGUI = CharacterPlacementMenuSubView('PlacementMenu', self.GUISheet, 'TestMode')
        BasicStorage.putGUIMode('MessageBox', messageGUI)
        BasicStorage.putGUIMode('CombatMenu', combatGUI)
        BasicStorage.putGUIMode('PlacementMenu', characterPlacementGUI)

        backgroundScene = BackgroundSubView('Background', self.GUISheet)
        combatScene = CombatMapSubView('Combat', self.sceneManager, Constant.MAP, ("cube1.mesh", "cube2.mesh", "cube3.mesh", "cube4.mesh", "cube5.mesh"))
        characterPlacementScene = CharacterPlacementSubView('Placement', self.sceneManager, Constant.PLACEMENT, "cube1.mesh")
        BasicStorage.putSceneMode('Background', backgroundScene)
        BasicStorage.putSceneMode('Combat', combatScene)
        BasicStorage.putSceneMode('Placement', characterPlacementScene)

        self.gameModeList['IntroMode'] = View("IntroMode", 'Background', 'MessageBox', '')
        self.gameModeList['CombatMode'] = View("CombatMode", 'Combat', 'CombatMenu', '')
        self.gameModeList['PlacementMode'] = View("PlacementMode", 'Placement', 'PlacementMenu', '')

    # Renders the screen-----------------------------------------------------------------------------------------------#
    def render(self):
        exit = self.root.renderOneFrame()
        return exit

    # Gets the instance of the GraphicsEngine--------------------------------------------------------------------------#
    @classmethod
    def getSingleton(cls):
        if cls.__singleton is not None:
            return cls.__singleton
        else:
            raise Exception("GraphicsEngine is not initialised.\
             Please initialise GraphicsEngine before retrieving an instance.")

    # Cleans up all used resources so OGRE can shutdown correctly------------------------------------------------------#
    def cleanUp(self):
        GraphicsEngineMain.__singleton = None
        if self.camera is not None: del self.camera                         # Delete Camera
        if self.sceneManager is not None: del self.sceneManager             # Delete Scene Manager
        if self.system is not None: del self.system                         # Delete CEGUI System
        if self.renderer is not None: del self.renderer                     # Delete OGRE-CEGUI Renderer
        if self.root is not None: del self.root                             # Delete OGRE Root
        if self.viewport is not None: del self.viewport                     # Delete OGRE Viewport