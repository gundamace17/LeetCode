# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 12:45:26 2020

@author: gunda
"""

class Solution:
    def isValid(self, s):
        stack = []
        brackets = ['(', '[', '{']
        mapping = {'(': ')', '[': ']', '{': '}'}
        
        for char in s:
            if char in brackets:
                stack.append(char)
            elif stack and char == mapping[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
    
solution = Solution()
solution.isValid("{[)]}")
