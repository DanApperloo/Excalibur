#Import Basic Python Logging Libraries
import logging
import Storage.Constants as Constant
import os
import datetime
import inspect

class LoggingUtil(object):
    """A Utility to allow easy logging - Initialize with string of Class name"""

    #Class Variables ------------------------------
    logFileName = "GameLog.txt"
    loggerMap = {}
    active = False
    console = None
    fileLog = None
    exceptionLogger = None
    loggingEnabled = True
    #----------------------------------------------

    #
    # Constructor
    # @param className the Name of the class that is initializing its logger
    #
    def __init__(self, classNameIn):
        if not LoggingUtil.active:
            LoggingUtil.active = True
            LoggingUtil.setupLoggingOutputs()
        if classNameIn in LoggingUtil.loggerMap:
            self.logger = LoggingUtil.loggerMap[classNameIn]
        else:
            self.logger = Logger(classNameIn, LoggingUtil.console, LoggingUtil.fileLog)
        self.logger.setLevel(Constant.LOGGING_LEVEL)

    #
    # Method to set up logging handlers
    #
    @classmethod
    def setupLoggingOutputs(cls):
        cls.console = logging.StreamHandler()
        cls.fileLog = logging.FileHandler(cls.logFileName,'w')
    
    #
    # Will log a message in the format <TimeLogged> <ClassName> ERROR <Message>
    # @param message the message to display
    #
    def logError(self, message):
        if self.logger and self.loggingEnabled:
            self.logger.error(message)

    #
    # Will log a message in the format <TimeLogged> <ClassName> WARNING <Message>
    # @param message the message to display
    #
    def logWarn(self, message):
        if self.logger and self.loggingEnabled:
            self.logger.warning(message)

    #
    # Will log a message in the format <TimeLogged> <ClassName> DEBUG <Message>
    # @param message the message to display
    #
    def logDebug(self, message):
        if self.logger and self.loggingEnabled:
            self.logger.debug(message)

    #
    # Will log a message in the format <TimeLogged> <ClassName> INFO <Message>
    # @param message the message to display
    #
    def logInfo(self, message):
        if self.logger and self.loggingEnabled:
            self.logger.info(message)

    #
    # Method to log catched exceptions to LogFile and Console
    # @param exception message to log
    #
    @classmethod
    def logException(cls, message):
        if cls.loggingEnabled:
            if not cls.active:
                cls.setupLoggingOutputs()
            cls.exceptionLogger = Logger(cls.__name__, LoggingUtil.console, LoggingUtil.fileLog)
            cls.exceptionLogger.error(message)
            cls.exceptionLogger = None
            if not cls.active:
                cls.console.flush()
                cls.console = None
                cls.fileLog.close()
                cls.fileLog = None

    #
    # Enables Logging Output
    #
    @classmethod
    def enableLogging(cls):
        cls.loggingEnabled = True

    #
    # Disables Logging Output
    #
    @classmethod
    def disableLogging(cls):
        cls.loggingEnabled = False
        
    #
    # Release the resources used by the logger. MUST BE CALLED BEFORE PROGRAM ENDS
    #
    @classmethod
    def shutdown(cls):
        if cls.active:
            cls.active = False
            cls.console.flush()
            cls.console = None
            cls.fileLog.close()
            cls.fileLog = None
            for it in cls.loggerMap:
                cls.loggerMap[it].shutdown()
            cls.loggerMap = {}
        

####################################################################################
class Logger(object):
    """Logs Information to Console and File - Uses Root as calling identifier"""

    dateFormat = "%m-%d %H:%M"
    messageFormat = '%(asctime)s %(name)-12s: %(levelname)-8s %(message)s'
    
    def __init__(self, classNameIn, consoleIn, fileLogIn):
        if classNameIn == "":
            self.loggerName = "Root"
        else:
            self.loggerName = classNameIn
        self.console = consoleIn
        self.fileLog = fileLogIn
        self.loggingLevel = 21

    def setLevel(self, lvl):
        self.loggingLevel = lvl

    def getTimeStamp(self):
        return datetime.datetime.today().strftime("%m-%d %H:%M")

    def error(self, message):
        messageLevel = "ERROR"
        levelNumber = 40
        self.logMessage(levelNumber, messageLevel, message)

    def warning(self, message):
        messageLevel = "WARNING"
        levelNumber = 30
        self.logMessage(levelNumber, messageLevel, message)

    def info(self, message):
        messageLevel = "INFO"
        levelNumber = 25
        self.logMessage(levelNumber, messageLevel, message)

    def debug(self, message):
        messageLevel = "DEBUG"
        levelNumber = 20
        self.logMessage(levelNumber, messageLevel, message)

    def logMessage(self, levelNumber, level, message):
        if levelNumber >= self.loggingLevel:
            record = logging.LogRecord(self.loggerName, levelNumber, os.path.abspath(__file__), inspect.currentframe().f_back.f_lineno, Logger.messageFormat, {"asctime":self.getTimeStamp(),"name":self.loggerName, "levelname":level, "message":message}, None)
            self.console.handle(record)
            self.fileLog.handle(record)

    def shutdown(self):
        self.fileLog = None
        self.console = None
        
        
        
    
        

            
