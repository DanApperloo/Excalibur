import random
from GameEngine.Actions.Skill import* 


class AttackAction(object):
    

    def __init__(self):
        self.atta = ""
        self.defe = ""
        self.skill = ""
        self.magatt = ""
        
        
        
    def HitEstim(self,attacker,defender):
        att = attacker.findtext("acc")
        defense = defender.findtext("evn")
        
        if att >= defense:
            return ">=50%"
        else:
            return "<50%"
               
    @staticmethod    
    def HitEval(attacker, defender):
        if((attacker.hit+random.randint(0,attacker.hit)) - (defender.evasion+random.randint(0,defender.evasion)) > 0):                         #If structure ----- If({condition to check}):
            return True                              #                      {Good Case}
        else:                                        #                   else:
            return False                             #                      {Fail Case}
        
    def DamageCalc(self,attacker,defender):
        self.atta = attacker
        self.defe = defender
        
        if ( AttackAction.HitEval(self.atta,self.defe) == True ):
            damage = self.atta.nonMagicAtt - self.defe.defense                           #Notice that targetchar is being passed in then its defense value is being grabbed
            if(damage < 0):                             
                damage = 1
                print self.atta.name +" did " + str(damage) + " Damage!"                      #Everything needs to be a string in print, so use str({thing to chang}) to do so
                self.defe.currenthp = (self.defe.currenthp - damage)                              #Again notice the referencing
                print self.defe.name +" has " + str(self.defe.currenthp) + " HP left!"              #Print doesn't need to have () around its output
                return
            else:
                print self.atta.name +" did "+ str(damage) + " Damage!"                      #Everything needs to be a string in print, so use str({thing to chang}) to do so
                self.defe.currenthp = (self.defe.currenthp - damage)                              #Again notice the referencing
                print self.defe.name +" has " + str(self.defe.currenthp) + " HP left!"              #Print doesn't need to have () around its output
                return
                
        else:
            print "Attack missed"
            
    @staticmethod        
    def HitPointCheck(atta,defe):
        if defe.currenthp > 0 :
            return True
        else:
            atta.exp = atta.exp + defe.exp
            if int(atta.exp) >= 100 :
                atta.updateStats(atta,atta.job)
                pass
            else:
                pass
            print defe.name + "  has Died  " + atta.name + " has Gained "+ str(defe.exp) + " exp"
        
    def SkillDamage(self,attacker,defender,skillname):
        self.atta = attacker
        self.defe = defender
        self.skill = skillname
        
        if AttackAction.HitEval(self.atta,self.defe)== True:
            damage = SkillAttack.SkillSelecter(self.atta,self.defe,self.skill)                           #Notice that targetchar is being passed in then its defense value is being grabbed
            if(damage < 0):                             
                damage = 1
                print self.atta.name +" did " + str(damage) + " Damage!"                      #Everything needs to be a string in print, so use str({thing to chang}) to do so
                self.defe.currenthp = (self.defe.currenthp - damage)
                 
                if self.HitPointCheck(self.atta, self.defe) == True :                             #Again notice the referencing
                    print self.defe.name +" has " + str(self.defe.currenthp) + " HP left!"              #Print doesn't need to have () around its output
                else:
                    pass
            elif damage == "heal" :
                print self.atta.name +" Healed "                    #Everything needs to be a string in print, so use str({thing to chang}) to do so
                if self.defe.currenthp > self.defe.hitpoints:
                    self.defe.currenthp = self.defe.hitpoints
                    pass
                    
                if self.HitPointCheck(self.atta, self.defe) == True :                             #Again notice the referencing
                    print self.defe.name +" has " + str(self.defe.currenthp) + " HP left!"              #Print doesn't need to have () around its output
                else:
                    pass                
            else:
                print self.atta.name +" did "+ str(damage) + " Damage!"                      #Everything needs to be a string in print, so use str({thing to chang}) to do so
                self.defe.currenthp = (self.defe.currenthp - damage)                              #Again notice the referencing
                if self.HitPointCheck(self.atta, self.defe) == True :                             #Again notice the referencing
                    print self.defe.name +" has " + str(self.defe.currenthp) + " HP left!"              #Print doesn't need to have () around its output
                else:
                    return
        else:
            print "Attack missed"
            

        
            
        