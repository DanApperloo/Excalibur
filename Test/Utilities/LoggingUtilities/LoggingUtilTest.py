from Utilities.LoggingUtilities.LoggingUtil import *
from Test.Utilities.TestingUtilities.TestingUtil import *

class TestLogging(AbstractTestClass):
    """Test the Logging Utility Methods"""

    logger = LoggingUtil("TestLogging")

    #Sets up the conditions for every test, will happen before each test
    def setUp(self):
        self.logFile = open('GameLog.txt', 'r')

    #Tests the logInfo Function to make sure it appends a message with INFO in it
    def test_logInfo(self):
        self.logger.logInfo('info message')
        contents = self.logFile.read()
        self.assertTrue("INFO" in contents)

    #Tests the logDebug Function to make sure it appends a message with DEBUG in it
    def test_logDebug(self):
        self.logger.logDebug('debug message')
        contents = self.logFile.read()
        self.assertTrue("DEBUG" in contents)

    #Tests the logWarn Function to make sure it appends a message with WARNING in it
    def test_logWarn(self):
        self.logger.logWarn('warn message')
        contents = self.logFile.read()
        self.assertTrue("WARNING" in contents)

    #Tests the logError Function to make sure it appends a message with ERROR in it
    def test_logError(self):
        self.logger.logError('error message')
        contents = self.logFile.read()
        self.assertTrue("ERROR" in contents)

    #Test the logException when the logging has been initialized
    def test_logExceptionWithLoggingOn(self):
        try:
            raise MyError("exception message 1")
        except Exception, e:
            LoggingUtil.logException(e.value)
        contents = self.logFile.read()
        self.assertTrue("exception message 1" in contents)

    #Tets the logException when logging has not been initialized
    def test_logExceptionWithLoggingOff(self):
        LoggingUtil.shutdown()
        try:
            raise MyError("exception message 2")
        except Exception, e:
            LoggingUtil.logException(e.value)
        contents = self.logFile.read()
        self.assertTrue("exception message 2" in contents)
        TestLogging.logger = LoggingUtil("TestLogging")
            
    #Happens after every test. Used to make sure things reset and are closed.
    def tearDown(self):
        self.logFile.close()

##############################################
#Error Class Used for Testing
class MyError(Exception):
    def __init__(self, valuein):
        self.value = valuein

    def __str__(self):
        return self.value
        
#############################################
if __name__ == '__main__':
    TestControl.start(TestLogging)
