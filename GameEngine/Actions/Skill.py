


class SkillAttack(object):
    
    
    @staticmethod
    def TypeMatch(type2,type1):
        typeDict = {"fire":"ice", "lit":"aqua", "ice":"fire", "aqua":"earth", "earth":"lit", "heal":"heal"}
        if type1 == typeDict[type2]:
            return True
        elif type2 == "heal":
            return "heal"
        else:
            return False
        
    @staticmethod    
    def DamageCalc(pwrvar,typem,atta,defe):
        if typem == True:
            damage = ((atta.MagicAtt*pwrvar) - (defe.defense))
            damage = damage * 2 
            return damage
        elif "heal" == typem :
            defe.currenthp = (defe.currenthp + (atta.MagicAtt*pwrvar))
            damage = "heal"
            return damage
        else:
            damage = ((atta.MagicAtt*pwrvar) - (defe.defense))
            return damage

    @staticmethod
    def SkillSelecter(atta,defe,skill):
    
        if skill == "Fire":
            elem = "fire"
            pwrvar = 1 
            damage = SkillAttack.DamageCalc(pwrvar,SkillAttack.TypeMatch(elem,defe.type),atta,defe)
            return damage

        elif skill ==  "Fire2":
            elem = "fire"
            pwrvar = 2 
            damage = SkillAttack.DamageCalc(pwrvar,SkillAttack.TypeMatch(elem,defe.type),atta,defe)
            return damage
        
        elif skill ==  "Fire3":
            elem = "fire"
            pwrvar = 3
            damage = SkillAttack.DamageCalc(pwrvar,SkillAttack.TypeMatch(elem,defe.type),atta,defe)
            return damage


        elif skill ==  "Ice":
            damage = (atta.MagicAtt) - (defe.defense)
            elem = "ice"
            return damage


        elif skill ==  "Ice2":
            elem = "ice"
            pwrvar = 2 
            damage = SkillAttack.DamageCalc(pwrvar,SkillAttack.TypeMatch(elem,defe.type),atta,defe)            
            return damage


        elif skill ==  "Ice3":
            damage = (atta.MagicAtt*3) - (defe.defense)
            elem = "ice"
            return damage


        elif skill ==  "Lit":
            damage = (atta.MagicAtt) - (defe.defense)
            elem = "lit"
            return damage


        elif skill ==  "Lit2":
            elem = "lit"
            pwrvar = 2 
            damage = SkillAttack.DamageCalc(pwrvar,SkillAttack.TypeMatch(elem,defe.type),atta,defe)
            return damage


        elif skill ==  "Lit3":
            damage = (atta.MagicAtt*3) - (defe.defense)
            elem = "lit"
            return damage
        
        elif skill ==  "Quake":
            damage = (atta.MagicAtt*1.5) - (defe.defense/1.5)
            elem = "earth"
            return damage
        
        
        elif skill ==  "Posion":
            damage = (atta.MagicAtt*2) - (defe.defense/2)
            elem = "pois"
            return damage
        
        elif skill ==  "Heal":
            elem = "heal"
            pwrvar = 1 
            damage = SkillAttack.DamageCalc(pwrvar,SkillAttack.TypeMatch(elem,defe.type),atta,defe)
            return damage
        
        elif skill ==  "Heal2":
            elem = "heal"
            pwrvar = 2 
            damage = SkillAttack.DamageCalc(pwrvar,SkillAttack.TypeMatch(elem,defe.type),atta,defe)
            return damage        
        
        elif skill ==  "Heal3":
            elem = "heal"
            pwrvar = 3 
            damage = SkillAttack.DamageCalc(pwrvar,SkillAttack.TypeMatch(elem,defe.type),atta,defe)
            return damage        