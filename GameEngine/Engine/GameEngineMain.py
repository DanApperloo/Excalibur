
# GameEngineMain handles interaction with game data objects------------------------------------------------------------#
class GameEngineMain(object):

    # Class Variables--------------------------------------------------------------------------------------------------#
    __singleton = None
    # -----------------------------------------------------------------------------------------------------------------#

    # Default Constructor----------------------------------------------------------------------------------------------#
    def __init__(self):
        self.__setUp()
        GameEngineMain.__singleton = self

    # Initialises the GameEngine in the correct order------------------------------------------------------------------#
    def __setUp(self):
        pass

    # Gets the instance of the GameEngine------------------------------------------------------------------------------#
    @classmethod
    def getSingleton(cls):
        if cls.__singleton is not None:
            return cls.__singleton
        else:
            raise Exception("GameEngine is not initialised.\
             Please initialise GameEngine before retrieving an instance.")

    # Cleans up resources----------------------------------------------------------------------------------------------#
    def cleanUp(self):
        pass


