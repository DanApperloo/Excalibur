from Utilities.LoggingUtilities.LoggingUtil import *
from GameEngine.Combatants.Combatant import *

class Monster(Combatant):

    logger = LoggingUtil("Monster")

    def __init__(self, nameIn, lvlIn, jobIn, typeIn, nonMagIn, magIn, hitIn, evasIn, defIn, hitPointsIn, expin):
        Combatant.__init__(self, nameIn, lvlIn, jobIn, nonMagIn, magIn, hitIn, evasIn, defIn, hitPointsIn, expin)
        self.type = typeIn
        self.creation()

    def creation(self):
        

        if self.job == "Fighter": 
            self.currenthp = self.hitpoints
            self.abilitlist = "Power Attack"

        elif self.job == "Wizard" :
            self.currenthp = self.hitpoints
            self.abilitlist = "Fire"

        elif self.job == "Ranged" :
            self.currenthp = self.hitpoints
            self.abilitlist = "Head Shot"

        #Log Creation Completion
        self.logger.logInfo(self.monsterStatsToString())
        self.logger.logInfo("Monster creation completed")

    def monsterStatsToString(self):
        stringToReturn = "Basic Values: "
        Combatant.combatantStatsToString(self)
        stringToReturn += "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(self.type, self.currenthp, self.invname, self.lvl, self.job, self.nonMagicAtt, self.MagicAtt, self.hit, self.evasion, self.defense)
        return stringToReturn
