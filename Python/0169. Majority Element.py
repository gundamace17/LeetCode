# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 20:19:16 2020

@author: gunda
"""

import collections
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        print(counts)
        print(max(counts.keys(), key = counts.get))
        return max(counts.keys(), key = counts.get)
    
solution = Solution()
solution.majorityElement([2,2,1,1,1,2,2])
