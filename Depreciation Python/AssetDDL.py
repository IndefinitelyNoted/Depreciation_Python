#Double Declining Balance Depreciation

class AssetDDL():
    """DDL Deprecition"""

    def __init__(self,c=0.0,s=0.0,lf=0):
        self.setCost(c)
        self.setSalvage(s)
        self.setLife(lf)
        self._error = ""
        if self.isValid():
            self.buildAsset()
            
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
        self._bbal = [0] * self._life
        self._anndep = [0] * self._life
        self._ebal = [0] * self._life
        self._anndeppct = [0] * self._life

        self._rate = (1.0 / self._life) * 2.0;
        self._sldep = (self._cost - self._salvage) / self._life
        

        self._bbal[0] = self._cost
        for i in range(0,self._life):
            if i > 0:
                self._bbal[i] = self._ebal[i-1]
                
            depwrk = self._bbal[i] * self._rate
            if depwrk < self._sldep:
                depwrk = self._sldep
            if self._bbal[i] - depwrk < self._salvage:
                #can't go below salvage value
                depwrk = self._bbal[i] - self._salvage
            
            self._anndep[i] = depwrk
            self._ebal[i] = self._bbal[i] - self._anndep[i]
            self._anndeppct[i] = self._anndep[i] / self._cost

        

    def getErrorMsg(self):
        return self._error
    def getAnnDep(self,yr=0):
        if yr <= 0 or yr > self._life:
            return -1
        return self._anndep[yr-1]
    def getBegBal(self,yr=0):
        if yr <= 0 or yr > self._life:
            return -1
        return self._bbal[yr-1]
    def getEndBal(self,yr=0):
        if yr <= 0 or yr > self._life:
            return -1
        return self._ebal[yr-1]
    def getAnnDepPct(self,yr=0):
        if yr <= 0 or yr > self._life:
            return -1
        return self._anndeppct[yr-1]
            
