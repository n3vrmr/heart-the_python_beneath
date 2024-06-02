# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:11:27 2024

@author: Nevermore
"""

import dice as d
import time as t
import pandas as pd
from fallout import minor_fallout, major_fallout, critical_fallout, fallout_df
from ancestry import Ancestry

class Character:
    def __init__(self):
        """
        Function used to create a character as a class object and structure its
        methods and attributes specific to it.

        Returns
        -------
        None.

        """
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
        """
        Checks existing stress in a character's specified resistance and rolls
        a d12 to see if any fallout should be applied to that resistance. Then,
        clears stress of that resistance if fallout is applied. This function 
        will be used automatically whenever stress is applied to a character.

        Parameters
        ----------
        kind : str
            The resistance to which fallout will be applied. Acceptable values
            for this parameter are:
                blood
                mind
                echo
                fortune
                supplies.

        Returns
        -------
        self.resistances : modified dict object of the character's resistances
        and their values.

        """
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
    
    def apply_stress(self, kind:str, dice:str="d4"):
        """
        If a character takes stress from a roll (the function used to roll will
        tell you), use this method. It will apply stress to the character
        according to the parameters used. If the character's protection for the
        resitance to which stress will be applied negates the amount of stress,
        no stress will be applied. If stress is applied, the function will then
        roll for fallout.

        Parameters
        ----------
        kind : str
            The resistance to which stress will be applied. Acceptable values
            for this parameter are:
                blood
                mind
                echo
                fortune
                supplies
                
        dice : str, optional
            Size of the dice which will be used to calculate the amount of
            stress to be applied. Since the core rulebook gives freedom for the
            GM to decide this, any dice size from a d4 to a d12 is acceptable.
            The dice size should be written as the letter d immediately 
            followed by the number of sides it has. The default is "d4".

        Returns
        -------
        self.resistances : modified dict object of the character's resistances
        and their values.

        """
        resistances_list = ['blood','mind','echo','fortune','supplies']
        if kind not in resistances_list:
            raise ValueError("Select one between blood, mind, echo, fortune or supplies.")
        
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
        else:
            raise ValueError("Dice size not acceptable.")
            
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
    
def main():
    if __name__ == '__main__':
        print("The Heart beckons...")
    return

if __name__ == '__main__':
    main()
