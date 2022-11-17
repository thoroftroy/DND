#loot table randomizer for chests, and enemies
import time
import random

#lets assign some loot
common = ['Bone(s)','Leather Scrap(s)','Poor Quality Cloth(s)','Cobweb(s)','Copper Coin(s)','Old Food Scrap(s)','Pile(s) of Dust','Twig(s)','Bundle(s) of String','Arrow(s)','Slime','Pebbles','Rotting Meat Sack(s)','Rotten Wood Chunk(s)','Beatle Carcas(es)','Rope Scrap(s)','Rotten Bannana(s)','Cracked Glass Bottle(s)','Old Broken Key(s)','Ripped Bag(s)','Moldy Bread Chunk(s)','Old Silver Spoon(s)','Screw(s)','Rusty Nail(s)']
uncommon = ['Silver Coin(s)','Bottle(s) of Oil','ft of rope','Bag(s) of Sand','Torch(es)','Anti-toxin(s)','Small Healing Potion(s)','Small Magnet(s)','Empty Glass Bottle(s)','Small Sack(s)']
rare = ['Rusty Knife(s)','Old Cap(s)','Rusty Chainmail Shirt(s)','Rusty Chain Leggings','Old Leather Boots','Fire Arrow(s)','Crowbar(s)','Marble(s)']
superRare = ['Golden Coin(s)','Good Leather','Firestarter(s)','Canteen(s)','Oil Lantern(s)','Healing Potion(s)','Molatov(s)','Bottle(s) of Mana','Chicken Nugget(s)','Large Magnet(s)','Jar(s) of Pickels']
ultraRare = ['Copper sword(s)','Copper Helmet(s)','Copper Chestplate(s)','Copper Leggings(s)','Good Bow(s)','Quarterstaff(s)','Wand(s)','Magic Staff(s)','Mase(s)','Low Quiality Gem(s)']
legendary = ['Platinum Coin','Ruby','Sapphire','Diamond','Emerald','Enchanted Sword','Opal','Obsidian Sphere','Golden Sheild','Plated Helmet','Plate Mail Chestplate','Plate Mail Leggings','Plate Mail Boots','Good Iron Sword','Multitool']
mythical = ['Magic Tome','Ring of Wishes','Staff of Healing','Ring of Free Action','Ring of +1 Bonus Action','Ring of Loot','Greater Healing Potion','Sword of Power','Necrotic Arrow Quiver','Bottle of Poison','Pan\'s Cheese','Flamethrower','Cap of Invisability','Wine of Dionysus']
#here is the types of chest in list form
cType = ['Common','Uncommon','Rare','Super Rare','Ultra Rare','Legendary','Mythical']
enemies = ['humaniod','undead','undead humanoid','dwarf','elf','imp','fay']
prefix = 'null'

def randomizeChestLevel():
    chestLevel = random.randint(1,85)
    if(chestLevel==1)|(chestLevel==2)|(chestLevel==3)|(chestLevel==4)|(chestLevel==5)|(chestLevel==6)|(chestLevel==7)|(chestLevel==8):
        chestType = random.randint(2,3)
        randomizeChestLoot(chestType)
    elif(chestLevel==9)|(chestLevel==10)|(chestLevel==11)|(chestLevel==12)|(chestLevel==13)|(chestLevel==14)|(chestLevel==14)|(chestLevel==18)|(chestLevel==19)|(chestLevel==20)|(chestLevel==21)|(chestLevel==22):
        chestType = random.randint(2,4)
        randomizeChestLoot(chestType)
    elif(chestLevel==40)|(chestLevel==41)|(chestLevel==42):
        chestType = random.randint(3,5)
        randomizeChestLoot(chestType)
    elif(chestLevel==80):
        chestType = random.randint(5,7)
        randomizeChestLoot(chestType)
    else:
        chestType = 1
        randomizeChestLoot(chestType)
        
def randomizeChestLoot(chestType):
    loot = 'null'
    print(cType[chestType-1],'Chest Found!')
    getLoot(chestType,loot)

def getLoot(chestType,loot):
    print('Generating loot....')
    time.sleep(0.25)
    print('...')
    time.sleep(0.25)
    if(chestType == 1):
        count = random.randint(1,5)
        while (count < 10):   
            count = count + 1
            time.sleep(0.005)
            prefix = random.randint(1,10)
            print("You gained",prefix,common[random.randint(1,len(common)-1)])
    elif(chestType == 2):
        count = random.randint(2,6)
        while (count < 10):   
            count = count + 1
            time.sleep(0.005)
            prefix = random.randint(1,4)
            print("You gained",prefix,uncommon[random.randint(1,len(uncommon)-1)])
    elif(chestType == 3):
        count = random.randint(3,7)
        while (count < 10):   
            count = count + 1
            time.sleep(0.005)
            prefix = random.randint(1,2)
            print("You gained",prefix,rare[random.randint(1,len(rare)-1)])
    elif(chestType == 4):
        count = random.randint(6,8)
        while (count < 10):   
            count = count + 1
            time.sleep(0.005)
            prefix = 1
            print("You gained",prefix,superRare[random.randint(1,len(superRare)-1)])
    elif(chestType == 5):
        count = random.randint(7,9)
        while (count < 10):   
            count = count + 1
            time.sleep(0.005)
            prefix = 1
            print("You gained",prefix,ultraRare[random.randint(1,len(ultraRare)-1)])
    elif(chestType == 6):
        count = 9
        while (count < 10):   
            count = count + 1
            time.sleep(0.005)
            prefix = 1
            print("You gained",prefix,legendary[random.randint(1,len(legendary)-1)])
    elif(chestType == 7):
        count = 9
        while (count < 10):   
            count = count + 1
            time.sleep(0.005)
            prefix = 1
            print("You gained",prefix,mythical[random.randint(1,len(mythical)-1)])
    else:
        print('This shoudn\'t happen...')
        getLoot(chestType)
    
def convStr(chestsOpened): 
    count = 0
    while (count < chestsOpened):   
        count = count + 1
        time.sleep(0.01)
        print('|')
        print('|')
        randomizeChestLevel()
    startFunction()
    
def startFunction():
    print('|')
    print('|')
    print('ONLY TYPE NUMBERS (ex: 2, 53, 1439805183 [no decimals])')
    chestsOpened = input('How many chests would you like to open? ')
    if chestsOpened.isdigit() == True:
        chestsOpened = int(chestsOpened)
        print('Opening',chestsOpened,'chests!')
        convStr(chestsOpened)
    elif chestsOpened.isdigit() == False:
        if(chestsOpened == 'exit') | (chestsOpened == 'Exit'):
            exit
        elif(chestsOpened == 'common') | (chestsOpened == 'Common'):
            print('You cheeter')
            chestType = 1
            randomizeChestLoot(chestType)
            startFunction()
        elif(chestsOpened == 'uncommon') | (chestsOpened == 'Uncommon'):
            print('You cheeter')
            chestType = 2
            randomizeChestLoot(chestType)
            startFunction()
        elif(chestsOpened == 'rare') | (chestsOpened == 'Rare'):
            print('You cheeter')
            chestType = 3
            randomizeChestLoot(chestType)
            startFunction()
        elif(chestsOpened == 'super rare') | (chestsOpened == 'Super Rare'):
            print('You cheeter')
            chestType = 4
            randomizeChestLoot(chestType)
            startFunction()
        elif(chestsOpened == 'ultra rare') | (chestsOpened == 'Ultra Rare'):
            print('You cheeter')
            chestType = 5
            randomizeChestLoot(chestType)
            startFunction()
        elif(chestsOpened == 'legendary') | (chestsOpened == 'Legendary'):
            print('You cheeter')
            chestType = 6
            randomizeChestLoot(chestType)
            startFunction()
        elif(chestsOpened == 'Mythical') | (chestsOpened == 'mythical'):
            print('You cheeter')
            chestType = 7
            randomizeChestLoot(chestType)
            startFunction()
        else:
            print('|')
            print(chestsOpened,"IS NOT A VALID NUMBER!!!!")
            startFunction()
    else:
        print('|')
        print(chestsOpened,"IS NOT A VALID NUMBER!!!!")
        startFunction()
    

startFunction()
