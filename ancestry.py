# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:36:55 2024

@author: Nevermore
"""
# This is the fourth file in a very long list of files

import time as t
import random as rd

class Ancestry:
    def __init__(self):
        self.ancestry = self.choosing()
        self.origin = self.origins()
        self.trinkets = self.trinkets()
        return

    def choosing():
        ancestry = input("Choose your character's ancestry: ").lower().strip()
        return ancestry
    
    def origins(self):
        if self._ancestry == "drow":
            self.a = Drow
            o = Drow.drow_details(self)
        elif self._ancestry == "human":
            self.a = Human
            o = Human.human_details(self)
        elif self._ancestry == "aelfir":
            self.a = Aelfir
            o = Aelfir.aelfir_details(self)
        elif self._ancestry == "gnoll":
            self.a = Gnoll
            o = Gnoll.gnoll_details(self)
        return o
    
    def trinkets(self):
        if self._ancestry == "drow":
            t = Drow.drow_trinkets(self)
        elif self._ancestry == "human":
            t = Human.human_trinkets(self)
        elif self._ancestry == "aelfir":
            t = Aelfir.aelfir_trinkets(self)
        elif self._ancestry == "gnoll":
            t = Gnoll.gnoll_trinkets(self)
        return t

class Drow:
    def drow_details(self):
        char_creation = "Answer one of the following questions:"
        q1 = "1. You were born in the City Above and served a durance - 4 years of indentured servitude - to a cruel aelfir. What were you forced to do?"
        q2 = "2. You were born in the City Beneath. Where does your family live, and who or what do they worship?"
        q3 = "3. You're a traveller from a distant nation. The desert of Aliquam, the treacherous foothills of Nujab or the warrenous Home Nations. Where are you from, and why aren't you there anymore?"
        print(char_creation)
        t.sleep(1.5)
        print(q1)
        t.sleep(3)
        print(q2)
        t.sleep(3)
        print(q3)
        t.sleep(3)
        
        choice = int(input("Choose one of the options. Type 1, 2 or 3: ").strip())
        if choice == 1:
            origin = q1
        elif choice == 2:
            origin = q2
        else:
            origin = q3
        answer = input("Write your answer to the question: ")
        self._origin = {origin:answer}
        return self._origin
    
    def drow_trinkets(self):
        trinkets_list = ["Deck of Malrique fortune cards","Yeast mother",
                         "Half a bottle of malak tincture; all that remains of your stash",
                         "Dog-tags from the Allied Defense Forces",
                         "Friendly but stupid pocket mouse",
                         "Hand-drawn image of your dad's largest pig",
                         "Bag of statuettes representing The Many, a gang of refugee gods",
                         "Portable triptych shrine to the Moon Goddess, incense, candles",
                         "Small collection of Half-sten Horror sensationalist pulp literature",
                         "Coupon good for 1 (one) skywhale trip to Ys",
                         "Warm, hand-knitted scarf and gloves",
                         "Battered leather mask","Midwife's blood-letting kit",
                         "Brightly-coloured headscarf and dark glasses",
                         "Bottle of corpsefruit liqueur",
                         "Your mother's second-best dagger",
                         "Votive image of Hallow Hearts-Breath-Hiding",
                         "Well-worn brass statuette of an open mouthed toad",
                         "Wanted poster from the City Above with your face on it"]
        
        name_list = ["Yeast mother","Friendly but stupid pocket mouse"]
        
        first_trinket = trinkets_list[rd.randint(0, 19)]
        trinkets_list.remove(first_trinket)
        second_trinket = trinkets_list[rd.randint(0, 18)]
        
        character_trinkets = [first_trinket,second_trinket]
        if character_trinkets[0] == name_list[0] or character_trinkets[1] == name_list[0]:
            yeast_mother_name = input("Name your yeast mother: ")
            character_trinkets.append({"Yeast mother name":yeast_mother_name})
        if character_trinkets[0] == name_list[1] or character_trinkets[1] == name_list[1]:
            mouse_name = input("Name your pocket mouse: ")
            character_trinkets.append({"Mouse name":mouse_name})
        self._trinkets = character_trinkets
        print(f"Your trinkets: {self._trinkets}")
        return self._trinkets
    
class Human:
    def human_details(self):
        char_creation = "Answer one of the following questions:"
        q1 = "1. You are from the Eastern Kingdoms. You came to Spire with nothing but the clothes on your back and a dream, looking for excitement and profit. What went wrong?"
        q2 = "2. You were kicked out of a retro-engineering or magical college thanks to your unorthodox beliefs and practices. What did you do?"
        q3 = "3. You're third-generation Heartborn, and not at all like the humans on the surface. What incorrect assumption do people most often make about you?"
        print(char_creation)
        t.sleep(1.5)
        print(q1)
        t.sleep(3)
        print(q2)
        t.sleep(3)
        print(q3)
        t.sleep(3)
        
        choice = int(input("Choose one of the options. Type 1, 2 or 3: ").strip())
        if choice == 1:
            origin = q1
        elif choice == 2:
            origin = q2
        else:
            origin = q3
        answer = input("Write your answer to the question: ")
        self._origin = {origin:answer}
        return self._origin
    
    def human_trinkets(self):
        trinkets_list = ["Grail charm made of wyvern-bone",
                         "Bullet with your own name carved on it",
                         "Broken pocket-watch with a picture of your mum in it",
                         "Arcology shard necklace",
                         "String of flickering coloured magelights",
                         "Votive image of a deceased Wanderer-King",
                         "Dog-eared Whitecross travel documents",
                         "Long-stemmed pipe and pungent tobacco",
                         "Feather-tokens to Luxulyan, Duke of Air",
                         "A single mechanical finger (in place of your own)",
                         "Battered and oft-repaired green coat",
                         "Custom scrimshaw kit, well-used",
                         "Sporadically-updated travel diary",
                         "Hard-to-clean drinking horn",
                         "Matching shell-casing charm bracelets, variety of calibers",
                         "Three slim unopened cans of cooked eels",
                         "Once colourful mercenary fatigues",
                         "Harmonica inscribed with 'SUMMER-COURT'",
                         "Pop-arcana book about humanity's ability to ascend to godhood, and how YOU can do it",
                         "Brightly coloured fish in a jar"]
        
        name_list = ["Brightly coloured fish in a jar"]
        
        first_trinket = trinkets_list[rd.randint(0, 19)]
        trinkets_list.remove(first_trinket)
        second_trinket = trinkets_list[rd.randint(0, 18)]
        
        character_trinkets = [first_trinket,second_trinket]
        if character_trinkets[0] == name_list[0] or character_trinkets[1] == name_list[0]:
            fish_name = input("Name your fish: ")
            character_trinkets.append({"Fish name":fish_name})
        self._trinkets = character_trinkets
        print((f"Your trinkets: {self._trinkets}"))
        return self._trinkets
    
class Aelfir:
    def aelfir_details(self):
        char_creation = "Answer one of the following questions:"
        q1 = "1. You still wear your mask. What does it look like, and why do you wear it?"
        q2 = "2. Your family name was ruined by a cataclysmic social faux pas. What did they do?"
        q3 = "3. You still cling to one luxury that keeps you centered - a habit, a style of clothing, a drug, etc. What is it?"
        print(char_creation)
        t.sleep(1.5)
        print(q1)
        t.sleep(3)
        print(q2)
        t.sleep(3)
        print(q3)
        t.sleep(3)
        
        choice = int(input("Choose one of the options. Type 1, 2 or 3: ").strip())
        if choice == 1:
            origin = q1
        elif choice == 2:
            origin = q2
        else:
            origin = q3
        answer = input("Write your answer to the question: ")
        self._origin = {origin:answer}
        return self._origin
    
    def aelfir_trinkets(self):
        trinkets_list = ["Vial of orchid oil-perfume","Fingerbone necklace",
                         "Your brother's preserved eye in a glass jar",
                         "Oversized and awkward book of family history",
                         "Your spouse's death-mask",
                         "Devotional circlet bearing imagery of the Solar Pantheon",
                         "Semi-functional music box",
                         "Ticket stub from an Opera-Orgy",
                         "Mummified cat","Elaborate and shrill-sounding flute",
                         "Glasses with red-tinted smoked lenses",
                         "Bone-pipe and the dregs of a poppy-dust bag",
                         "The flensing knife you got for your fifth birthday",
                         "Sword hilt with a half-inch of broke blade",
                         "Sacred symbols of the Old Gods, outlawed in the City Above",
                         "Metal teeth (original teeth removed due to boredom)",
                         "Spritz bottle and pocket fan, to keep from overheating",
                         "Stunted tree that grows sour fruit",
                         "Paints, brushes, and an easel of sorts",
                         "Patchy evidence regarding your step-sister's betrayal"]
        
        name_list = ["Mummified cat"]
        
        first_trinket = trinkets_list[rd.randint(0, 19)]
        trinkets_list.remove(first_trinket)
        second_trinket = trinkets_list[rd.randint(0, 18)]
        
        character_trinkets = [first_trinket,second_trinket]
        if character_trinkets[0] == name_list[0] or character_trinkets[1] == name_list[0]:
            cat_name = input("Name your cat: ")
            character_trinkets.append({"Cat":cat_name})
        self._trinkets = character_trinkets
        print((f"Your trinkets: {self._trinkets}"))
        return self._trinkets
    
class Gnoll:
    def gnoll_details(self):
        char_creation = "Answer one of the following questions:"
        q1 = "1. You travelled to the Heart in search of something specific. Were you part of a team, or were you on your own - and did you find what you were looking for?"
        q2 = "2. You fled Spire - you were an escaped prisoner of war, a refugee or an agent on a clandestine mission. What do you miss the most about the surface world?"
        q3 = "3. You were born down here. What image do you project to impress, surprise, or intimidate people?"
        print(char_creation)
        t.sleep(1.5)
        print(q1)
        t.sleep(3)
        print(q2)
        t.sleep(3)
        print(q3)
        t.sleep(3)
        
        choice = int(input("Choose one of the options. Type 1, 2 or 3: ").strip())
        if choice == 1:
            origin = q1
        elif choice == 2:
            origin = q2
        else:
            origin = q3
        answer = input("Write your answer to the question: ")
        self._origin = {origin:answer}
        return self._origin
    
    def gnoll_trinkets(self):
        trinkets_list = ["Tiny sealed box that gets angry when you shake it",
                         "Several cubes of refined sugar, wrapped in red paper",
                         "Annotated map of the war-torn Dust region",
                         "Stag beetle in a jar",
                         "Knotted weave of string that describes your grandmother",
                         "Poetry anthology with your work in it",
                         "Nujabian military fatigues",
                         "Spyglass built  by your lover","Warm, leathery egg",
                         "Hair-dressing scissors, razor and mirror",
                         "Painted dog skull",
                         "Book of unsolved mathematical equations",
                         "Small sphere with southern star-map on it",
                         "Zither inscribed with vine-leaves",
                         "Book of macabre fairy-tales",
                         "Tacky lenticular image of the Source Pyramid in Al'Marah",
                         "Vial of rainwater from the southlands",
                         "Brass-inlaid tin half-filled with a brown, gritty stimulant",
                         "Bag of boiled sweets (various flavours)",
                         "Djinn battery you don't know how to recharge"]
        
        name_list = ["Stag beetle in a jar"]
        
        first_trinket = trinkets_list[rd.randint(0, 19)]
        trinkets_list.remove(first_trinket)
        second_trinket = trinkets_list[rd.randint(0, 18)]
        
        character_trinkets = [first_trinket,second_trinket]
        if character_trinkets[0] == name_list[0] or character_trinkets[1] == name_list[0]:
            beetle_name = input("Name your beetle: ")
            character_trinkets.append({"Beetle":beetle_name})
        self.trinkets = character_trinkets
        print((f"Your trinkets: {self.trinkets}"))
        return self.trinkets
    
def main():
    if __name__ == '__main__':
        print("Regular Gnoll")

if __name__ == '__main__':
    main()
