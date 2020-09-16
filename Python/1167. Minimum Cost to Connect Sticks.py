# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:26:32 2020

@author: gunda
"""

class Solution:
    def connectSticks(self, sticks):
        sticks.sort()
        cost = 0
        print(sticks)
        while len(sticks) > 1:
            cost += sum(sticks[:2])
            sticks.append(sum(sticks[:2]))
            sticks.pop(0)
            sticks.pop(0)
            sticks.sort()
            print(sticks)
        
        print(cost)
        return cost
    
solution = Solution()
solution.connectSticks([3354,4316,3259,4904,4598,474,3166,6322,8080,9009])