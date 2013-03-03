from Utilities.LoggingUtilities.LoggingUtil import *
from GameEngine.Combatants.Combatant import *

class Character(Combatant):

    logger = LoggingUtil("Character")

    def __init__(self, nameIn, lvlIn, jobIn, typeIn, nonMagIn, magIn, hitIn, evasIn, defIn, hitPointsIn, expin):
        Combatant.__init__(self, nameIn, lvlIn, jobIn, nonMagIn, magIn, hitIn, evasIn, defIn, hitPointsIn, expin)
        self.type = typeIn
        self.charCreation()
    #def updatequipment(self,invname,dict2): # function to be called when adding new items to invnetory

    def charCreation(self):

        if self.job == "Fighter":
            self.currenthp = self.hitpoints
            self.abilitlist = ""
            self.inv[ 'wep' ] = "copper sword"
            self.inv[ 'arm' ] = "copper armour"
            self.nonMagicAtt = self.nonMagicAtt + 2
            self.defense = self.defense + 2 
            
        elif self.job == "Wizard" :
            self.currenthp = self.hitpoints
            self.abilitlist = ""
            self.inv[ 'wep' ] = "wooden staff"
            self.inv[ 'arm' ] = "wool robe"
            self.MagicAtt = self.MagicAtt +2
            self.defense = self.defense + 2 
        #Log Creation Completion
        self.logger.logInfo(self.characterStatsToString())
        self.logger.logInfo("Combatant creation completed")


    def characterStatsToString(self):
        stringToReturn = "Basic Values: "
        Combatant.combatantStatsToString(self)
        stringToReturn += "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(self.type, self.currenthp, self.invname, self.lvl, self.job, self.nonMagicAtt, self.MagicAtt, self.hit, self.evasion, self.defense)
        return stringToReturn
        return stringToReturn