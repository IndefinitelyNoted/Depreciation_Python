#Deoreciation (control program) Jahmya Goodwin

import locale
import os
from Asset import Asset
from AssetDDL import AssetDDL

cost = 0.0
salv = 0.0
life = 0

def main():
    global cost,salv,life
    result = locale.setlocale(locale.LC_ALL,'')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, 'en_US')    #set to US if not by
    print("Welcome to the depreciation calculator.")

    choice = input("Asset by: <i>nput, <f>ile, or <q>uit (i/f/q): ")
    while len(choice) > 0 and choice[0].upper() != "Q":
        if choice [0].upper() == "I":
            cost = getValue("Asset cost: ", "f")
            salv = getValue("Salvage value: ","f")
            life = getValue("LIfe (years): ","i")
        else:
            #getAssetFile method looks for files of extension .ast
            #and reads cost/salv/life values from selected file
            #returns the file in 'path'
            path = getAssetFile()
            if path != None:
                print("File " + path + " read with values: " +
                      str(cost) + ", " + str(salv) + ", " + str(life))
        #after if-else is done we should have cost, salv, life
        if cost > 0:
            doDepreciation()
        else:
            print("Asset has no cost - not processed")
        choice = input("Asset by: <i>nput, <f>ile, or <q>uit (i/f/q): ")
    print("Thanks for using the depreciaton calculator")

def doDepreciation():
    global cost,salv,life

    #instantiate Asset objects to display start values and possible schedule
    asset = Asset(cost,salv,life) #for Straight Line version
    addl = AssetDDL(cost,salv,life) #double declining depreciation
    if asset.getErrorMsg() == "":
        print("The Straight Line annual depreciation values is %s " %locale.currency(asset.getAnnDep(),grouping=True))
        print("First Year DDL deprecation value is %s "%locale.currency(addl.getAnnDep(1),grouping=True))
        sched = input("Schedule: <S>L, <D>DL, <B>oth, <N>one (S/D/B/N): ")
        if len(sched) > 0:
            #a schedule may be needed
            if sched[0].upper() == "S" or sched[0].upper() == "B":
                #Do Straight-Line schedule
                print("\n      Straight Line Depreciation Schedule")
                print("Year    Beg.Bal.    Depreciation    End.Bal.")
                for i in range(1,asset.getLife()+1):
                    print("{:4}".format(i) +
                          "{:13,.2f} {:13,.2f} {:13,.2f}".format(asset.getBegBal(i),asset.getAnnDep(),asset.getEndBal(i)))
            if sched[0].upper() == "D" or sched[0].upper() == "B":
                print("\n      Double Declining Depreciation Schedule")
                print("Year    Beg.Bal.    Depreciation    End.Bal.    Dep.Pct.")
                for i in range(1,addl.getLife()+1):
                    print("{:4}".format(i) +
                          "{:13,.2f} {:13,.2f} {:13,.2f}".format(addl.getBegBal(i),addl.getAnnDep(i),addl.getEndBal(i)) +
                          " {:13,.2%}".format(addl.getAnnDepPct(i)))
                    
    else:
        print("Asset instantiation error: " + asset.getErrorMsg())

def getAssetFile():
    global cost,salv,life
    print("Asset Files Available: ")
    path = ""
    assets = []
    fnum = 0
    #display all /ast files in directory
    cwd = os.getcwd()
    for entry in os.listdir(cwd):
        path = os.path.join(cwd,entry)
        if os.path.isfile(path) and entry.endswith(".ast"):
            fnum += 1
            print(str(fnum) + ": " + entry)
            assets.append(path)
        #retun None if no files were found
    if fnum == 0:
        print("Sorry, no asset file found.")
        cost = 0.0
        salv = 0.0
        life = 0
        return None

    #let user select file if at least one is found
    path = ""
    while path == "":
        fnum = int(input("Which Asset File #: "))
        if fnum < 1 or fnum > len(assets):
            print("file number entered is out of range")
        else:
            path = assets[fnum-1]
    #read the selected file
    try:
        f = open(path,"r")
        cost = float(f.readline())
        salv = float(f.readline())
        life = int(f.readline())
        f.close()
        return path
    except OSError as e:
        print("Asset file " + path + " could not be read: " + str(e))
        cost = 0.0
        salv = 0.0
        life = 0
    except ValueError as e:
        print("Asset file " + path +  "was corrupt: " + str(e))
        cost = 0.0
        salv = 0.0
        life = 0
        return None

                
            
def getValue(prompt,dType):
    goodVal = False
    while not goodVal:
        try:
            if dType.lower() == "f":
                amt = float(input(prompt))
            elif dType.lower() == "i":
                amt = int(input(prompt))
            else:
                amt = input(prompt + " as String: ")
            goodVal = True
        except ValueError:
            if dType.lower() == "i":
                print("Positive integers only please.")
            else:
                print("Illegal input: non-numeric.")
            goodVal = False
    return amt

if __name__ == "__main__":
    main()
