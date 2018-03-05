'''
This is act 1 (INN) of an adventure game and a project for my class 3D printing and computer engineering.
It holds the working title of Somewinter. It entails a stranded human, alone with a radio.
Author: Emma L. Graves
Date: 2/16/18 - x
'''


#imports
import funct
from classes import Item, Room, Combatant

if __name__ == "__main__":
    try:
        #Items:
        # jacket
        jacket = Item("Dark green parka", False)

        ''' 
        Room Attributes
        '''
        # attic
        attic = Room("attic", False, False)
        attic.set_description("- The roof is cracked. To your left you see a circular gable vent tilted open at a precarious angle.\
        Dense but gentle snowflakes are wafting in through the broken roof. To your right is a gray, weathered door.\
        You feel safe but terribly alone.")
        attic.lootable = False

        # hallway
        hallway = Room("hallway", "", False, False)
        hallway.name = "hallway"
        hallway.set_description("- You traced your way down the attic's stairwell and have reached a long hallway. \
        There are three doors along its' length and a stairway at its end.")

        # bedroom 1

        # bedroom 2
        bedroom2 = Room("bedroom 2", True, False, jacket)
        bedroom2.set_description ("- The door was broken down and so you were able to get inside. There is a jostled bed and an old chest.")


        #Variables
        name = "null" #string
        inventory = [] #list
        askoptions = [] #list
        twooptions = ". Would you like to examine or leave?" #str for examine func
        twooptionsstorage = twooptions #str for examine func
        threeoptions = ". Would you like to loot, examine or leave?" #str for examine func

        status = True
        currentroom = "attic"
        combatoptions = ["Attack", "Defend", "Prepare", "Inventory"]

        def p(words):
            print(words)

        #Story begins here

        p("The world is cold.")
        p("You're not..")
        p("Wake up.")

        name = input("Who are you?")

        p(name +". I almost forgot your name.")
        p("Get up. Being on the floor doesn't help anyone, especially not you, "+ name +".") # commas will add a space in the print, addition symbols will not!
        p("You need to find him. Go.")

        choice = input("Get up?")
        # Sashank: find how to convert str to lower or upper case (it will read something like yEs)
        if choice.lower == "yes":
            p("You got up.")

        else:
            for j in range(12):
                p("getup")

            p("You got up.")   

        askoptions.append("Who is he?")

        p("All you need to do is ask to talk to the voice.")
        if choice.lower() == "ask":
            p(askoptions)
        p("Look in your backpack to check your inventory.")


        funct.examineorleave(attic, twooptions, threeoptions, twooptionsstorage, inventory)
        funct.examineorleave(hallway, twooptions, threeoptions, twooptionsstorage, inventory)
        funct.examineorleave(bedroom2, twooptions, threeoptions, twooptionsstorage, inventory)

    except KeyboardInterrupt:
        print(" - Program has been interrupted.")