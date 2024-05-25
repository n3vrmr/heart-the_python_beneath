# -*- coding: utf-8 -*-
"""
Created on Sat May 25 19:11:27 2024

@author: Nevermore
"""

from ancestry import Ancestry

class Character:
    def __init__(self):
        self._ancestry = Ancestry.choosing()
        self._origin = Ancestry.origins(self)
        self._trinkets = Ancestry.trinkets(self)
        return
    
c = Character()