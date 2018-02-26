import inn
import funct

class Combatant(object):
    name = None #String
    hp = None #Integer
    speedstat = None #Integer

class Room():
    name = None #String
    description = None #String
    loot = None #String
    lootable = None #Boolean
    locked = None #Boolean
    deny = None #Boolean

class Item():
    name = None #String
    consumable = None #Boolean

#Items:
# jacket
jacket = Item()
jacket.name = "Dark green parka"
jacket.consumable = False

#Rooms: 
# attic
attic = Room()
attic.description = "The roof is cracked and to your left you see a circular gable vent tilted open at a precarious angle. Dense and gentle snowflakes are wafting in through the broken roof. To your right is a gray, weathered door. You feel safe but terribly alone."
attic.lootable = False

# hallway
hallway = Room()
hallway.description = "You traced your way down the attic's stairwell and have reached a long hallway. There are three doors along its' length and a stairway at its end."
hallway.lootable = False

# bedroom 1

# bedroom 2
bedroom2 = Room()
bedroom2.description = "The door was broken down and so you were able to get inside. There is a jostled bed and an old chest."
bedroom2.lootable = True
bedroom2.loot = jacket

# bedroom 3

# foyer
foyer = Room()
foyer.description = ""