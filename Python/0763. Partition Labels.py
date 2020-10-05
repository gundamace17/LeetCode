# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:14:52 2020

@author: gunda
"""

class Solution:
    def partitionLabels(self, S):
        last_seen = {char: i for i, char in enumerate(S)}
        res = []
        j = partition = 0
        for i, char in enumerate(S):
            j = max(j, last_seen[char])
            if i == j:
                res.append(i - partition + 1)
                partition = i+1
                
        print(res)
        return res
    
solution = Solution()
solution.partitionLabels("ababcbacadefegdehijhklij")                
