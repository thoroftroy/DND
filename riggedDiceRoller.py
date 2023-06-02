#Program to roll a dice
import random
import time

def rollSpecs(roll):
    howMany = 0
    howMany = int(input("How many dice do you want to roll? "))
    whatDice = input("What dice would you like to roll? [d4, d6, d8, d10, d12, d20] ")
    rollMod = int(input("What would you like to add to the roll? "))
    while howMany != 0:
        rollADice(roll,whatDice)
        howMany -= 1
    roll.append(rollMod)
    total(roll)
    
def rollSpecsRigged(roll):
    howMany = 0
    howMany = int(input("How many dice do you want to roll? "))
    whatDice = input("What dice would you like to roll? [d4, d6, d8, d10, d12, d20] ")
    rollMod = int(input("What would you like to add to the roll? "))
    while howMany != 0:
        rollRiggedDice(roll,whatDice)
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
    else:
        print("Defaulting to d20")
        rollTemp = random.randint(14,20)
    print(rollTemp," Rolled")
    roll.append(rollTemp)

def total(roll):
    rollTotal = sum(roll)
    print(rollTotal," is the current total")

def main():
    roll = []
    action = input("What do you want to do? ")
    if action == "roll":
        rollSpecs(roll)
    elif action == "rigged roll":
        rollSpecsRigged(roll)
    elif action == "clear":
        times = 25
        while times != 0:
            time.sleep(0.01)
            print("|")
            times -= 1
    else:
        print("That is not a valid action")
    main()

main()
