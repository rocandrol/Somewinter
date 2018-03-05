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
        '''
        Items
        '''
        # jacket
        jacket = Item("Dark green parka", False)

        ''' 
        Room Attributes
        '''
        # attic
        attic = Room("attic", False, False, False)
        attic.set_description("- The roof is cracked. To your left you see a circular gable vent tilted open at a precarious angle.\
        Dense but gentle snowflakes are wafting in through the broken roof. To your right is a gray, weathered door.\
        It doesn't look like there is any loot for you here. You feel safe but terribly alone.")
        attic.lootable = False

        # hallway
        hallway = Room("hallway", "", False, False)
        hallway.name = "hallway"
        hallway.set_description("- You traced your way down the attic's stairwell and have reached a long hallway. \
        It doesn't look like there's any loot for you here, but there are three doors along its length which could have something.")

        # bedroom 1
        bedroom1 = Room("bedroom 1", True, True, True, "Fist wrappings")

        # bedroom 2
        bedroom2 = Room("bedroom 2", True, False, False, jacket)
        bedroom2.set_description ("- The door was broken down so you were able to get inside. \
        There is a jostled bed and an old chest which could have some loot.")


        #Variables
        name = "null" #string
        inventory = [] #list
        askoptions = [] #list
        twooptions = ". Would you like to examine or leave?" #str for examine func
        twooptionsstorage = twooptions #str for examine func
        threeoptions = ". Would you like to loot, examine or leave?" #str for examine func

        status = True #boolean

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
        if choice.lower == "yes":
            p("You got up.")

        else:
            for j in range(12):
                p("getup")
            p("- You got up.")   

        p("Examine this place.. Search for items that could help you.")
        p("- The radio emits static and if the talk button works the voice isn't letting you know. You're on your own.")
        p("You have a backpack. Perhaps you could check it by saying inv or backpack?")

        funct.examineorleave(attic, twooptions, threeoptions, twooptionsstorage, inventory)
        funct.examineorleave(hallway, twooptions, threeoptions, twooptionsstorage, inventory)
        funct.examineorleave(bedroom2, twooptions, threeoptions, twooptionsstorage, inventory)
        p()

    except KeyboardInterrupt:
        print(" - Program has been interrupted.")