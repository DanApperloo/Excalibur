from Utilities.LoggingUtilities.LoggingUtil import *
from GameEngine.Database.ItemLibrary import *

class Combatant(object):

    logger = LoggingUtil("Combatant")

    def __init__(self, nameIn, lvlIn, jobIn, nonMagIn, magIn, hitIn, evasIn, defIn, hitPointsIn, expin):
        self.name = nameIn
        self.job = jobIn
        self.nonMagicAtt = int(nonMagIn)
        self.MagicAtt = int(magIn)
        self.hit = int(hitIn)
        self.evasion = int(evasIn)
        self.defense = int(defIn)
        self.hitpoints = int(hitPointsIn)
        self.currenthp = int(hitPointsIn)
        self.exp = expin
        self.lvl = lvlIn
        self.invname = self.name+"'s Inventory"
        self.inv = dict( wep = "", arm = "", acc = "")
        self.abilitlist = ""

        #Log Creation Completion
        #self.logger.logInfo(self.combatantStatsToString())
        self.logger.logInfo("Combatant creation completed")

    def updateStats(self,job):
        x = 5 
        self.lvl = self.lvl + 1 
        if self.job == "Fighter":
            self.nonMagicAtt = self.nonMagicAtt + x
            self.MagicAtt = self.MagicAtt + int(x/2)
            self.hit = self.hit + x
            self.evasion = self.evasion + int(x/2)
            self.defense = self.defense + x
            self.hitpoints = self.hitpoints +(x*2)
            
        elif self.job == "Wizard":
            self.nonMagicAtt = self.nonMagicAtt + int(x/2)
            self.MagicAtt = self.MagicAtt + x
            self.hit = self.hit + int(x/2)
            self.evasion = self.evasion + x
            self.defense = self.defense + int(x/2)
            self.hitpoints = self.hitpoints +x
        
        elif self.job == "Ranger":
            self.nonMagicAtt = self.nonMagicAtt + x
            self.MagicAtt = self.MagicAtt + int(x/2)
            self.hit = self.hit + x
            self.evasion = self.evasion + int(x/2)
            self.defense = self.defense + x
            self.hitpoints = self.hitpoints +(x*2)

    def updateHealth(self):
        print "runs to here"

    def updateLvl(self):
        print "runs to here"

    def updatEquipment(self,eqtype,eqname):
        
        if eqtype == "wep" :
            self.nonMagicAtt = self.nonMagicAtt - weapondict[self.inv["wep"]]  
            self.inv[ "wep" ] = eqname
            self.nonMagicAtt = self.nonMagicAtt + weapondict[self.inv["wep"]]
        elif eqtype == "arm" : 
            self.defense = self.defense - armourdict[self.inv["arm"]]  
            self.inv[ "arm" ] = eqname
            self.defense = self.defense + armourdict[self.inv["arm"]]
            
        elif eqtype == "acc":
            self.evasion = self.evasion - accessdict[self.inv["acc"]]  
            self.inv[ "acc" ] = eqname
            self.evasion = self.evasion + accessdict[self.inv["acc"]]
            
        else:
            print "runs to here"

    def combatantStatsToString(self):
        stringToReturn = "Basic Values: "
        stringToReturn += "{0} {1!s} {2!s} {3!s} {4!s} ".format(self.name, self.lvl, self.nonMagicAtt, self.MagicAtt, self.hit)
        stringToReturn += "{0!s} {1!s} {2!s} {3} {4}".format(self.evasion, self.defense, self.currenthp, self.invname, self.job)
        return stringToReturn

