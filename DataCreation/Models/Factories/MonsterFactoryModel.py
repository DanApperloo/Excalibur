__author__ = 'Dan'
from Utilities.LoggingUtilities.LoggingUtil import *
from GameEngine.Combatants.Monster import *
from DataCreation.Models.Factories.BaseFactoryModel import *
from xml.dom.minidom import parse

class MonsterFactory(Factory):
    
    logger = LoggingUtil("MonsterFactory")
    
    def __init__(self):
        self.filename = "/Game/Resources/datafiles/character data/Monster.xsd"
        Factory.__init__(self,self.filename )
        

    def Createmonster(self,xmlIn):
        xml = xmlIn
        response = self.Schemavalidate(xml)
        if response[0]:
            dom1 = parse(xml).documentElement
            return Monster( dom1.getAttribute("name")).creation( dom1.getElementsByTagName("lvl"),  dom1.getElementsByTagName("job"), dom1.getElementsByTagName("type"))
        else :
            print "monster creation failed"
            
    def Createmonster2(self,xmlIn):
        xml = xmlIn
        response = self.Schemavalidate(xml)
        output = "ERROR"
        if response[0]:
            output = Monster(response[1].getroot().get("name"), response[1].findtext("lvl"),  response[1].findtext("job"), response[1].findtext("type"), response[1].findtext("str"),response[1].findtext("mag"),response[1].findtext("acc"),response[1].findtext("evn"),response[1].findtext("def"),response[1].findtext("maxhp"), response[1].findtext("exp"))
        else :
            print "Monster creation failed."
        return output