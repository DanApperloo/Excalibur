class TransitionType(object):

    def __init__(self, source, destination, keyMappingList):
        self.source = source
        self.destination = destination
        self.keyMappings = keyMappingList

    def getKeyMapping(self):
        return self.keyMappings

    def getSource(self):
        return self.source

    def getDestination(self):
        return self.destination