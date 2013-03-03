from DataCreation.Models.Factories.MonsterFactoryModel import *
from DataCreation.Models.Factories.CharacterFactoryModel import *
from GameEngine.Actions.AttackAction import *
#from Resources import *

#print Factory("..\datafiles\schemes\Monster.xsd").Schemavalidate("..\datafiles\data\monsters\Basilisk.xml")
warr1 = MonsterFactory().Createmonster2("/Game/Resources/datafiles/character data/Basilisk.xml")
warr2 = CharacterFactory("/Game/Resources/datafiles/character data/Character.xsd").CreateCharacter("/Game/Resources/datafiles/character data/Nick.xml")
#attc1 =AttackAction()
#attc1.DamageCalc(warr1,warr2)
#attc1.DamageCalc(warr1,warr2)
#attc1.DamageCalc(warr1,warr2)
#attc1.DamageCalc(warr1,warr2)
#attc2 =  AttackAction()
#attc2.DamageCalc(warr2,warr1)
#attc2.DamageCalc(warr2,warr1)
#attc2.DamageCalc(warr2,warr1)
#attc2.DamageCalc(warr2,warr1)
#attc2.SkillDamage(warr2,warr1,"Fire3")
#attc2.SkillDamage(warr2,warr2,"Heal")