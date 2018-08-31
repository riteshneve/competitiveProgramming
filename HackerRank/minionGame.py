# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 11:22:40 2018

@author: deVelop

https://www.hackerrank.com/challenges/the-minion-game/problem
"""

def minion_game(string):
    #Stuart has to make words starting with consonants.
    #Kevin has to make words starting with vowels.
    stuartCount = 0
    kevinCount = 0
    length = len(string)
    for i in range(len(string)):
        if string[i] in ['A', 'E', 'I', 'O', 'U']:
            kevinCount += length - i
        else:
            stuartCount += length - i
    if stuartCount > kevinCount:
        print 'Stuart ' + str(stuartCount)
    elif stuartCount < kevinCount:
        print 'Kevin ' + str(kevinCount)
    else:
        print 'Draw'
    
minion_game("BANANA")