#Functions for Somewinter

import classes
import inn

status = True

#variables for examination command
twooptions = ". Would you like to examine or leave?"
twooptionsstorage = twooptions
threeoptions = ". Would you like to examine, loot or leave?"

def p(words):
    print(words)
#Shortened version of print

#A command for when the character discovers a 
def discovery(subject):
    if subject == Combatant:
        return hp, speedstat

    if subject == Item:
        return name

#A command to let you examine, leave or loot a room
def examineorleave(current, after):
        global twooptions
        roomchoice = input("• You are in the " + inn.currentroom + twooptions)
        if roomchoice == "Examine" or "examine":
            p(current.description)
            if current.lootable == True:
                global threeoptions
                global twooptionsstorage
                twooptions = threeoptions
        
        elif roomchoice == "Leave" or "leave":
            p(after.description)
            break
        
        elif roomchoice == "Loot" or "loot" and current.lootable == True:
            p("You found " + current.loot.name)
            inn.inventory.append(current.loot)
            twooptions = twooptionsstorage
            current.lootable = False