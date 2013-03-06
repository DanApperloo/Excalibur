from Test.Utilities.TestingUtilities.TestingUtil import *
import ogre.renderer.OGRE as ogre
from GraphicsEngine.Models.GraphicsObjects.Drawables.SpriteDrawable import *

class SpriteDrawableTest(AbstractTestClass):
    """Tests the EntityDrawable Class"""

    def __del__( self ):
        ## Fix to stop crashes at exit -- C++ tries to delete vertexData which is ugly if it's a python object
         #self.sm.vertexData=None
        return

    def setUp(self):
        self.root = ogre.Root()
        cf = ogre.ConfigFile()
        cf.load("resources.cfg")
        seci = cf.getSectionIterator()
        while seci.hasMoreElements():
            secName = seci.peekNextKey()
            settings = seci.getNext()
 
            for item in settings:
                typeName = item.key
                archName = item.value
                ogre.ResourceGroupManager.getSingleton().addResourceLocation(archName, typeName, secName)
        
        #If the user has run before, use last Render Configuration, else use default OGRE dialog box to setup
        if not self.root.showConfigDialog():
            #If user exits config, throw error and shutdown
            raise Exception("User canceled the config dialog -> Application.setupRenderSystem()")
        self.root.initialise(True, "Tutorial Render Window")
        ogre.TextureManager.getSingleton().setDefaultNumMipmaps(5)
        ogre.ResourceGroupManager.getSingleton().initialiseAllResourceGroups()
        self.sceneManager = self.root.createSceneManager(ogre.ST_GENERIC, "Default SceneManager")
        self.parentNode = self.sceneManager.getRootSceneNode()
        self.sprite = SpriteDrawable(self.sceneManager, self.parentNode, "TestUnique", "FighterRear")

    def test_initialize(self):
        """Test the initialize() function"""
        testName = self.sprite.getName()
        self.assertTrue(testName == "TestUnique", "Created Drawable does not have root scene node as parent")
        testObject = self.sprite.getNode().getAttachedObject(0)
        self.assertTrue(testObject.getName() == "TestUnique Sprite", "Attached object name is not the expected name")
        
    def test_isVisible(self):
        """Tests if entity is visible or not"""
        testVisible = self.sprite.isVisible()
        self.assertTrue(testVisible == True, "IsVisible returns incorrect Value")

    def test_setVisible(self):
        """Tests if we can change the state of visible or not"""
        self.sprite.setVisible(False)
        testVisible = self.sprite.isVisible()
        self.assertTrue(testVisible == False, "setVisible did not change state correctly")
        
    def tearDown(self):
        self.sprite.cleanUp()
        del self.sprite
        del self.sceneManager
        del self.root

############################################################

if __name__ == "__main__":
    try:
        TestControl.start(SpriteDrawableTest)
    except ogre.OgreException, e:
        print e
    finally:
        TestControl.clean()
