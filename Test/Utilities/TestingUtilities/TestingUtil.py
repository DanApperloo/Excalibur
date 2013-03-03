import unittest, os, errno

class AbstractTestClass(unittest.TestCase):
    """Base Test class to make testing easier"""

    @classmethod
    def setUpClass(cls):
        pass
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
        
#################################################################
class TestControl:
    """Start up the tests - call start()"""

    @classmethod
    def start(cls, clsin):
        suite = unittest.TestLoader().loadTestsFromTestCase(clsin)
        unittest.TextTestRunner(verbosity=2).run(suite)
            
    @classmethod
    def clean(cls):
        try:
            os.remove('ogre.cfg')
        except OSError, e:
            if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
                raise # re-raise exception if a different error occured
