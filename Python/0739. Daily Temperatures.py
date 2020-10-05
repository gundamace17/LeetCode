# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:26:44 2020

@author: gunda
"""

class Solution:
    def dailyTemperatures(self, T):
        wait = [0]*len(T)
        stack = []
        
        for day, temp in enumerate(T):      
            while stack and temp > T[stack[-1]]:
                k = stack.pop()
                wait[k] = day - k
            stack.append(day)
            
        print(wait)
        return wait
    
solution = Solution()
solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
