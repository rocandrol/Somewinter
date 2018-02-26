from random import randint

#your stats
herohp = 30
herodamage = randint(5, 8)
herodefense = 3
looper = 1
isdefense = False

#monster's stats
monsterhp = 20
monsterdamage = randint(4, 6)

print("Your HP: {}".format(herohp))
print("Monster HP: {}".format(monsterhp))


status = True

for i in range(looper):
    while status == True:
        choice = input("Attack or defend?")
        herohp = herohp - monsterdamage
        if choice == "attack" or "Attack":
            monsterhp = monsterhp - herodamage
        if choice == "defend" or "Defend":
            monsterdamage = monsterdamage -3
        print("• You did {} damage!".format(herodamage))
        print("• The monster did {} damage!".format(monsterdamage))
        print("Your HP: {}".format(herohp))
        print("Monster HP: {}".format(monsterhp))
    
        looper = +1
        herodamage = randint(3,7)
        monsterdamage = randint(4, 6)
        if monsterhp <= 0:
            looper = 0
            print("Good work, you won!")
            break
        elif herohp <= 0:
            looper = 0
            print("Oh no! The monster won!")
            break
