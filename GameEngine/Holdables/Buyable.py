from GameEngine.Database.ItemLibrary import *

class Buyable(object) :
    
    def __init__(self,StoreName):
        self.StoreIn = StoreName
        
        
    def StoreSelector(self,StoreName):
        StoreInvList = ""
        if StoreName == "Coral" :
            StoreInvList = ""
            return StoreInvList
        elif StoreName == "Blodel":
            StoreInvList = ""
            return StoreInvList
    