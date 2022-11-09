#randomized password assigner 
import time
import random
listLen = 'null'
#Alrighty this will allow a preprogrammed lock to be opened
#the correct combo will be randomized
def randomize():
    winComboDef = random.randint(1,100000000)
    print('Code is ',winComboDef)
    changeLock(winComboDef)
#now lets let the user try to crack the code
def cracking(winComboList,i,listLen):
    i += 1
    if(i<listLen):
        checkNum(i,winComboList,listLen)
    else:
        print('You unlocked it!')
        print('Now you can go again if you want!')
        changeLock()
        
def checkNum(i,winComboList,listLen):
    num = str(input('What is the next symbol? (type exit to give up) '))
    if(num == winComboList[i]):
        print('Yes!')
        print('')
        time.sleep(0.15)
        cracking(winComboList,i,listLen)
    elif(num == 'exit'):
        changeLock()
    else:
        print('Click! The switches reset!')
        i = -1
        print('')
        time.sleep(0.15)
        cracking(winComboList,i,listLen)
        
    
#but this can be changed
def changeLock(winComboDef): 
    i = -1
    listlen = 9
    change = str(input('Do you want to try agian? (1=yes 2=exit) '))
    if(change == '1') | (change == 'Yes') | (change == 'yes'):
        print('Keeping Current Lock')
        print(' ')
        winCombo = winComboDef
        convStr(winCombo,i,listLen)
    elif(change == '2') | (change == 'exit') | (change == 'Exit'):
        exit
    else:
        print('Try Again')
        changeLock(winComboDef)
#Just some code to turn the string into a list
def convStr(winCombo,i,listLen): 
    winComboList = list(winCombo)
    listLen = int(len(winComboList))
    cracking(winComboList,i,listLen)

randomize()
