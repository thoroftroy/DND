import random
#roll to hit
ac = input('Armor Class of Enemy:') 
attackRoll = (random.randint(1,20))
if(int(ac) > attackRoll):
    print('Miss')
else:
    print('Hit')

#speed calculation (Dnd has speed in sp/6sec and I need it in mps)
#1 ft/s = 0.681818 mph
sp = input('Players Speed:') #change this to players speed
baseSec = 6 #this is based on the turn speed in dnd
fts = round(int(sp)/baseSec)
spCalc = int(sp)*0.681818
w = input('Weight of the person (lbs):')
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
d = 985 #average human density
v = int(w)/d
m = v*d
f = m*int(sp)
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
