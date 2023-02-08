#marcuses 8 ball
import random
import time

futures = ["Yes","No","Of course not","Follow your heart","That is correct","What do you think?","I would say yes?"]
directions = ['north','south','east','west','up','left','down','right']
#do this, adj, to a, time, urgency
cryptMssg1 = ["Follow the","Eat a","Drink the","Trust a","Play with the","Act like a","Prevent the","Be aware of the attack from the","Watch out for the","Choose to listen to the","Divert the"]
cryptMssg2 = ["yellow", "red","slimey", "fast", "orange","blue","quiet","smart","dangorus","evil","bloody","light","pretty","soft","gentle","radiant"]
cryptMssg3 = ["bear","chicken"," friend","enemy","monster", "preist"," waffle","monkey","student","zombie","ghost","master","ally","gladiator","fighter","mage","magic caster","witch","water"]
cryptMssg4 = ["for a while","sometime soon","before sundown","tomorow","any time soon","when the time is right","to lift the fear","at night"]
cryptMssg5 = ["quickly, before it's too late!","OR DIE!","hurry, you must do this!","to save a loved one","or your friend will die","to save the day","to help the town"]

#say something cryptic
def cryptMessage():
    print("Well...")
    waitTime = (random.randint(5,10))*0.2
    time.sleep(waitTime)
    print(cryptMssg1[random.randint(0,len(cryptMssg1)-1)],cryptMssg2[random.randint(0,len(cryptMssg2)-1)],cryptMssg3[random.randint(0,len(cryptMssg3)-1)],cryptMssg4[random.randint(0,len(cryptMssg4)-1)],cryptMssg5[random.randint(0,len(cryptMssg5)-1)])

#roll some directions
def rollDir():
    print('Well...')
    randRoll = random.randint(0,len(directions)-1)
    waitTime = (random.randint(1,4))*0.2
    time.sleep(waitTime)
    print("|")
    print(directions[randRoll])
    print("|")
#do a normal roll
def roll():
    print('Well...')
    randRoll = random.randint(0,len(futures)-1)
    waitTime = (random.randint(1,4))*0.2
    time.sleep(waitTime)
    print("|")
    print(futures[randRoll])
    print("|")
#main loop
def whatDoYouWant():
    what = input()
    if(what == "directions"):
        rollDir()
    elif(what == "0000"):
        cryptMessage()
    else:
        crypt = random.randint(0,2000)
        if(crypt == 1):
            cryptMessage()
        else:
            roll()
    print("What would you like to know now?")
    whatDoYouWant()
    
print("What would you like to know?")
print("(EX: directions [this will tell you where to go], should I do... [it will tell you if you should])")
whatDoYouWant()
