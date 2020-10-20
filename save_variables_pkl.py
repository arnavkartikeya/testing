import pickle

saveFileName = "data.pkl"

#region string
def saveString(variableName, value):
    vardict = {}
    try:
        with open(saveFileName, "rb") as f:
            vardict = pickle.load(f)
    except:
        pass
    try:
        vardict[variableName] = value
    except:
        print("error saving variable")

    with open(saveFileName, 'wb') as f:
        pickle.dump(vardict, f)

def getString(variableName, defaultValue = ""):
    vardict = {}
    try:
        with open(saveFileName, "rb") as f:
            vardict = pickle.load(f)
    except:
        pass
    try:
        return vardict[variableName]
    except:
        return defaultValue
#endregion

def getArray(variableName, defaultValue = []):
    vardict = {}
    try:
        with open(saveFileName, "rb") as f:
            vardict = pickle.load(f)
    except:
        pass
    try:
        return vardict[variableName]
    except:
        return defaultValue

def getAllValues(defaultValue = {}):
    vardict = {}
    try:
        with open(saveFileName, "rb") as f:
            vardict = pickle.load(f)
    except:
        pass
    try:
        return vardict
    except:
        return defaultValue

def delete(variableName):
    vardict = {}
    try:
        with open(saveFileName, "rb") as f:
            vardict = pickle.load(f)
    except:
        pass
    try:
        vardict.pop(variableName)
    except:
        print("error removing variable")

    with open(saveFileName, 'wb') as f:
        pickle.dump(vardict, f)


def setSaveFileName(path):
    global saveFileName
    saveFileName = path
    fole = open(saveFileName, "a")
    fole.close()