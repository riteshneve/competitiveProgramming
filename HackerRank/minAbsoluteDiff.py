# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 02:48:43 2018

@author: deVelop

https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
"""

def minimumAbsoluteDifference(arr):
    if len(arr) != len(list(set(arr))):
        return 0
    arr = sorted(arr)
    minAbsDiff = abs(arr[0] - arr[1])
    for i in range(1, len(arr) - 1):
        if (minAbsDiff > abs(arr[i] - arr[i+1])):
            minAbsDiff = abs(arr[i] - arr[i+1])
    return minAbsDiff

arr = [3, -7, 0, 0]
print minimumAbsoluteDifference(arr)