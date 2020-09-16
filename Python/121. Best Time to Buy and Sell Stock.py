# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:03:32 2020

@author: gunda
"""

class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        
        temp_lowest = prices[0]
        profit = []
        
        for i in range(1, len(prices)):
            temp_lowest = min(prices[i], temp_lowest)
            profit.append(prices[i] - temp_lowest)
        
        print(profit)
        print(max(profit))
        return max(profit)
    
solution = Solution()
solution.maxProfit([1])