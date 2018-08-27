# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 10:17:27 2018

@author: deVelop

https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""

def twoStrings(s1, s2):
    d = {}
    for char in s1:
        d[char] = 1
    for char in s2:
        if char in d:
            return "YES"
    return "NO"

print twoStrings("hi", "world")