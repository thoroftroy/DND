import time
import random
#a simple combat simulator for groups of enemies
enemyIdList = ['Darkmantle','Goul','Enhanced Ghoul','Sprite','Sprite Leader','Sprite Warrior','Bugbear','Bugbear Cub','Bugbear Giant','Bugbear Leader','Zombie','Wraith','Troll','Shadow Fay','Mimic','Ghost','Cultist','Cult Leader','Cult Prophet','Cult Fanatic']
enemyHealth = ['23','20','40','10','30','40','60','20','80','70','30','140','60','120','40','10','15','130','170','40']
enemyAC = ['11','14','16','17','18','15','10','5','14','16','14','19','10','14','13','4','10','16','17','15']



def chooseEnemy():
    print(enemyIdList,' are the possible monsters. ')
    choose = input('Type the name or the numerical id to select a monester (ex: Darkmantle or 0, Goul or 1 ')
    if(choose.isnumeric()):
        choose = int(choose)
        mon = enemyIdList[choose]
        enemyId = int(mon)
    else:
        choose = str(choose)
        mon = choose
        enemyId = int(mon)

    print(mon,' choosen!')
    print('Stats: ',enemyHealth[enemyId])
    
    
    
def playerAttack():
    print('|')


chooseEnemy()
