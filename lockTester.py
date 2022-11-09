import time
import random
listLen = 'null'
#Alrighty this will allow a preprogrammed lock to be opened
#the correct combo will be
winComboDef = '123456789'
#now lets let the user try to crack the code
def randomize(winCombo,i,listLen):
    typeChoose = input('How many didgets do you want it to be? (1-10 didgets or random to randomize it) ')
    if(typeChoose == '1'):
        winCombo = str(random.randint(1,9))
        convStr(winCombo,i,listLen)
    elif(typeChoose == '2'):
        winCombo = str(random.randint(1,99))
        convStr(winCombo,i,listLen)
    elif(typeChoose == '3'):
        winCombo = str(random.randint(1,999))
        convStr(winCombo,i,listLen)
    elif(typeChoose == '4'):
        winCombo = str(random.randint(1,9999))
        convStr(winCombo,i,listLen)
    elif(typeChoose == '5'):
        winCombo = str(random.randint(1,99999))
        convStr(winCombo,i,listLen)
    elif(typeChoose == '6'):
        winCombo = str(random.randint(1,999999))
        convStr(winCombo,i,listLen)
    elif(typeChoose == '7'):
        winCombo = str(random.randint(1,9999999))
        convStr(winCombo,i,listLen)
    elif(typeChoose == '8'):
        winCombo = str(random.randint(1,99999999))
        convStr(winCombo,i,listLen)
    elif(typeChoose == '9'):
        winCombo = str(random.randint(1,999999999))
        convStr(winCombo,i,listLen)
    elif(typeChoose == '10'):
        winCombo = str(random.randint(1,9999999999))
        convStr(winCombo,i,listLen)
    elif(typeChoose == 'random'):
        winCombo = str(random.randint(1,random.randint(1,9999999999)))
        convStr(winCombo,i,listLen)
    else:
        print('Please input a valid number')
        randomize(winCombo,i,listLen)

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
