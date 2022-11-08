import time
#Alrighty this will allow a preprogrammed lock to be opened
#the correct combo will be
winComboDef = '983621574'
#now lets let the user try to crack the code
def cracking(winComboList,numVal):
    numVal = numVal + 1
    checkNum(numVal,winComboList)
        
def checkNum(numVal,winComboList):
    num = input('What is the next number?')
    if(num == winComboList[numVal]):
        print('Yes, onto the next switch!')
        time.sleep(1)
        cracking(winComboList,numVal)
    else:
        print('Click! The switches reset!')
        numVal = -1
        time.sleep(1)
        cracking(numVal,winComboList)
        
    
#but this can be changed
def changeLock(): 
    numVal = -1
    change = input('Do you want to change preset lock? (0=yes 1=no 2=exit) ')
    if(change == '0'):
        print('Changing Lock...')
        winCombo = input('Type numbers 1-9 in order of lock with no spaces (ex: 768594321) ')
        print(winCombo,' Is the new lock Number')
        print(' ')
        convStr(winCombo,numVal)
    elif(change == '1'):
        print('Keeping Current Lock')
        print(' ')
        winCombo = winComboDef
        convStr(winCombo,numVal)
    elif(change == '2'):
        exit
    else:
        print('Try Again')
        changeLock()
#Just some code to turn the string into a list
def convStr(winCombo,numVal): 
    winComboList = list(winCombo)
    cracking(winComboList,numVal)
    

changeLock()
