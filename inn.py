'''
This is act 1 (INN) of an adventure game and a project for my class 3D printing and computer engineering.
It holds the working title of Somewinter. It entails a stranded human, alone with a radio.
Author: Emma L. Graves
Date: 2/16/18 - x
'''


#imports
import funct
import time
from classes import Item, Room, Combatant


if __name__ == "__main__":
    try:
        '''
        Items
        '''
        # jacket
        jacket = Item("Dark green parka", False)
        key = Item("Brass key", False)
        key.name_ = "Brass key"

        #weapon variables
        #barehands = randint(4, 7)
        #fistwrappings = randint(5, 8)
        #brassknuckles = rantint(7, 10)

        #health variables
        rags = 15
        parka = 20
        leather = 30

        herodamageintmin = 3
        herodamageintmax = 6

        ''' 
        Room pt 1 Attributes
        '''
        # attic
        attic = Room("attic", False, False, False)
        desc = ("- The roof is cracked. To your left you see a circular gable vent tilted open at a precarious angle. "
        "Dense but gentle snowflakes are wafting in through the broken roof. To your right is a gray, weathered door. "
        "It doesn't look like there is any loot for you here. You feel safe but terribly alone.")
        attic.set_description(desc)
        attic.lootable = False

        # hallway
        hallway = Room("hallway", "", False, False)
        hallway.name = "hallway"
        hallway.set_description("- It doesn't look like there's any loot in the hallway, "
        "but there are three doors along its length which might contain something."
        " You're certain there's something or someone at the end of the hallway.")

        # hallway2
        hallway2 = Room("hallway", "", False, False)
        hallway2.name = "hallway"
        hallway2.set_description("- There is very little here besides the crate you are now kneeling behind. "
        "There is something up ahead. You're going to run into it if you want to keep moving.")

        # bedroom 2
        bedroom2 = Room("second bedroom", True, False, False, jacket)
        bedroom2.set_description("- The door was broken down so you were able to get inside. "
        "There is a jostled bed and an old chest which could have some loot.")


        '''
        Room pt. 2 attributes
        '''
        #Foyer
        foyer = Room("foyer", False, False, False)
        foyer.set_description("- The foyer is open and musty. There is a gnarled"
        " chandelier whose candles have dripped a copious amount of wax onto an old rug in the center of the room.")

        #Kitchen
        kitchen = Room("kitchen", True, False, True, key)
        kitchen.set_description("- The kitchen is brighter than the other areas. It holds a large intact window that's "
        "smothered with snow. You can't see out of it, but when you're close to it you can hear faint whining noises. "
        "After a brief examination, you find a set of drawers that look like they could be pried open.")

        '''
        Mobs
        '''
        # yeti
        yeti = Combatant("Yeti", 10, 3, 5, 0)

        #Variables
        name = "null" #string
        inventory = ["Backpack is empty."] #list
        askoptions = [] #list
        twooptions = ". Would you like to examine or leave? " #str for examine func
        othtwooptions = ". Would you like to examine or continue? " #str for examine func
        twooptionsstorage = twooptions #str for examine func
        threeoptions = ". Would you like to loot, examine or leave? " #str for examine func
        outcome = True

        status = True #boolean

        def p(words):
            print(words)

        #Story begins here

        p("The world is cold.")
        p("You aren't..")
        p("Wake up.")

        name = input("Who are you? ")

        p(name +". I almost forgot your name.")
        p("Get up. Being on the floor doesn't help anyone, especially not you, "+ name +".") # commas will add a space in the print, addition symbols will not!
        p("You need to find him. Go.")

        choice = input("Get up? ")
        if choice.lower == "yes":
            p("- You got up.")

        else:
            for j in range(12):
                p("getup")
            p("- You got up.")   

        p("Examine this place.. Search for items that could help you.")
        p("- The radio emits static and if the talk button works the voice isn't letting you know. You're on your own.")
        p("You have a backpack. Perhaps you could check it by saying inv or backpack?")

        funct.examineorleave(attic, twooptions, threeoptions, twooptionsstorage, inventory)
        p("- There is a loud scratching noise at the end of the hallway. Save for soft streams of light coming through"
        " a few windows on the lefthand side, you are in shadows. There are three doors, but would you chance to open them?")
        funct.examineorleave(hallway, twooptions, threeoptions, twooptionsstorage, inventory)
        p("- The first door was locked. You continued to the second door.")
        funct.examineorleave(bedroom2, twooptions, threeoptions, twooptionsstorage, inventory)
        p("- The creature is right in front of you. You're about to run into it.")
        funct.examineorleave(hallway2, twooptions, threeoptions, twooptionsstorage, inventory)
        funct.combat(rags, herodamageintmin, herodamageintmax, yeti.dmgmin, yeti.dmgmax, yeti.hp, yeti.name, outcome)
        if outcome == True:
            p("The Yeti collapsed. It's skin is wrinkled and peppered with matted tufts of once-white fur."
            "It doesn't appear to have any loot. You decided to move along.")
            p("You are in the foyer.")
            p("- Down the stairs from the hallway, you see an exit. It's a weathered gray door. You try the handle a few times, but "
            "it won't budge. You need a key.")
        funct.examineorleave(foyer, twooptions, threeoptions, twooptionsstorage, inventory)
        funct.combat(rags, herodamageintmin, herodamageintmax, yeti.dmgmin, yeti.dmgmax, yeti.hp, yeti.name, outcome)
        funct.examineorleave(kitchen, twooptions, threeoptions, twooptionsstorage, inventory)
        while True:
                if kitchen.lootable == False:
                    p("You made your way back to the foyer and slipped the key into the lock. You made it outside.")
                    p("its white")
                    p("so")
                    p("white")
                    p("its everywhere")
                    p("...")
                    p("the end")
                    p("?")
                    break
                if kitchen.lootable == True:
                    p("You don't have the key yet, you need to keep looking.")
                    funct.examineorleave(kitchen, twooptions, threeoptions, twooptionsstorage, inventory)
                    
    except KeyboardInterrupt:
        print(" - Program has been interrupted.")