from random import randint

print("Welcome to the combat system! (If you don't attack or defend you'll forfeit a turn!)")

#your stats
herohp = 30
herodamage = randint(5, 8)
herodefense = 3
looper = 1
isdefense = False
status = True

#monster's stats
monsterhp = 20
monsterdamage = randint(4, 6)

print("Your HP: {}".format(herohp))
print("Monster HP: {}".format(monsterhp))


for i in range(looper):
    while status == True:
        choice = input("Attack or defend?")
        herohp = herohp - monsterdamage
        if choice.lower() == "attack":
            monsterhp = monsterhp - herodamage
            print("• You did {} damage!".format(herodamage))
        elif choice.lower() == "defend":
            monsterdamage = monsterdamage -3
        print("• The monster did {} damage!".format(monsterdamage))
        print("Your HP: {}".format(herohp))
        print("Monster HP: {}".format(monsterhp))
    
        looper = +1
        herodamage = randint(3,7)
        monsterdamage = randint(4, 6)
        if herohp <= 0 and monsterhp <= 0:
            looper = 0
            print("Oh no! You both got knocked out!")
            break
        elif monsterhp <= 0:
            looper = 0
            print("Good work, you won!")
            break
        elif herohp <= 0:
            looper = 0
            print("Oh no! The monster won!")
            break
