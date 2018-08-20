# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 02:33:26 2018

@author: deVelop

https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
"""

def countSwaps(a):
    swapCount = 0
    for i in range(len(a)-1):
        isSwapping = False
        for j in range(len(a)-1):
            if (a[j] > a[j+1]):
                isSwapping = True
                swapCount += 1
                a[j], a[j+1] = a[j+1], a[j]
        if (not isSwapping):
            break
    print "Array is sorted in " + str(swapCount) + " swaps."
    print "First Element: " + str(a[0])
    print "Last Element: " + str(a[len(a) - 1])

a = [1, 2, 3]
countSwaps(a)