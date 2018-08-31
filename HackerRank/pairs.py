# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 11:07:40 2018

@author: deVelop

https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
"""

def pairs(k, arr):
    count = 0
    i = 0
    j = 1
    n = len(arr)
    arr.sort()
    while j < n:
        diff = arr[j] - arr[i]
        if diff == k:
            count += 1
            j += 1
        elif diff < k:
            j += 1
        else:
            i += 1        
    return count

print pairs(2, [1, 5, 3, 4, 2])