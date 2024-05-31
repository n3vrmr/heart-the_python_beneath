# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:09:00 2024

@author: Nevermore
"""
# This is the second file in a very long list of files

import dice as d
import time as t

def action(difficulty:str, skill:int=0, domain:int=0, mastery:int=0,
           assists:int=0):
    """
    Function to be used when a character takes an action that requires a roll,
    as defined by the GM and the player. There must be something at stake for
    the character. Ask yourself what the character has to lose when they take
    an action. If there is something to lose, make a roll.
    
    This function will calculate the size of your dice pool and subtract dice
    based on the difficulty of the action, if any. It will also tell you
    whether or not the character has succeeded, and what are the consequences
    of failing... or if your success has come at a cost.

    Parameters
    ----------
    difficulty : str
        Possible values for this argument are: 'standard', 'risky', and
        'dangerous', as defined by the core rulebook. Impossible actions are
        not included in this function.
    skill : int, optional
        If the character has a skill that is relevant to the roll, set this
        value to 1. Otherwise, leave it as it is. The default is 0.
    domain : int, optional
        If the character has a domain that is relevant to the roll, set this
        value to 1. Otherwise, leave it as it is. The default is 0.
    mastery : int, optional
        If the character has a mastery that is relevant to the roll, set this
        value to 1. Otherwise, leave it as it is. The default is 0.
    assists : int, optional
        If any characters are assisting the one taking the action, set this
        value to the number of characters participating. They take stress the
        same way as the character who initiated the action. The GM can limit
        the number of characters who can assist the action. The default is 0.

    Returns
    -------
    single_result
        If your dice pool has been reduced to 0 or less dice due to
        the difficulty, the function rolls a single d10 and returns an int of
        your roll.
    
    take_highest
        In any other case, the function will roll an amount of dice
        equal to your final dice pool and remove the highest results, if the
        difficulty parameter is 'risky' or 'dangerous'. The function will tell
        you what rolls are being removed, then tell you what your highest roll
        was from the remaining pool. Finally, the function will tell you
        whether or not you have succeeded and the consequences of your action.
        In this case, the function returns an int equal to the highest roll of
        your dice pool.

    """

    failure_msg_1 = "\033[1;31;47mCritical failure. Take double stress.\033[0m"
    failure_msg_2 = "\033[1;31;47mFailure. Take stress.\033[0m"
    success_msg_1 = "\033[1;31;47mSuccess at a cost. Take stress.\033[0m"
    success_msg_2 = "\033[1;32;40mSuccess. Take no stress.\033[0m"
    success_msg_3 = "\033[1;32;40mCritical success. Increase outgoing stress dice by 1 step.\033[0m"
    
    relevant_to_roll = [skill, domain, mastery, assists]
    a = sum(relevant_to_roll)
    dice_pool = a + 1
        
    if difficulty == "standard":
        amount_to_remove = 0
    elif difficulty == "risky":
        amount_to_remove = 1
    elif difficulty == "dangerous":
        amount_to_remove = 2
    
    final_pool = dice_pool - amount_to_remove
    
    if final_pool <= 0:
        print("You are attempting a difficult action.")
        t.sleep(1)
        single_result = d.roll(1, 10)
        if single_result == 1:
            print(failure_msg_1)
        elif single_result >= 2 and single_result < 10:
            print(failure_msg_2)
        elif single_result == 10:
            print(success_msg_1)
        return single_result
    
    else:
        rolls = d.roll(dice_pool, 10, s=True)
        
        descending_rolls = sorted(rolls,reverse=True)
        
        if amount_to_remove == 1:
            print(f"Removing highest result: {descending_rolls[0]}")
            t.sleep(1)
            del descending_rolls[0]
        elif amount_to_remove == 2:
            print(f"Removing highest results: {descending_rolls[0:2]}")
            t.sleep(1)
            del descending_rolls[0:2]
    
        take_highest = max(descending_rolls)
        print(f"Your highest roll was a {take_highest}.")
        t.sleep(1)
        
        if take_highest == 1:
            print(failure_msg_1)
        elif take_highest >=2 and take_highest <=5:
            print(failure_msg_2)
        elif take_highest == 6 or take_highest == 7:
            print(success_msg_1)
        elif take_highest == 8 or take_highest == 9:
            print(success_msg_2)
        elif take_highest == 10:
            print(success_msg_3)
        
        return take_highest

def main():
    if __name__ == '__main__':
        print("Good luck.")

if __name__ == '__main__':
    main()
    help(action)
