'''
This is the file containing all functions for Somewinter.
Author: Emma Graves
Date: 2/16/18 - x
'''

import classes

#variables for examination command
examined = False

def p(words):
    """
This function's purpose is to shorten the task of writing print.
:param words: These are the words that will be printed, Str()
    """
    print(words)

def handleinput(inp):
    if inp == "inv" or inp == "backpack" or inp == "bp":
        print("inventory yayaya")
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
            roomchoice = handleinput(input("You are in the " + str(current) + twooptions))
            if roomchoice.lower() == "examine":
                p(current.description)
                if current.lootable == True:
                    twooptions = threeoptions
                    examined = True
                
            elif roomchoice.lower() == "leave":
                p("You have left the " + str(current) + ".")
                looper = 0
                break
                
            elif roomchoice.lower() == "loot" and current.lootable == True and examined == True:
                p("You found " + current.loot.name + ".")
                inventory.append(current.loot)
                twooptions = twooptionsstorage
                current.lootable = False
            looper = +1

def inventory(inp, inventory):
    """
    This function will be used to view your inventory.
    :param inp: Stands for input, meaning if the input equals any of the following strings then it will print inventory, Str()
    :param inventory: This parameter represents the list that contains all items in your inventory, List()
    """
    inp = inp.lower()
    if inp == "backpack" or inp == "bp" or inp == "inventory":
        print(inventory)