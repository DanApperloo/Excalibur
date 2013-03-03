# Constants
STORAGE_CATEGORIES = ['GUIModes', 'SceneModes']

class BasicStorage(object):
    """Global dictionary wrapper that allows access through class methods"""

    # Class Storage
    storage = dict() # Dictionary that holds dictionaries
    for category in STORAGE_CATEGORIES:
        storage[category] = dict()

    @classmethod
    def getGUIMode(cls, key):
        return cls.storage['GUIModes'][key]

    @classmethod
    def putGUIMode(cls, key, it):
        cls.putWrapper(key, it, 'GUIModes')

    @classmethod
    def getSceneMode(cls, key):
        return cls.storage['SceneModes'][key]

    @classmethod
    def putSceneMode(cls, key, it):
        cls.putWrapper(key, it, 'SceneModes')

    @classmethod
    def putWrapper(cls, key, it, repo):
        if key in cls.storage[repo]:
            errorString = str(key) + ' entity already exists in ' + repo
            raise NameError(errorString)
        else:
            cls.storage[repo][key] = it