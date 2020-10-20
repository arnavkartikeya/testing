import pickle as pkl


class KidClass:
    def __init__(self, id):
        self.id = id


class KidChannelVars(KidClass):
    def __init__(self, channel_id):
        super().__init__(channel_id)
        self.ssc = 1
        self.rmc = 5
        self.rrc = 4
        self.rrcc = 10
        self.bw = True
        self.spam = 20
        self.whitelist = False


class KidReactionRoles(KidClass):
    def __init__(self, id):
        super().__init__(id)
        self.roleDict = {}


class KidPolls(KidClass):
    def __init__(self, id):
        super().__init__(id)
        self.poll = None
        self.options = []
        self.votes = []


class KidServerVars(KidClass):
    def __init__(self, id):
        super().__init__(id)
        self.bannedPlayers = []
        self.mutedPlayers = []

class KidTimers(KidClass):
    def __init__(self, id):
        super().__init__(id)
        self.timers = []
        self.callbacks = []
        self.channelIDs = []

def getObjectFromFileAndCreateANewOneIfItDoesntExist(filename, cls, value):
    try:
        with open(filename, 'rb+') as f:
            try:
                l = pkl.load(f)
            except EOFError:
                l = []
                pkl.dump(l, f)
    except FileNotFoundError:
        with open(filename, 'xb') as f:
            l = []
            pkl.dump(l, f)
    for i in l:
        if i.id == value:
            obj = i
            break
    else:
        obj = cls(value)
        l.append(obj)
    with open(filename, 'wb') as f:
        pkl.dump(l, f)
    return obj


def getObjectFromFile(filename, value):
    try:
        with open(filename, 'rb+') as f:
            try:
                l = pkl.load(f)
            except EOFError:
                l = []
                pkl.dump(l, f)
        for i in l:
            if i.id == value:
                return i
        return None
    except:
        return None


def getAllObjectsFromFile(filename):
    try:
        with open(filename, 'rb+') as f:
            try:
                l = pkl.load(f)
                return l
            except EOFError:
                l = []
                pkl.dump(l, f)
                return l
        return None
    except:
        return None


def storeObjectInFile(filename, obj):
    try:
        with open(filename, 'rb') as f:
            l = pkl.load(f)
        for i in l:
            if i.id == obj.id:
                l.remove(i)
                break
        l.append(obj)
        with open(filename, 'wb') as f:
            pkl.dump(l, f)
    except:
        print("This file hasn't been initialized yet. Do popObjectFromFile first noob.")


def removeObjectFromFile(filename, value):
    try:
        with open(filename, 'rb+') as f:
            try:
                l = pkl.load(f)
            except EOFError:
                l = []
                pkl.dump(l, f)
    except FileNotFoundError:
        with open(filename, 'xb') as f:
            l = []
            pkl.dump(l, f)
    for i in l:
        if i.id == value:
            l.remove(i)
            break
    with open(filename, 'wb') as f:
        pkl.dump(l, f)
