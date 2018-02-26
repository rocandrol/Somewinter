'''
This is act 1 (INN) of an adventure game and a project for my class 3D printing and computer engineering.
It holds the working title of Somewinter. It entails a stranded human, alone with a radio.
Author: Emma L. Graves
Date: 2/16/18 - x
'''

#work on game and try to work in functions.
#imports
import funct
import classes

#Variables
name = 0
inventory = []
choice = input()
askoptions = []
roomoptions = ["examine", "leave"]

status = True
currentroom = "attic"
combatoptions = ["Attack", "Defend", "Prepare", "Inventory"]

def p(words):
    print(words)

# Inn Code
if __name__ == "__main__":
    p("The world is cold.")
    p("You're not..")
    p("Wake up.")

    name = input("Who are you?")

    p(name +". I almost forgot your name.")
    p("Get up. Being on the floor doesn't help anyone, especially not you, "+ name +".") # commas will add a space in the print, addition symbols will not!
    p("You need to find him. Go.")

    choice = input("Get up?")
    # Sashank: find how to convert str to lower or upper case (it will read something like yEs)
    if choice == "yes" or choice == "Yes" or choice == "y":
        p("• You got up.")

    else:
        for i in range(12):
            p("getup")

        p("• You got up.")   

    askoptions.append("Who is he?")

    p("All you need to do is ask to talk to the voice.")
    if choice == "Ask" or choice == "ask":
        p(askoptions)
    p("Look in your backpack to check your inventory.")

    nextroom = classes.hallway
    funct.examineorleave(classes.attic, classes.hallway)
