# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 01:55:25 2018

@author: deVelop
"""

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
        if year % 400 == 0:
            leap = True
    else:
        leap = False
    return leap

print is_leap(1992)