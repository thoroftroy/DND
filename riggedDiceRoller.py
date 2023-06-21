#Program to roll a dice
import random
import time
import math

#modifiers = [8,1,5,-3,-3,2]	#Stats for Thadicus
#savingModifiers = [11,1,8,-3,-3,-2]	#Stats for Thadicus
modifiers = [0,5,1,0,-1,3]	#Stats for Soren
savingModifiers = [0,5,1,0,-1,3]	#Stats for Soren
modiferNames = ["Strength", "Dexterity", "Constittion","Intelligence", "Wisdom", "Charisma"]

def rollSpecs(roll):
    howMany = 0
    howManyAvg = 0
    howMany = input("How many dice do you want to roll? ")
    if(howMany.isnumeric() == True):
        howMany = int(howMany)
        howManyAvg = int(howMany)
    else:
        print("That is not a number, defaulting to 1")
        howMany = 1
        howManyAvg = 1
    whatDice = input("What dice would you like to roll? [d4, d6, d8, d10, d12, d20, d100] ")
    rollMod = input("What would you like to add to the roll? ")
    if(rollMod.isnumeric() == True):
        rollMod = int(rollMod)
    else:
        print("That is not a valid number, defaulting to 0")
        rollMod = 0
    while howMany != 0:
        rollADice(roll,whatDice)
        howMany -= 1
    roll.append(rollMod)
    total(roll,rollMod,howManyAvg)
    
def rollSpecsRigged(roll):
    howMany = 0
    howManyAvg = 0
    howMany = input("How many dice do you want to roll? ")
    if(howMany.isnumeric() == True):
        howMany = int(howMany)
        howManyAvg = int(howMany)
    else:
        print("That is not a number, defaulting to 1")
        howMany = 1
        howManyAvg = 1
    whatDice = input("What dice would you like to roll? [d4, d6, d8, d10, d12, d20, d100] ")
    rollMod = input("What would you like to add to the roll? ")
    if(rollMod.isnumeric() == True):
        rollMod = int(rollMod)
    else:
        print("That is not a valid number, defaulting to 0")
        rollMod = 0
    while howMany != 0:
        rollRiggedDice(roll,whatDice)
        howMany -= 1
    roll.append(rollMod)
    total(roll,rollMod,howManyAvg)
    
def rollSpecsBad(roll):
    howMany = 0
    howManyAvg = 0
    howMany = input("How many dice do you want to roll? ")
    if(howMany.isnumeric() == True):
        howMany = int(howMany)
        howManyAvg = int(howMany)
    else:
        print("That is not a number, defaulting to 1")
        howMany = 1
        howManyAvg = 1
    whatDice = input("What dice would you like to roll? [d4, d6, d8, d10, d12, d20, d100] ")
    rollMod = input("What would you like to add to the roll? ")
    if(rollMod.isnumeric() == True):
        rollMod = int(rollMod)
    else:
        print("That is not a valid number, defaulting to 0")
        rollMod = 0
    while howMany != 0:
        rollBadDice(roll,whatDice)
        howMany -= 1
    roll.append(rollMod)
    total(roll,rollMod,howManyAvg)

def rollADice(roll,whatDice):
    rollTemp = 0
    print("Rolling...")
    time.sleep(0.1)
    if whatDice == "d4":
        rollTemp = random.randint(1,4)
    elif whatDice == "d6":
        rollTemp = random.randint(1,6)
    elif whatDice == "d8":
        rollTemp = random.randint(1,8)
    elif whatDice == "d10":
        rollTemp = random.randint(1,10)
    elif whatDice == "d12":
        rollTemp = random.randint(1,12)
    elif whatDice == "d20":
        rollTemp = random.randint(1,20)
    elif whatDice == "d100":
        rollTemp = random.randint(1,100)
    else:
        print("Defaulting to d20")
        rollTemp = random.randint(1,20)
    print(rollTemp," Rolled")
    roll.append(rollTemp)

def rollRiggedDice(roll, whatDice):
    rollTemp = 0
    print("Rolling...")
    time.sleep(0.1)
    if whatDice == "d4":
        rollTemp = random.randint(2,4)
    elif whatDice == "d6":
        rollTemp = random.randint(3,6)
    elif whatDice == "d8":
        rollTemp = random.randint(5,8)
    elif whatDice == "d10":
        rollTemp = random.randint(7,10)
    elif whatDice == "d12":
        rollTemp = random.randint(9,12)
    elif whatDice == "d20":
        rollTemp = random.randint(14,20)
    elif whatDice == "d100":
        rollTemp = random.randint(74,100)
    else:
        print("Defaulting to d20")
        rollTemp = random.randint(14,20)
    print(rollTemp," Rolled")
    roll.append(rollTemp)

def rollBadDice(roll, whatDice):
    rollTemp = 0
    print("Rolling...")
    time.sleep(0.1)
    if whatDice == "d4":
        rollTemp = random.randint(1,2)
    elif whatDice == "d6":
        rollTemp = random.randint(1,3)
    elif whatDice == "d8":
        rollTemp = random.randint(1,4)
    elif whatDice == "d10":
        rollTemp = random.randint(1,5)
    elif whatDice == "d12":
        rollTemp = random.randint(1,6)
    elif whatDice == "d20":
        rollTemp = random.randint(1,10)
    elif whatDice == "d100":
        rollTemp = random.randint(1,30)
    else:
        print("Defaulting to d20")
        rollTemp = random.randint(1,10)
    print(rollTemp," Rolled")
    roll.append(rollTemp)

def total(roll,rollMod,howManyAvg):
    rollTotal = sum(roll)
    rollAverage = sum(roll)/howManyAvg
    rollAverage = round(rollAverage,1)
    print("|")
    print(rollTotal," is the current total")
    print(rollMod,"was added to the total)")
    print(rollAverage,"is the average roll")
    print("|")

def rollSpecialNumber():
    floatOrInt = input("Do you want the numbers to include decimals in the roll? [y or n] ")
    if floatOrInt == "yes" or floatOrInt == "Yes" or floatOrInt == "y":
        sRollMin = input("What do you want the MINimum number to be? ")
        if(sRollMin.isnumeric() == True):
            sRollMin = float(sRollMin)
        else:
            sRollMin = float(0)
            print("Invalid selection, defaulting to 0")
        sRollMax = input("What do you want the MAXimum number to be? ")
        if(sRollMax.isnumeric() == True):
            sRollMax = float(sRollMax)
        else:
            sRollMax = float(10)
            print("Invalid selection, defaulting to 10")
        print("Roll:",random.uniform(sRollMin, sRollMax))
    else:
        sRollMin = input("What do you want the MINimum number to be? ")
        if(sRollMin.isnumeric() == True):
            sRollMin = int(sRollMin)
        else:
            sRollMin = int(0)
            print("Invalid selection, defaulting to 0")
        sRollMax = input("What do you want the MAXimum number to be? ")
        if(sRollMax.isnumeric() == True):
            sRollMax = int(sRollMax)
        else:
            sRollMax = int(10)
            print("Invalid selection, defaulting to 10")
        print("Roll:",random.randint(sRollMin,sRollMax))

def main():
    roll = []
    action = input("What do you want to do? ")
    if action == "roll" or action == "0":
        rollSpecs(roll)
    elif action == "rigged roll" or action == "1":
        rollSpecsRigged(roll)
    elif action == "bad roll" or action == "2":
        rollSpecsBad(roll)
    elif action == "clear" or action == "cls" or action == "7":
        times = 25
        while times != 0:
            time.sleep(0.01)
            print("|")
            times -= 1
    elif action == "d20" or action == "3":
        print("Rolled a d20:",random.randint(1,20))
    elif action == "saving throw" or action == "4":
        throw = None
        print("type the number index of which throw you are doing")
        print("0,   1,   2,   3,   4,   5")
        throw = input("str, dex, con, int, wis, cha ")
        if(throw.isnumeric() == True):
            throw = int(throw)
            if throw >= 0 and throw <= 6:
                pass
            else:
                print("Invalid numarical index, defaulting to 0")
                throw = 0
        else:
            print("Invalid numarical index, defaulting to 0")
            throw = 0
        savingThrowRoll = random.randint(1,20)+savingModifiers[throw]
        print(modiferNames[throw],"Saving Throw: ",savingThrowRoll)
    elif action == "skill check" or action == "5":
        check = 0
        print("type the number index of which throw you are doing")
        print("0,   1,   2,   3,   4,   5")
        check = input("str, dex, con, int, wis, cha ")
        if(check.isnumeric() == True):
            check = int(check)
            if check >= 0 and check <= 6:
                pass
            else:
                print("Invalid numarical index, defaulting to 0")
                check = 0
        else:
            print("Invalid numarical index, defaulting to 0")
            check = 0
        skillCheckRoll = random.randint(1,20)+modifiers[check]
        print(modiferNames[check],"Skill Check: ",skillCheckRoll)
    elif action == 'roll special' or action == '8':
        rollSpecialNumber()
    elif action == "list actions" or action == "list" or action == "6":
        print("roll, rigged roll, bad roll, d20, saving throw, skill check, list actions, clear, roll special")
        print("  0 	   1 	     2 	      3 	4 	    5,	    	6,	    7,	      8")
    elif action == "d4":
        print("Rolled a d4:",random.randint(1,4))
    elif action == "d6":
        print("Rolled a d6:",random.randint(1,6))
    elif action == "d8":
        print("Rolled a d8:",random.randint(1,8))
    elif action == "d10":
        print("Rolled a d10:",random.randint(1,10))
    elif action == "d12":
        print("Rolled a d12:",random.randint(1,12))
    elif action == "d100":
        print("Rolled a d100:",random.randint(1,100))
    else:
        print("That is not a valid action")
        print("(Type 'list actions' to view valid actions)")
    main()

print("Type 'list actions' to see what you can do ")
main()
