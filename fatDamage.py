import random
#roll to hit
ac = 15 #just an average ac
attackRoll = (random.randint(1,20)+2)
if(ac > attackRoll):
    print('Miss')
else:
    print('Hit')

#speed calculation (Dnd has speed in sp/6sec and I need it in mps)
#1 ft/s = 0.681818 mph
sp = 25 #change this to players speed
baseSec = 6 #this is based on the turn speed in dnd
fts = round(sp/baseSec)
spCalc = sp*0.681818

#Damage Calculator For Borbus Roll

#Here is what his force should be
#A throwing hammer does 1d6 bludgeoning
#thats around 700lbs of force, that being said we can assume that for
#every 700lbs of force you deal 1d6 damage
#this gives us some proportions we can work with
#1d6/700 = x/f
print('|')
print('Here is what it should actually be based on DND:')
print('(This is based on the amount of force from bludgeoning and their rolls, etc)')
print('|')
sp = spCalc
w = 400
d = 985
v = w/d
m = v*d
f = m*sp
print('Speed:',sp," Weight:",w,'Density: ',d)
print("Volume: ",v," Mass: ", m,'Force: ',f)
#Now lets calculate damage
p3 = round(f/700)
# make an I loop to do this as many times as p3 roll()
points = 0
pointsList = []
def roll(points):
    points = random.randint(1,6) + points
    pointsList.append(points)
for x in range(p3-1):
  roll(points)
print('Rolls:',pointsList)
p2 = sum(pointsList)
print('Borbus Damage: ',p2)

#9-54 for real damage if you have a speed of 25 and a weight of 400



