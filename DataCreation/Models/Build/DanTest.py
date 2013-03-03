from DataCreation.Models.Factories.BaseFactoryModel import *
from DataCreation.Models.Factories.MonsterFactoryModel import *


print Factory("..\datafiles\schemes\Monster.xsd").Schemavalidate( "..\datafiles\data\monsters\Basilisk.xml")
print MonsterFactory().Createmonster2("..\datafiles\data\monsters\Basilisk.xml")
