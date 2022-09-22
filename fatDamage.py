#Damage Calculator For Borbus Roll
import random
print('Here is the damage based on my math')
sp = 25
w = 400
d = random.randint(1,12)
print('Speed:',sp," Weight:",w," Dice Roll:",d)
damage = ((((sp/12)*(w/5))-(w/3))+d)-10
damage1 = round(damage)
print('Borbus Damage: ',damage1)

#Other Claculators 
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
sp = 25 #Speed is the most important factor, it make damage go up faster than weight ever will
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




#This is a python file that does the damage of a character I made, his whole thing is that he is really fat and rolls into enemies. Change the sp to the speed he is moving and the w to his current weight. I think my equation is more balanced but I tried matching it to dnd and real life physics as well

