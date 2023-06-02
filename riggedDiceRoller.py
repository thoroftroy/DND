#Program to roll a dice
import random
import time

modifiers = [8,1,5,-3,-3,2]
savingModifiers = [11,1,8,-3,-3,-2]

def rollSpecs(roll):
    howMany = 0
    howMany = int(input("How many dice do you want to roll? "))
    whatDice = input("What dice would you like to roll? [d4, d6, d8, d10, d12, d20, d100] ")
    rollMod = int(input("What would you like to add to the roll? "))
    while howMany != 0:
        rollADice(roll,whatDice)
        howMany -= 1
    roll.append(rollMod)
    total(roll)
    
def rollSpecsRigged(roll):
    howMany = 0
    howMany = int(input("How many dice do you want to roll? "))
    whatDice = input("What dice would you like to roll? [d4, d6, d8, d10, d12, d20, d100] ")
    rollMod = int(input("What would you like to add to the roll? "))
    while howMany != 0:
        rollRiggedDice(roll,whatDice)
        howMany -= 1
    roll.append(rollMod)
    total(roll)
    
def rollSpecsBad(roll):
    howMany = 0
    howMany = int(input("How many dice do you want to roll? "))
    whatDice = input("What dice would you like to roll? [d4, d6, d8, d10, d12, d20, d100] ")
    rollMod = int(input("What would you like to add to the roll? "))
    while howMany != 0:
        rollBadDice(roll,whatDice)
        howMany -= 1
    roll.append(rollMod)
    total(roll)

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

def total(roll):
    rollTotal = sum(roll)
    print(rollTotal," is the current total")

def main():
    roll = []
    action = input("What do you want to do? ")
    if action == "roll" or action == "roll0":
        rollSpecs(roll)
    elif action == "rigged roll" or action == "roll1":
        rollSpecsRigged(roll)
    elif action == "bad roll" or action == "roll2":
    	rollSpecsBad(roll)
    elif action == "clear":
        times = 25
        while times != 0:
            time.sleep(0.01)
            print("|")
            times -= 1
    elif action == "d20":
    	print("Rolled: ", random.randint(1,20))
    elif action == "saving throw":
    	print("type the number index of which throw you are doing")
    	throw = int(input("str, dex, con, int, wis, cha "))
    	savingThrowRoll = random.randint(1,20)+savingModifiers[throw]
    	print("Saving Throw: ",savingThrowRoll)
    elif action == "skill check":
    	print("type the number index of which throw you are doing")
    	check = int(input("str, dex, con, int, wis, cha "))
    	skillCheckRoll = random.randint(1,20)+modifiers[check]
    	print("Skill Check: ",skillCheckRoll)
    else:
        print("That is not a valid action")
    main()

main()
