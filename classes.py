"""
This is a file containing all classes for Somewinter.
Author: Emma Graves
Date: 2/16/18 - x
"""

'''
Combatant
Enemy class
'''

class Combatant(object):
    def __init__(self, name_, hp_, dmgmin_, dmgmax_, speedstat_):
        self.name = name_ #string
        self.hp = hp_ #string
        self.dmgmin = dmgmin_ #int
        self.dmgmax = dmgmax_ #int
        self.speedstat = speedstat_ #integer

'''
Room
Class defining
'''
class Room():
    def __init__(self, name_, lootable_, locked_, enemy_, loot_=""):
        self.name = name_ #String
        self.loot = loot_ #String
        self.lootable = lootable_ #Boolean
        self.locked = locked_ #Boolean
        self.enemy = enemy_ #Boolean
    
    def set_description(self, description_):
        self.description = description_ #String
    
    def __str__(self):
       return self.name #String

class Item():
    # Init method, constructor
    def __init__(self, name_, consumable_):
        self.name = name_ #String
        self.consumable = consumable_ #Boolean
