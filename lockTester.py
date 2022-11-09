import time
import random
listLen = 'null'
#Alrighty this will allow a preprogrammed lock to be opened
#the correct combo will be
winComboDef = '123456789'
#now lets let the user try to crack the code
def randomize(winCombo,i,listLen):
    winCombo = str(random.randint(1,1000000000000))
    convStr(winCombo,i,listLen)
    
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
def changeLock(): 
    i = -1
    listlen = 9
    change = str(input('Do you want to change preset lock? (0=yes 1=no 2=exit 3=randomize password) '))
    if(change == '0') | (change == 'yes') | (change == 'Yes'):
        print('Changing Lock...')
        winCombo = input('Type numbers in order of lock with no spaces (ex: 768594321 [it can be more than 9 characters]) ')
        print(winCombo,' Is the new lock Number')
        time.sleep(0.5)
        print('|')
        time.sleep(0.5)
        waitTime = ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"]
        for x in waitTime:
            print(x)
        convStr(winCombo,i,listLen)
    elif(change == '1') | (change == 'no') | (change == 'No'):
        print('Keeping Current Lock')
        print(' ')
        winCombo = winComboDef
        convStr(winCombo,i,listLen)
    elif(change == '2') | (change == 'exit') | (change == 'Exit'):
        exit
    elif(change == '3') | (change == 'randomize') | (change == 'Randomize'):
        winCombo = winComboDef
        randomize(winCombo,i,listLen)
    else:
        print('Try Again')
        changeLock()
#Just some code to turn the string into a list
def convStr(winCombo,i,listLen): 
    winComboList = list(winCombo)
    listLen = int(len(winComboList))
    cracking(winComboList,i,listLen)
    
print('Default password is \'123456789\'')
changeLock()
