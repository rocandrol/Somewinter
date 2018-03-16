'''
This is the file containing all functions for Somewinter.
Author: Emma Graves
Date: 2/16/18 - x
'''

import classes
from random import randint

#variables for examination command
examined = False

def p(words):
    """
This function's purpose is to shorten the task of writing print.
:param words: These are the words that will be printed, Str()
    """
    print(words)

def handleinput(inp, invlist):
    if inp == "inv" or inp == "backpack" or inp == "bp":
        print(invlist)
    return inp

def examineorleave(current, twooptions, threeoptions, twooptionsstorage, inventory):
    """
    This function lets the character examine, loot, or leave a room.
    :param current: The room the character is currently in, Room()
    :param roomchoice: The input that will determine if your character examines, loots or leaves the room, Str()
    :param twooptions: A variable containing a string with two options, Str()
    :param threeoptions: A variable containing a string with three options, Str()
    :param twooptionsstorage: A variable to retain the initial string value of twooptions, Str()
    :param inventory: The list containing the player's inventory, List()
    """
    looper = 1
    for i in range (looper):
        while True:
            roomchoice = handleinput(input("You are in the " + str(current) + twooptions), inventory)
            if roomchoice.lower() == "examine" or roomchoice.lower() == "e":
                p(current.description)
                if current.lootable == True:
                    twooptions = threeoptions
                    examined = True
                
            elif roomchoice.lower() == "leave" or roomchoice.lower() == "l":
                p("You have left the " + str(current) + ".")
                looper = 0
                break
                
            elif roomchoice.lower() == "loot" or roomchoice.lower() == "l" and current.lootable == True and examined == True:
                p("You found " + current.loot.name + ".")
                inventory.append(current.loot)
                twooptions = twooptionsstorage
                current.lootable = False
            looper = +1

def combat(herohp, hdrad1, hdrad2, mdrad1, mdrad2, monsterhp, moname, outcome):
    yoinks = 1
    monsterdamage = randint(mdrad1, mdrad2)
    herodamage = randint(hdrad1, hdrad2)
    print("You've entered combat with a", moname + "!" )
    print("Your HP: {}".format(herohp))
    print("Monster HP: {}".format(monsterhp))
    for k in range(yoinks):
        while True:
            choice = input("Attack or defend? ")
            herohp = herohp - monsterdamage
            if choice.lower() == "attack" or choice.lower() == "a":
                monsterhp = monsterhp - herodamage
                print("- You did {} damage!".format(herodamage))
            elif choice.lower() == "defend" or choice.lower() == "d":
                monsterdamage = monsterdamage -3
            print("- The monster did {} damage!".format(monsterdamage))
            print("Your HP: {}".format(herohp))
            print("Monster HP: {}".format(monsterhp))
        
            yoinks = +1
            herodamage = randint(hdrad1,hdrad2)
            monsterdamage = randint(mdrad1, mdrad2)
            if herohp <= 0 and monsterhp <= 0:
                yoinks = 0
                print("You and the", moname, "were both knocked out.")
                print("You awaken hours later, your health lowered. The", moname, "is nowhere to be seen.")
                outcome = False
                break
            elif monsterhp <= 0:
                yoinks = 0
                print("You've knocked out the", moname +".")
                outcome = True
                break
            elif herohp <= 0:
                yoinks = 0
                print("The", moname, "has knocked you out.")
                print("You awaken hours later with your health lowered.")
                outcome = False
                break