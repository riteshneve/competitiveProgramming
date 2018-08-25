# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 01:39:18 2018

@author: deVelop

https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""

def minimumBribes(q):
    swaps = 0
    for i in xrange(len(q)-1, -1, -1):
        #print q
        if q[i] == i+1:
            #print "continue"
            continue
        if q[i-1] != i+1 and q[i-2] != i+1:
            print "Too chaotic"
            return
        if q[i-1] == i+1:
            #print "swap 1 place"
            q[i], q[i-1] = q[i-1], q[i]
            swaps += 1
        if q[i-2] == i+1:
            #print "swap 2 places"
            q[i-2], q[i-1] = q[i-1], q[i-2]
            q[i], q[i-1] = q[i-1], q[i]
            swaps += 2
    print swaps

minimumBribes([1, 2, 5, 3, 4, 7, 8, 6])