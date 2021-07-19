#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:16:46 2020

@author: vibinscat
"""

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    doc_dic = {val : val.split(' ')   for val in doc_list}
    returnlist = {}
    
    for keyword in keywords:
        value_found = []
        for key, values in doc_dic.items():
            if sum([value.rstrip('.').rstrip(',').lower() == keyword.lower() for value in values]) > 0 :
               value_found.append(doc_list.index(key)) 
        returnlist[keyword] = value_found
            
    return returnlist

# Check your answer
doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']

print(multi_word_search(doc_list, keywords))