from Test.Utilities.TestingUtilities.TestingUtil import *
import ogre.renderer.OGRE as ogre
from GraphicsEngine.Models.GraphicsObjects.Drawables.Drawable import *

class DrawableTest(AbstractTestClass):
    """Tests the Drawable Class"""

    def __del__( self ):
        ## Fix to stop crashes at exit -- C++ tries to delete vertexData which is ugly if it's a python object
        #self.sm.vertexData=None
        return
    
    def setUp(self):
        self.root = ogre.Root()
        self.sceneManager = self.root.createSceneManager(ogre.ST_GENERIC, "Default SceneManager")
        self.parentNode = self.sceneManager.getRootSceneNode()
        self.drawable = Drawable(self.sceneManager, self.parentNode, "TestDrawable")

    def test_Constructor(self):
        """Test the default constructor function"""
        testParentNode = self.drawable.getParentNode()
        self.assertEqual(testParentNode, self.parentNode, "Created Drawable does not have root scene node as parent")

    def test_createNode(self):
        """Tests the proper creation of a child node"""
        testName = self.drawable.getName()
        self.assertTrue(testName == "TestDrawable", "Node was not created correctly")

    def test_attachObject(self):
        """Tests the proper attaching of objects to nodes"""
        originalObject = ogre.MovableObject()
        self.drawable.attachObject(originalObject)
        testObject = self.drawable.getNode().getAttachedObject(0)
        self.assertEqual(testObject, originalObject, "Attached object is not the same object as the created object")
        
    def test_setPosition(self):
        """Tests the set position function"""
        testPosition = (1, 1, 1)
        self.drawable.setPosition(testPosition)
        actualPosition = self.drawable.getPosition()
        self.assertTrue(testPosition == actualPosition, "Position is not being set correctly")

    def tearDown(self):
        self.drawable.cleanUp()
        del self.drawable
        del self.sceneManager
        del self.root

############################################################

if __name__ == "__main__":
    TestControl.start(DrawableTest)
    TestControl.clean()
    
