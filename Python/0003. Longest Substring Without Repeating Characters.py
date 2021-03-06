# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:31:11 2020

@author: gunda
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = {}
        head = 0
        maxlength = 0
        
        for i in range(len(s)):
            if s[i] in indices:
                head = max(head, indices[s[i]]+1)
            maxlength = max(maxlength, i-head+1)
            indices[s[i]] = i
        return maxlength
    
solution = Solution()
solution.lengthOfLongestSubstring('dvdf')
