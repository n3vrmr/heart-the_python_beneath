# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:11:27 2024

@author: Nevermore
"""

import dice as d
import time as t
import pandas as pd
from fallout import *
from ancestry import Ancestry

class Character:
    def __init__(self):
        self._name = input("Character name: ")
        self._ancestry = Ancestry.choosing()
        self._origin = Ancestry.origins(self)
        self._trinkets = Ancestry.trinkets(self)
        self.resistances = {"blood":0,"mind":0,"echo":0,"fortune":0,
                            "supplies":0}
        self.protection = {"blood":0,"mind":0,"echo":0,"fortune":0,
                           "supplies":0}
        self.character_fallout = pd.DataFrame({"level":[],
                                               "kind":[],
                                               "name":[],
                                               "description":[],
                                               "duration":[]})
        return
    
    def add_fallout(self, name:str):
        return
    
    def apply_fallout(self, kind:str):        
        stress_check = d.roll(1, 12)
        if stress_check < 6:
            fallout_level = "minor"
        else:
            fallout_level = "major"
        
        if stress_check <= self.resistances.get(kind):
            self.resistances[f"{kind}"] = 0
            print(f"{self._name} has taken {fallout_level} fallout to {kind}.")
            
            
        else:
            print("No fallout taken.")
            return self.resistances
        return self.resistances
    
    def apply_stress(self, kind:str, dice="d4"):
        if dice == "d4":
            amount = d.roll(1, 4)
        elif dice == "d6":
            amount = d.roll(1, 6)
        elif dice == "d8":
            amount = d.roll(1, 8)
        elif dice == "d10":
            amount = d.roll(1, 10)
        elif dice == "d12":
            amount = d.roll(1, 12)
            
        total = amount - self.protection.get(kind)
        
        if total > 0:
            self.resistances[f"{kind}"] =  self.resistances.get(kind) + amount
            print(f"{self._name} has taken {amount} stress to {kind}.")
            t.sleep(1.8)
            print("Checking for fallout...")
            t.sleep(1.8)
            self.apply_fallout(kind)
        
        else:
            print("No stress or fallout taken due to protection.")
        
        return self.resistances
    
c = Character()
