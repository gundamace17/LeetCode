# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:55:01 2020

@author: gunda
"""

class Solution:
    def findTargetSumWays(self, nums, S):
        counts = {nums[0]:1, -nums[0]:1}
        if nums[0] == 0:
            counts[0] += 1
        
        for num in nums[1:]:
            keys = list(counts)
            new = {}
            
            for key in keys:
                if key + num not in new:
                    new[key + num] = 0
                if key - num not in new:
                    new[key - num] = 0
                new[key + num] += counts[key]
                new[key - num] += counts[key]
            counts = new
            
        return counts[S] if S in counts else 0