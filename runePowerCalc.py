#This is used to calculate the affinity of someone when casting a rune spell
import random
import time

#runes
runeList = ["Fire","Neon","Phosphorus","Sulfur","Lightning","Radiant","Heat",
            "Water","Cobalt","Gallium","Arsenic","Mercury","Neptunium","Acidic","Cold",
            "Earth","Gold","Silicon","Titanium","Iron","Silver","Tungsten","Osmium","Platinum",
            "Air","Oxygen","Helium","Uranium","Necrotic","Pressure",
            "Carbon","Link","Detect","Time","Kinetic","Gravity","Creation","Destruction","Renewal","Decay","Up","Left","Right","Down","All (Dir)"]
craftAffList = ["Generic","Dirt","Wood","Stone","Metal","Gem","Skin"]
typeCraftAffList = ["Draw","Paint","Carve","Tattoo"]
fireAffList = ["Fire","Neon","Phosphorus","Sulfur","Lightning","Radiant","Heat"]
waterAffList = ["Water","Cobalt","Gallium","Arsenic","Mercury","Neptunium","Acidic","Cold"]
earthAffList = ["Earth","Gold","Silicon","Titanium","Iron","Silver","Tungsten","Osmium","Platinum"]
airAffList = ["Air","Oxygen","Helium","Uranium","Necrotic","Pressure"]
utilAffList = ["Carbon","Link","Detect","Up","Left","Right","Down","All (Dir)"]
physAffList = ["Time","Kinetic","Gravity"]
createAffList = ["Creation","Destruction","Renewal","Decay"]

#player/npc affinity
savedNpcList = ["Alex","Master","Apprentice","Daggan","Random Master","Random Basic"]
affinityTypes = ["Crafting","Fire","Earth","Water","Air","Utility","Physical","Creation","Generic"]
alexAffinityTypes = [-10,   -10,    -10,    -10,    -10,    -10,    -10,        -10,        0]
masterAffinityTypes = [6,     2,      2,      2,      2,      2,      1,          0,        0]
apprenticeAffinityTypes = [3, 0,      0,      0,      0,      0,     -5,         -7,        0]
dagganAffinityTypes = [5,     8,      4,     -3,      5,      2,      1,         10,        0]

def showPowerScale(percentage):
    if percentage == 0:
        print("Wow that was pathetic, the runes barley activated")
    elif 1 <= percentage <= 10:
        print("Strikes with the force of a hammer")
    elif 11 <= percentage <= 20:
        print("Around the strength of a solid sledge hammer swing")
    elif 21 <= percentage <= 30:
        print("The strength of a grenade")
    elif 31 <= percentage <= 40:
        print("Roughly as strong as a stick of tnt")
    elif 51 <= percentage <= 60:
        print("Around the strength of a small nuke")
    elif 61 <= percentage <= 70:
        print("The strength of a large nuke")
    elif 71 <= percentage <= 80:
        print("The force of a large astroid")
    elif 81 <= percentage <= 90:
        print("As if the moon itself hit the earth")
    elif 91 <= percentage <= 100:
        print("The planet's destruction is ensured")
    elif percentage > 100:
        print("The universe itself has imploded")
    else:
        print("How the heck did we get here?")
        
def calcRunePowerAuto(runesInSpell):
    #choose who you are automating for
    #randomize the random npcs
    randomizedMasterAffinityTypes = [random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,8),random.randint(0,10),random.randint(0,8),random.randint(0,5)]
    randomizedBasicAffinityTypes = [random.randint(-10,5),random.randint(-10,5),random.randint(-10,5),random.randint(-10,5),random.randint(-10,5),random.randint(-10,5),random.randint(-10,5),random.randint(-10,5),random.randint(0,2)]
    print("Please select an NPC or player from the following list, type their entire name as seen in the list with capitalization.")
    print(savedNpcList)
    choose = input()
    if choose in savedNpcList:
        print('Great! Calculating for',choose)
        i = 0
        sumOfAffinities = 0
        for x in range(len(runesInSpell)):
            time.sleep(0.5)
            if runesInSpell[i] in craftAffList:
                print(runesInSpell[i],"was found in craft list!") #This is kind of an awful way of doing this and its a ton of work to add in a new npc but it will work for now
                if "Alex" == choose:
                    sumOfAffinities += alexAffinityTypes[0]
                elif "Master" == choose:
                    sumOfAffinities += masterAffinityTypes[0]
                elif "Apprentice" == choose:
                    sumOfAffinities += apprenticeAffinityTypes[0]
                elif "Daggan" == choose:
                    sumOfAffinities += dagganAffinityTypes[0]
                elif "Random Master" == choose:
                    sumOfAffinities += randomizedMasterAffinityTypes[0]
                elif "Random Basic" == choose:
                    sumOfAffinities += randomizedBasicAffinityTypes[0]
                else:
                    print("Something went very wrong, aborting...")
                    time.sleep(0.5)
                    main()
            elif runesInSpell[i] in fireAffList:
                print(runesInSpell[i],"was found in fire list!")
                if "Alex" == choose:
                    sumOfAffinities += alexAffinityTypes[1]
                elif "Master" == choose:
                    sumOfAffinities += masterAffinityTypes[1]
                elif "Apprentice" == choose:
                    sumOfAffinities += apprenticeAffinityTypes[1]
                elif "Daggan" == choose:
                    sumOfAffinities += dagganAffinityTypes[1]
                elif "Random Master" == choose:
                    sumOfAffinities += randomizedMasterAffinityTypes[1]
                elif "Random Basic" == choose:
                    sumOfAffinities += randomizedBasicAffinityTypes[1]
                else:
                    print("Something went very wrong, aborting...")
                    time.sleep(0.5)
                    main()
            elif runesInSpell[i] in waterAffList:
                print(runesInSpell[i],"was found in water list!")
                if "Alex" == choose:
                    sumOfAffinities += alexAffinityTypes[2]
                elif "Master" == choose:
                    sumOfAffinities += masterAffinityTypes[2]
                elif "Apprentice" == choose:
                    sumOfAffinities += apprenticeAffinityTypes[2]
                elif "Daggan" == choose:
                    sumOfAffinities += dagganAffinityTypes[2]
                elif "Random Master" == choose:
                    sumOfAffinities += randomizedMasterAffinityTypes[2]
                elif "Random Basic" == choose:
                    sumOfAffinities += randomizedBasicAffinityTypes[2]
                else:
                    print("Something went very wrong, aborting...")
                    time.sleep(0.5)
                    main()
            elif runesInSpell[i] in earthAffList:
                print(runesInSpell[i],"was found in earth list!")
                if "Alex" == choose:
                    sumOfAffinities += alexAffinityTypes[3]
                elif "Master" == choose:
                    sumOfAffinities += masterAffinityTypes[3]
                elif "Apprentice" == choose:
                    sumOfAffinities += apprenticeAffinityTypes[3]
                elif "Daggan" == choose:
                    sumOfAffinities += dagganAffinityTypes[3]
                elif "Random Master" == choose:
                    sumOfAffinities += randomizedMasterAffinityTypes[3]
                elif "Random Basic" == choose:
                    sumOfAffinities += randomizedBasicAffinityTypes[3]
                else:
                    print("Something went very wrong, aborting...")
                    time.sleep(0.5)
                    main()
            elif runesInSpell[i] in airAffList:
                print(runesInSpell[i],"was found in air list!")
                if "Alex" == choose:
                    sumOfAffinities += alexAffinityTypes[4]
                elif "Master" == choose:
                    sumOfAffinities += masterAffinityTypes[4]
                elif "Apprentice" == choose:
                    sumOfAffinities += apprenticeAffinityTypes[4]
                elif "Daggan" == choose:
                    sumOfAffinities += dagganAffinityTypes[4]
                elif "Random Master" == choose:
                    sumOfAffinities += randomizedMasterAffinityTypes[4]
                elif "Random Basic" == choose:
                    sumOfAffinities += randomizedBasicAffinityTypes[4]
                else:
                    print("Something went very wrong, aborting...")
                    time.sleep(0.5)
                    main()
            elif runesInSpell[i] in utilAffList:
                print(runesInSpell[i],"was found in utility list!")
                if "Alex" == choose:
                    sumOfAffinities += alexAffinityTypes[5]
                elif "Master" == choose:
                    sumOfAffinities += masterAffinityTypes[5]
                elif "Apprentice" == choose:
                    sumOfAffinities += apprenticeAffinityTypes[5]
                elif "Daggan" == choose:
                    sumOfAffinities += dagganAffinityTypes[5]
                elif "Random Master" == choose:
                    sumOfAffinities += randomizedMasterAffinityTypes[5]
                elif "Random Basic" == choose:
                    sumOfAffinities += randomizedBasicAffinityTypes[5]
                else:
                    print("Something went very wrong, aborting...")
                    time.sleep(0.5)
                    main()
            elif runesInSpell[i] in physAffList:
                print(runesInSpell[i],"was found in physical list!")
                if "Alex" == choose:
                    sumOfAffinities += alexAffinityTypes[6]
                elif "Master" == choose:
                    sumOfAffinities += masterAffinityTypes[6]
                elif "Apprentice" == choose:
                    sumOfAffinities += apprenticeAffinityTypes[6]
                elif "Daggan" == choose:
                    sumOfAffinities += dagganAffinityTypes[6]
                elif "Random Master" == choose:
                    sumOfAffinities += randomizedMasterAffinityTypes[6]
                elif "Random Basic" == choose:
                    sumOfAffinities += randomizedBasicAffinityTypes[6]
                else:
                    print("Something went very wrong, aborting...")
                    time.sleep(0.5)
                    main()
            elif runesInSpell[i] in createAffList:
                print(runesInSpell[i],"was found in creation list!")
                if "Alex" == choose:
                    sumOfAffinities += alexAffinityTypes[7]
                elif "Master" == choose:
                    sumOfAffinities += masterAffinityTypes[7]
                elif "Apprentice" == choose:
                    sumOfAffinities += apprenticeAffinityTypes[7]
                elif "Daggan" == choose:
                    sumOfAffinities += dagganAffinityTypes[7]
                elif "Random Master" == choose:
                    sumOfAffinities += randomizedMasterAffinityTypes[7]
                elif "Random Basic" == choose:
                    sumOfAffinities += randomizedBasicAffinityTypes[7]
                else:
                    print("Something went very wrong, aborting...")
                    time.sleep(0.5)
                    main()
            else:
                print(runesInSpell[i],"was not found in any list!")
                print("Exiting...")
                time.sleep(0.5)
                main()
            i += 1
        #now we add the generic modifier
        if "Alex" == choose:
            sumOfAffinities += alexAffinityTypes[8]
            print("Adding generic modifier of:",alexAffinityTypes[8])
        elif "Master" == choose:
            sumOfAffinities += masterAffinityTypes[8]
            print("Adding generic modifier of:",masterAffinityTypes[8])
        elif "Apprentice" == choose:
            sumOfAffinities += apprenticeAffinityTypes[8]
            print("Adding generic modifier of:",apprenticeAffinityTypes[8])
        elif "Daggan" == choose:
            sumOfAffinities += dagganAffinityTypes[8]
            print("Adding generic modifier of:",dagganAffinityTypes[8])
        elif "Random Master" == choose:
            sumOfAffinities += randomizedMasterAffinityTypes[8]
            print("Adding generic modifier of:",randomizedMasterAffinityTypes[8])
        elif "Random Basic" == choose:
            sumOfAffinities += randomizedBasicAffinityTypes[8]
            print("Adding generic modifier of:",randomizedBasicAffinityTypes[8])
        else:
                    print("Something went very wrong, aborting...")
                    time.sleep(0.5)
                    main()
        #next we roll a dice
        devider = random.randint(1,20)
        devider = devider
        print("Roll:", devider)
        #Set the weight value
        #Get what type of material the symbols are drawn on
        print(craftAffList)
        print("What is the material used for the crafting? (please input the numerical value)")
        material = input()
        if material.isnumeric() == True:
            material = int(material)+1
        else:
            print("Non valid input, defaulting to 1")
            material = 1
        #get how the symbols are drawn
        print(typeCraftAffList)
        print("How are the symbols drawn?")
        drawnMethod = input()
        if drawnMethod.isnumeric() == True:
            drawnMethod = int(material)+1
        else:
            print("Non valid input, defaulting to 1")
            drawnMethod = 1
        weight = material * drawnMethod
        #now we actually calculate it
        totalSpellPower = int((len(runesInSpell) + (sumOfAffinities + weight)) + devider)
        if totalSpellPower <= 0:
            totalSpellPower = 0
        max = 300
        percentage =  100 * float(totalSpellPower)/float(max)
        print("Your spell has a power of",totalSpellPower)
        percentage = round(percentage,1)
        print("You have achieved",percentage,"% of maximum power")
        print("(That is based on 300 being the maximum achievable number, with 20 runes as the soft cap)")
        showPowerScale(percentage)
    elif choose not in savedNpcList:
        print(choose,' is not present in the list')
        calcRunePowerAuto(runesInSpell)

def calcRunePower(runesInSpell):
    #get what affinities the user has 
    affinityList = []
    print(runesInSpell)
    print("Affinities go between -10 and 10, they all start at -10")
    print("If your affinity is -10 then type 'y' to isNeg and then 10 to the affinity number")
    i = 0
    for x in range(len(runesInSpell)):
        print("Is your affinity negative? (y/n) ")
        isNeg = input()
        if isNeg == "y":
            isNeg = -1
        else:
            isNeg = 1
        print("What is your affinity with:",runesInSpell[i])
        i += 1
        affinity = input()
        if affinity.isnumeric() == True:
            affinity == int(affinity)
        else:
            print("Non valid input, defaulting to 1")
            affinity = 1
        affinity * isNeg #this makes it negative if the user wanted it to be
        affinityList.append(int(affinity))
    #Get what type of material the symbols are drawn on
    print(craftAffList)
    print("What is the material used for the crafting? (please input the numerical value)")
    material = input()
    if material.isnumeric() == True:
        material = int(material)+1
    else:
        print("Non valid input, defaulting to 1")
        material = 1
    #get how the symbols are drawn
    print(typeCraftAffList)
    print("How are the symbols drawn?")
    drawnMethod = input()
    if drawnMethod.isnumeric() == True:
        drawnMethod = int(material)+1
    else:
        print("Non valid input, defaulting to 1")
        drawnMethod = 1
    #next we roll a dice
    devider = random.randint(1,20)
    devider = devider
    print("Roll:", devider)
    #Set the weight value
    weight = material * drawnMethod
    #now we actually calculate it
    totalSpellPower = int(( len(runesInSpell) + ( (sum(affinityList)) + weight) ) + devider)
    if totalSpellPower <= 0:
        totalSpellPower = 0
    max = 300
    percentage =  100 * float(totalSpellPower)/float(max)
    print("Your spell has a power of",totalSpellPower)
    percentage = round(percentage,1)
    print("You have achieved",percentage,"% of maximum power")
    print("(That is based on 300 being the maximum achievable number, with 20 runes as the soft cap)")
    showPowerScale(percentage)

def calc():
    runesInSpell = []
    indexRune = 1
    howMany = input("How many non carbon runes are in the recipe? ")
    if(howMany.isnumeric() == True):
        howMany = int(howMany)
    else:
        print("Please type a valid number [nonnegative integers]")
        calc()
    print(runeList)
    for x in range(howMany):
        time.sleep(0.2)
        print("Please select a rune from the list, make sure to capitalize")
        print("What is the [",indexRune, "] rune? ")
        rune = input()
        indexRune += 1
        runesInSpell.append(rune)
    for x in range(5):
        print("|")
    time.sleep(0.3)
    print("Your spell is:")
    time.sleep(0.1)
    print(runesInSpell)
    print("|")
    correct = input("Is this correct? (y/n) ")
    if correct == "y":
        print('Perfect! Moving on then...')
        print("Do you want to automate the roll for a player/npc? (y/n) ")
        want = input()
        if want == "y":
            calcRunePowerAuto(runesInSpell)
        else:
            print("Alrighty into manual we go...")
            calcRunePower(runesInSpell)
    elif correct == "n":
        print("Starting over...")
        time.sleep(0.5)
        calc()
    else:
        print("Invalid Answer, restarting process...")
        time.sleep(0.5)
        calc()

def failChance():
    print("How many total runes are in the circle (including carbon)")
    runeNum = input()
    if runeNum.isnumeric() == True:
        runeNum = int(runeNum)
    else:
        print("Invalid input, please input non decimal, non negative int")
        failChance()
    failChanceList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    if runeNum >= len(failChanceList):
        runeNum == 40
    failChancePercentage = failChanceList[runeNum]
    randomChance = random.randint(1,100)
    if randomChance >= failChancePercentage:
        print("Your runes succeeded")
    else:
        print("Your runes failed")

def main():
    print("What do you want to do? [type 'list' to list valid actions]")
    what = input()
    if what == "list" or what == "List":
        print("List, Calc Affinity, Clear, Fail")
    elif what == "clear" or what == "Clear":
        for x in range(20):
            print("|")
    elif what == "Calc Affinity" or what == "calc affinity" or what == "calc":
        calc()
    elif what == "fail" or what == "Fail":
        failChance()
    else:
        print("Please input a valid action [type 'list' to list valid actions]")
    print("|")
    main()
main()
