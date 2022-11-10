#loot table randomizer for chests, and enemies
import time
import random

#lets assign some loot
common = ['Bone(s)','Leather Scrap(s)','Poor Quality Cloth(s)','Cobweb(s)','Copper Coin(s)','Old Food Scrap(s)','Pile(s) of Dust','Twig(s)','Bundle(s) of String','Arrow(s)','Slime']
uncommon = ['Silver Coin(s)','Bottle(s) of Oil','ft of rope','Bag(s) of Sand','Torch(es)','Anti-toxin(s)','Small Healing Potion(s)']
rare = ['Rusty Knife(s)','Old Cap(s)','Rusty Chainmail Shirt(s)','Rusty Chain Leggings','Old Leather Boots','Fire Arrow(s)','Crowbar(s)']
superRare = ['Golden Coin(s)','Good Leather','Firestarter(s)','Canteen(s)','Oil Lantern(s)','Healing Potion(s)','Molatov(s)','Bottle(s) of Mana']
ultraRare = ['copper sword','copper helmet','copper chestplate','copper leggings','good bow','quarterstaff','wand','magic staff','mase','low quiality gem']
legendary = ['platinum coin','ruby','sapphire','diamond','emerald','enchanted sword','opal','obsidian sphere','golden sheild','plated helmet','plate mail chestplate','plate mail leggings','plate mail boots','good iron sword']
mythical = ['magic tome','ring of wishes','staff of healing','ring of free action','ring of +1 bonus action','ring of loot','greater healing potion','sword of power','necrotic arrow quiver','bottle of poison','pan\'s cheese','flamethrower','cap of invisability','wine of dionysus']
#here is the types of chest in list form
cType = ['Common','Uncommon','Rare','Super Rare','Ultra Rare','Legendary','Mythical']
enemies = ['humaniod','undead','undead humanoid','dwarf','elf','imp','fay']
prefix = 'null'

def randomizeChestLevel():
    chestLevel = random.randint(1,40)
    if(chestLevel==1)|(chestLevel==2)|(chestLevel==3)|(chestLevel==4)|(chestLevel==5)|(chestLevel==6)|(chestLevel==7)|(chestLevel==8):
        chestType = random.randint(1,3)
        randomizeChestLoot(chestType)
    elif(chestLevel==9)|(chestLevel==10)|(chestLevel==11)|(chestLevel==12)|(chestLevel==13)|(chestLevel==14):
        chestType = random.randint(2,4)
        randomizeChestLoot(chestType)
    elif(chestLevel==15)|(chestLevel==16)|(chestLevel==17):
        chestType = random.randint(3,5)
        randomizeChestLoot(chestType)
    elif(chestLevel==20):
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
    print('Genorating loot....')
    time.sleep(0.5)
    print('...')
    time.sleep(0.5)
    if(chestType == 1):
        count = random.randint(1,5)
        while (count < 10):   
            count = count + 1
            time.sleep(0.25)
            prefix = random.randint(1,10)
            print("You gained",prefix,common[random.randint(1,len(common)-1)])
    elif(chestType == 2):
        count = random.randint(2,6)
        while (count < 10):   
            count = count + 1
            time.sleep(0.25)
            prefix = random.randint(1,6)
            print("You gained",prefix,uncommon[random.randint(1,len(uncommon)-1)])
    elif(chestType == 3):
        count = random.randint(3,7)
        while (count < 10):   
            count = count + 1
            time.sleep(0.25)
            prefix = random.randint(1,2)
            print("You gained",prefix,rare[random.randint(1,len(rare)-1)])
    elif(chestType == 4):
        count = random.randint(6,8)
        while (count < 10):   
            count = count + 1
            time.sleep(0.25)
            prefix = 1
            print("You gained",prefix,superRare[random.randint(1,len(superRare)-1)])
    elif(chestType == 5):
        count = random.randint(7,9)
        while (count < 10):   
            count = count + 1
            time.sleep(0.25)
            prefix = 1
            print("You gained",prefix,ultraRare[random.randint(1,len(ultraRare)-1)])
    elif(chestType == 6):
        count = 9
        while (count < 10):   
            count = count + 1
            time.sleep(0.25)
            prefix = 1
            print("You gained",prefix,legendary[random.randint(1,len(legendary)-1)])
    elif(chestType == 7):
        count = 9
        while (count < 10):   
            count = count + 1
            time.sleep(0.25)
            prefix = 1
            print("You gained",prefix,mythical[random.randint(1,len(mythical)-1)])
    else:
        print('This shoudn\'t happen...')
        getLoot(chestType)
    
def convStr(chestsOpened): 
    count = 0
    while (count < chestsOpened):   
        count = count + 1
        time.sleep(0.5)
        print('|')
        print('|')
        randomizeChestLevel()
    startFunction()
    
def startFunction():
    chestsOpened = int(input('How many chests would you like to open? '))
    print('Opening',chestsOpened,'chests!')
    convStr(chestsOpened)

startFunction()
