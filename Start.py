import sys, os
sys.path.insert(0,'.')
from GameEntry.GameLoader import GameLoader

if __name__ == '__main__':
    try:
        application = GameLoader()
        application.initialiseGameEngine()
        application.initialiseGraphicsEngine()
        application.initialiseInputManager()
        application.gameLoop()
        application.cleanUp()
    finally:
        os.remove('ogre.cfg')


