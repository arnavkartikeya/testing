import classes as c
import pickle as pkl

t = c.getObjectFromFileAndCreateANewOneIfItDoesntExist("./test.pkl", c.Test, 5)

print(t.id)

print(t.p)

t.p = 34
print(t.p)

c.storeObjectInFile("./test.pkl", t)

t = c.getObjectFromFileAndCreateANewOneIfItDoesntExist("./test.pkl", c.Test, 7)

print(t.id)

print(t.p)

c.storeObjectInFile("./test.pkl", t)

with open("./test.pkl", 'rb') as f:
    print(pkl.load(f))
print("lol im editing this from my phone")