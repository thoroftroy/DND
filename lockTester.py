import time
#Alrighty this will allow a preprogrammed lock to be opened
#the correct combo will be
winComboDef = '123456789'
#now lets let the user try to crack the code
def cracking(winComboList,i):
    i = i + 1
    if(i<9):
        checkNum(i,winComboList)
    else:
        print('You unlocked it!')
        print('Now you can go again if you want!')
        changeLock()
        
def checkNum(i,winComboList):
    num = str(input('What is the next number? '))
    if(num == winComboList[i]):
        print('Yes, onto the next switch!')
        print('')
        time.sleep(0.25)
        cracking(winComboList,i)
    else:
        print('Click! The switches reset!')
        i = -1
        print('')
        time.sleep(0.25)
        cracking(i,winComboList)
        
    
#but this can be changed
def changeLock(): 
    i = -1
    change = input('Do you want to change preset lock? (0=yes 1=no 2=exit) ')
    if(change == '0'):
        print('Changing Lock...')
        winCombo = input('Type numbers 1-9 in order of lock with no spaces (ex: 768594321) ')
        print(winCombo,' Is the new lock Number')
        print(' ')
        convStr(winCombo,i)
    elif(change == '1'):
        print('Keeping Current Lock')
        print(' ')
        winCombo = winComboDef
        convStr(winCombo,i)
    elif(change == '2'):
        exit
    else:
        print('Try Again')
        changeLock()
#Just some code to turn the string into a list
def convStr(winCombo,i): 
    winComboList = list(winCombo)
    cracking(winComboList,i)
    

changeLock()
