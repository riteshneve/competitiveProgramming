# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 21:36:35 2018

@author: deVelop

https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""

def checkMagazine(magazine, note):
    dict = {}
    for str in magazine:
        if str in dict:
            dict[str] += 1
        else:
            dict[str] = 1
    isPossible = True
    for str in note:
        if str in dict and dict[str] > 0:
            dict[str] -= 1
            #print 'continue'
        else:
            isPossible = False
            break;
    return 'Yes' if isPossible else 'No'

magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
note = ['give', 'one', 'grand', 'today']
print checkMagazine(magazine, note)