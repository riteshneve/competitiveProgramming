# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 01:59:16 2018

@author: deVelop

https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues
"""

def isBalanced(s):
    stack = []
    retValue = "YES"
    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif char == ')' or char == ']' or char == '}':
            if char == ')':
                expClosing = '('
            elif char == ']':
                expClosing = '['
            else:
                expClosing = '{'
            if (len(stack) == 0):
                retValue = "NO"
                break
            if stack[len(stack) - 1] == expClosing:
                stack.pop()
            else:
                retValue = "NO"
                break

    return retValue

print isBalanced("[()][{}[{}[{}]]][]{}[]{}[]{{}({}(){({{}")