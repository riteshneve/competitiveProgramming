# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 06:00:28 2018

@author: deVelop

https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""

def hourglassSum(arr):
    maxsum = arr[0][0] + arr[0][1] + arr[0][2] + arr[1][2] + arr[2][0] + arr[2][1] + arr[2][2]
    
    for i in range (4):
        for j in range (4):
            tempsum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j+0] + arr[i+2][j+1] + arr[i+2][j+2]
            if (tempsum > maxsum):
                maxsum = tempsum
    return maxsum

arr = [[1, 1, 1, 0, 0, 0], 
       [0, 1, 0, 0, 0, 0], 
       [1, 1, 1, 0, 0, 0], 
       [0, 0, 2, 4, 4, 0], 
       [0, 0, 0, 2, 0, 0], 
       [0, 0, 1, 2, 4, 0]]

print hourglassSum(arr)