#Asset class for Straight Line depreciation

class Asset:
    """SL Depreciation"""
    def __init__(self,c=0.0,s=0.0,lf=0):
        self.setCost(c)
        self.setSalvage(s)
        self.setLife(lf)
        self._error = ""
        if self.isValid():
            self.buildAsset()
        else:
            self._anndep = 0.0
            
    def setCost(self,c):
        self._cost = c
    def getCost(self):
        return self._cost
    def setSalvage(self,s):
        self._salvage = s
    def getSalvage(self):
        return self._salvage
    def setLife(self,lf):
        self._life = lf
    def getLife(self):
        return self._life

    def isValid(self):
        self._error = ""
        valid = True
        if self._cost <= 0.0:
            self._error += "Cost must be positive. \n"
            valid = False
        if self._salvage < 0.0:
            self._error == "Salvage cannot be negative. \n"
            valid = False
        if self._life <= 0:
            self._error += "Life must be positive. \n"
            valid = False
        if self._salvage >= self._cost:
            self._error += "Salvage must be less than cost. \n"
            valid = False
        return valid
    
    def buildAsset(self):
        self._anndep = (self._cost - self._salvage) / self._life

    def getErrorMsg(self):
        return self._error
    def getAnnDep(self):
        return self._anndep
    def getBegBal(self,yr=0):
        if yr <= 0 or yr > self._life:
            return -1
        bbal = self._cost - (self._anndep * (yr - 1))
        return bbal
    def getEndBal(self,yr=0):
        if yr <= 0 or yr > self._life:
            return -1
        return self._cost - (self._anndep * yr)
    
        
    
            
            
