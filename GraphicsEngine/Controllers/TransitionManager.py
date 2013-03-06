from GraphicsEngine.Models.Flow.Transition import Transition

class TransitionManager(object):

    __singleton = None

    def __init__(self):
        self.registeredTransitionTypes = {}
        self.transitionPath = []
        TransitionManager.__singleton = self

    def registerTransitionType(self, transitionType):
        self.registeredTransitionTypes[(transitionType.source, transitionType.destination)] = transitionType

    def createTransitionFromTypeAndSource(self, transitionTypeKey, sourceObject):
        transitionType = self.registeredTransitionTypes[transitionTypeKey]
        dataTransferMapping = []
        for mapping in transitionType.getKeyMapping():
            dataTransferMapping.append((getattr(sourceObject, sourceObject.outputMapping[mapping[0]]), mapping[1]))
        transition = Transition(transitionType.source, transitionType.destination, dataTransferMapping)
        return transition

    def readAndSetDataFromTransition(self, transition, destinationObject):
        pass

    def readTransition(self):
        return self.transitionPath[len(self.transitionPath) - 1]

    def sendTransition(self, transition):
        self.transitionPath.append(transition)

    @classmethod
    def getSingleton(cls):
        return cls.__singleton