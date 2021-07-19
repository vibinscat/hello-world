#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:17:34 2020

@author: vibinscat
"""
from itertools import product


def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> 
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    # get the value of cards 1 for royal cards and constants
    sum_hand_1_constants = sum([int(card) for card in hand_1 if card not in ['A','K','Q','J'] ])
    sum_hand_1_royals = sum([10 for card in hand_1 if card in ['K','Q','J']])
    sum_hand_1 = sum_hand_1_constants + sum_hand_1_royals
    
    range_A_hand1 = len([1 for card in hand_1 if card == 'A'])
    comb_A_hand1 = product([1,11], repeat = range_A_hand1)
    
    sum_A_hand1 = [sum(comb) for comb in comb_A_hand1 if sum(comb) <= 21]
    sum_A_hand1 = list( dict.fromkeys(sum_A_hand1) ) # Removing duplicates 
    
    print(sum_A_hand1)
    # check for total sum with differenet combination sums of Card A take the closest to 21
    if 'A' in  hand_1 :
        # check for total sum with differenet combination sums of Card A take the closest to 21
        sums_hand1 = [ (sum_hand_1 + sumA)  for sumA in sum_A_hand1 if (sum_hand_1 + sumA) <= 21 ]
        sums_hand1.sort(reverse=True)
        print(sums_hand1)
        if (len(sums_hand1) > 0):
            sum_hand_1 = sums_hand1.pop()
        else:
            sum_hand_1 = -1
    else:
        if sum_hand_1 > 21:
            sum_hand_1 = -1
    
    
    
    sum_hand_2_constants = sum([int(card) for card in hand_2 if card not in ['A','K','Q','J'] ])
    sum_hand_2_royals = sum([10 for card in hand_2 if card in ['K','Q','J']])
    sum_hand_2 = sum_hand_2_constants + sum_hand_2_royals
    
    range_A_hand2 = len([1 for card in hand_2 if card == 'A'])
    comb_A_hand2 = product([1,11], repeat = range_A_hand2)
    
    sum_A_hand2 = [sum(comb) for comb in comb_A_hand2 if sum(comb) <= 21]
    sum_A_hand2 = list( dict.fromkeys(sum_A_hand2) ) # Removing duplicates 
    
    
    if 'A' in  hand_2 :
        # check for total sum with differenet combination sums of Card A take the closest to 21
        sums_hand2 = [ (sum_hand_2 + sumA)  for sumA in sum_A_hand2 if (sum_hand_2 + sumA) <= 21 ]
        sums_hand2.sort(reverse=True)
        if (len(sums_hand2) > 0):
            sum_hand_2 = sums_hand2.pop()
        else:
            sum_hand_2 = -1
    else:
        if sum_hand_2 > 21:
            sum_hand_2 = -1
    
    
    #print (sum_hand_1_constants)
    #print (sum_hand_1_royals)
    #print(sum_hand_1)
    #print(sum_hand_2)
        
    
    #value_1 = []
    
    
    return sum_hand_1 > sum_hand_2

# Check your answer
#print(blackjack_hand_greater_than(['A','A','K'], ['3', '4']))
hand_1=['4', 'A'] 
hand_2=['4','7']
print(blackjack_hand_greater_than(hand_1, hand_2))

#print(blackjack_hand_greater_than(['K'], ['10']))
#print(blackjack_hand_greater_than(['K', 'K', '2'], ['3']))