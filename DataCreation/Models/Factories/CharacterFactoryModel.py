from Utilities.LoggingUtilities.LoggingUtil import *
from GameEngine.Combatants.Character import *
from DataCreation.Models.Factories.BaseFactoryModel import *

class CharacterFactory(Factory):
    
    logger = LoggingUtil("CharacterFactory")
    
    def __init__(self,filenamein):
        self.filename = filenamein
        Factory.__init__(self,self.filename)

    def CreateCharacter(self,xmlIn):
        xml = xmlIn
        response = self.Schemavalidate(xml)
        output = "ERROR"
        if response[0]:
            output = Character(response[1].getroot().get("name"), response[1].findtext("lvl"),  response[1].findtext("job"), response[1].findtext("type"), response[1].findtext("str"),response[1].findtext("mag"),response[1].findtext("acc"),response[1].findtext("evn"),response[1].findtext("def"),response[1].findtext("maxhp"),response[1].findtext("exp"))
        else :
            print "Character creation failed."
        return output    
        
    def SaveCharacter(self,xmlIn):
        pass