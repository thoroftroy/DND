#marcuses 8 ball
import random
import time

futures = ["Yes","No","Of course not","Follow your heart","That is correct","What do you think?","I would say yes?"]
directions = ['north','south','east','west','up','left','down','right']

def rollDir():
    print('Well...')
    randRoll = random.randint(0,len(directions)-1)
    waitTime = (random.randint(1,4))*0.2
    time.sleep(waitTime)
    print("|")
    print(directions[randRoll])
    print("|")

def roll():
    print('Well...')
    randRoll = random.randint(0,len(futures)-1)
    waitTime = (random.randint(1,4))*0.2
    time.sleep(waitTime)
    print("|")
    print(futures[randRoll])
    print("|")

def whatDoYouWant():
    print("What would you like to know?")
    print("(EX: directions [this will tell you where to go], should I do... [it will tell you if you should]")
    what = input()
    if(what == "directions"):
        rollDir()
    else:
        roll()
    whatDoYouWant()
    
whatDoYouWant()
