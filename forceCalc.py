sp = input('Speed of the object in mph:') #speed in mph
w = input('Weight of the object:') #the weight of the person
d = input('Density of the object (985 for people):') #the dencity of an object, 985 is the average human dencity
v = int(w)/int(d) #this is the volume, don't worry about it
m = v*int(d) #the mass variable, it is being calculated for you (v*d)
f = m*int(sp) #now this is the actual force that is applied
#the force is the total force of the entire body not the actual force contact would make with it
print('(The average force of a punch is 150. It is 700 in dnd when you throw a hammer at something)')
print('|')
print('Speed:',sp," Weight:",w,'Density: ',d)
print("Volume: ",v," Mass: ", m,'Force: ',f)
