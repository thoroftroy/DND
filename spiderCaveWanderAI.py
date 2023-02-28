#this is meant to randomly move a big boi all over the dungeon
import time
import random
#               0       1                   2                   3                       4               5       6       7       8           9       10
locations = ["Starting Room","Small Monster Cave","Large Monster Cave","Medium Monster Cave","Monster Cave","Boss 1","Boss 2","Mimic","Treasure","Water","Healing Well"]
waitTime = random.randint(10,60)
location = locations[random.randint(0,len(locations)-1)]

def wander(location):
    print("|")
    print("Wandering...")
    print("|")
    time.sleep(waitTime)
    if(location == locations[0]):   #if the wanderer is in the starting room he can only go to the small monster cave
        location = locations[1] #small monster cave
        print("Enters into",location)
    elif(location == locations[1]): #if he is in the small monster cave he can go to either the monster cave or the large monster cave
        choose = random.randint(0,2)
        if(choose == 0):
            location = locations[2] #Large Monster Cave
            print("Enters into",location)
        elif(choose == 1):
            location = locations[4] #Monster Cave
            print("Enters into",location)
        elif(choose == 2):
            location = locations[0] #Starting Room
            print("Enters into",location)
        else:
            print("Something is wrong")
    elif(location == locations[2]): #if he is in the large monster cave he can go to, small monster cave, healing well, treasure room, or medium monster cave
        choose = random.randint(0,3)
        if(choose == 0):
            location = locations[1]  #staring room
            print("Enters into",location)
        elif(choose == 1):
            location = locations[10] #healing well
            print("Enters into",location)
        elif(choose == 2):
            location = locations[8]  #Treasure room
            print("Enters into",location)
        elif(choose == 3):
            location = locations[3]  #Medium monster Cave
            print("Enters into",location)
        else:
            print("Something is wrong")
    elif(location == locations[3]): #if he is in the Medium monster Cave he can go to, Monster Cave or monster cave large
        choose = random.randint(0,1)
        if(choose == 0):
            location = locations[2] #monster cave large
            print("Enters into",location)
        elif(choose == 1):
            location = locations[4] #monster cave
            print("Enters into",location)
        else:
            print("Something is wrong")
    elif(location == locations[4]): #if he is in the Monster Cave he can go to, Small monster cave, medium monster cave, or boss 1
        choose = random.randint(0,2)
        if(choose == 0):
            location = locations[1] #small monster cave
            print("Enters into",location)
        elif(choose == 1):
            location = locations[3] #medium monster cave
            print("Enters into",location)
        elif(choose == 2):
            location = locations[5] #boss 1 room 
            print("Enters into",location)
        else:
            print("Something is wrong")
    elif(location == locations[5]): #if he is in Boss 1 then he can go, treasure or monster cave
        choose = random.randint(0,1)
        if(choose == 0):
            location = locations[4] #treasure room
            print("Enters into",location)
        elif(choose == 1):
            location = locations[8] #monster cave
            print("Enters into",location)
        else:
            print("Something is wrong")
    elif(location == locations[6]): #if he is in Boss 2 then he can go to healing well or mimic
        choose = random.randint(0,1)
        if(choose == 0):
            location = locations[10] #healing well
            print("Enters into",location)
        elif(choose == 1):
            location = locations[7] #mimic
            print("Enters into",location)
        else:
            print("Something is wrong")
    elif(location == locations[7]): #if he is in Mimic he can go to Boss 2
        location = locations[6] #boss 2
        print("enters into",location)
    elif(location == locations[8]): #if he is in Treasure he can go to boss 1 or Large monster room
        choose = random.randint(0,1)
        if(choose == 0):
            location = locations[5] #boss 1
            print("Enters into",location)
        elif(choose == 1):
            location = locations[2] #large monster room
            print("Enters into",location)
        else:
            print("Something is wrong")
    elif(location == locations[9]): #if he is in Water he can go to the healing well
        location = locations[10] #healing well
        print("Enters into",location)
    elif(location == locations[10]): #if he is in Healing Well he can enter Boss 2, Water, Monster Cave Large
        choose = random.randint(0,2)
        if(choose == 0):
            location = locations[6] #boss 2
            print("Enters into",location)
        elif(choose == 1):
            location = locations[9] #water
            print("Enters into",location)
        elif(choose == 2):
            location = locations[2] #Large monster cave
            print("Enters into",location)
        else:
            print("Something is wrong")
    else:
        print("Something is wrong")
    wander(location)
        
print("Starts in",location)
wander(location)
