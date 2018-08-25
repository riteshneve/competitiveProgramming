# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 01:27:36 2018

@author: deVelop

https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
"""

def makeAnagram(a, b):
    deletions = 0
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in b:
        if i in d and d[i] > 0:
            d[i] -= 1
        else:
            deletions += 1
    for key in d:
        deletions += d[key]
    return deletions

print makeAnagram("cde", "abc")