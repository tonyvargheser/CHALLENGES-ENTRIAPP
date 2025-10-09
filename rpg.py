import random
print("------------Wlcome to the RPG Game--------------------")
player = input("\n Enter your name    ").upper()
e = ['GOBLIN','ORC','SKELTON','GHOST']
enemy = random.choice(e)
print(f"\n Hai {player}. your enemy is{enemy}\n\n")
turn = 1
playerhp = 100
enemyhp = 100
p =['ATTACK','DEFEND','HEAL']


while playerhp >=0 and enemyhp >=0 :
    print("\n\n TURN",turn)
    playeraction = random.choice(p)
    enemyaction = random.choice(p)
    print(f"pleayer action is  {playeraction}  vs enemy action is {enemyaction}")


    if playeraction == 'ATTACK' and enemyaction == 'ATTACK':
        print("\n--------Both are attacking-------------")
        playerhp -= random.randint(10,35)
        enemyhp -= random.randint(10,30)
        print(f"\n{player}Health: ",playerhp)
        print(f"\n{enemy} Health:  ",enemyhp)

    elif playeraction == 'ATTACK' and enemyaction =='DEFEND':
        print(f"\n\n {player} is attacking and {enemy} is Defending")
        playerhp -= random.randint(10,35)
        enemyhp -= random.randint(10,30)//2
        print(f"\n{player}Health: ",playerhp)
        print(f"\n{enemy} Health:  ",enemyhp)

    elif playeraction == 'ATTACK' and enemyaction == 'HEAL':
        print(f"\n\n {player} is attacking and {enemy} is Healing")
        playerhp -= random.randint(10,35)
        print(f"\n{player}Health: ",playerhp)
        enemyheal =random.randint(10,25)
        if (enemyhp+enemyheal<100):
            enemyhp +=enemyheal
            print(f"\n{enemy} Health:  ",enemyhp)
        else:
            enemyhp =100
            print(f"\n{enemy} Health:  ",enemyhp)
    
    elif playeraction =='DEFEND' and enemyaction == 'ATTACK':
        print(f"\n\n{player} id defending and {enemy} is attacking")
        playerhp -= random.randint(10,35)//2
        enemyhp -= random.randint(10,30)
        print(f"\n{player}Health: ",playerhp)
        print(f"\n{enemy} Health:  ",enemyhp)

    elif playeraction == 'DEFEND' and enemyaction == 'DEFEND':
        print("\n--------Both are Defending-------------")
        # playerhp -= random.randint(10,35)//2
        # enemyhp -= random.randint(10,30)//2
        print(f"\n{player}Health: ",playerhp)
        print(f"\n{enemy} Health:  ",enemyhp)
        print(f"\n\n {player} and {enemy} Health is same ------waiting for ATTACK")

    elif playeraction =='DEFEND' and enemyaction == 'HEAL':
        print(f"\n\n{player} id defending and {enemy} is Healing")
        # playerhp -= random.randint(10,35)
        print(f"\n{player}Health: ",playerhp)
        # enemyheal =random.randint(10,25)
        # if (enemyhp+enemyheal<100):
        #     enemyhp +=enemyheal
        print(f"\n{enemy} Health:  ",enemyhp)
        # else:
        #     enemyhp =100
        #     print(f"\n{enemy} Health:  ",enemyhp)
        print(f"\n\n {player} and {enemy} Health is same ------waiting for ATTACK")


    elif playeraction == 'HEAL' and enemyaction == 'ATTACK':
        print(f"\n\n{player} is Healing and {enemy} is Attacking")
        playerheal = random.randint(10,25)
        if (playerhp+playerheal <100):
            playerhp += playerheal
            print(f"\n{player}Health: ",playerhp)
        else:
            playerhp = 100
            print(f"\n{player}Health: ",playerhp)
        enemyhp -= random.randint(10,30)
        print(f"\n{enemy} Health:  ",enemyhp)
    
    elif playeraction == 'HEAL' and enemyaction == 'DEFEND':
        print(f"\n\n{player} is Healing and {enemy} is Defending")
        # playerhp -= random.randint(10,35)//2
        # enemyhp -= random.randint(10,30)//2
        print(f"\n{player}Health: ",playerhp)
        print(f"\n{enemy} Health:  ",enemyhp)
        print(f"\n\n {player} and {enemy} Health is same ------waiting for ATTACK")

    elif playeraction == 'HEAL' and enemyaction == 'HEAL':
        print(f"\n\n{player} is Healing and {enemy} is Healing")
        # playerhp -= random.randint(10,35)//2
        # enemyhp -= random.randint(10,30)//2
        print(f"\n{player}Health: ",playerhp)
        print(f"\n{enemy} Health:  ",enemyhp)
        print(f"\n\n {player} and {enemy} Health is same ------waiting for ATTACK")

    turn +=1

if playerhp <= 0:
    print(f"\n\n GAME is over {enemy} is won!!!!!!!!!")
elif enemyhp<=0:
    print(f"\n\n GAME is over {player} is won!!!!!!!!!")












