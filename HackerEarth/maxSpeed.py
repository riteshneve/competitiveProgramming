# -*- coding: utf-8 -*-
"""
Created on Tue Sep 04 10:32:32 2018

@author: deVelop

https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/speed-7/
"""

def getCarsAtTopSpeed(speed):
    minSpeed = speed[0]
    count = 1
    for i in range (1, len(speed)):
        if (speed[i] < minSpeed):
            minSpeed = speed[i]
            count += 1
    return count

t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    speed = [int(x) for x in raw_input().split()]
    print getCarsAtTopSpeed(speed)