# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 02:17:25 2018

@author: deVelop

https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/forum?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
"""

def whatFlavors(cost, money):
    dict = {}
    firstMoney = 0
    secondMoney = 0
    for i in range(len(cost)):
        firstMoney = i
        if money - cost[i] in dict:
            secondMoney = dict[money - cost[i]]
            break
        if cost[i] not in dict:
            dict[cost[i]] = i
    print secondMoney + 1, firstMoney + 1
    
money = 4
cost = [1, 4, 5, 3, 2]
whatFlavors(cost, money)