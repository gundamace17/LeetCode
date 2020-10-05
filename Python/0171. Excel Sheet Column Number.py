# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:15:35 2020

@author: gunda
"""

class Solution:
    def titleToNumber(self, s):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        pairs = {}
        for num in range(len(letters)):
            pairs[letters[num]] = (num + 1)
        print(pairs)
    
        result = 0
        i = len(s)
        while i >= 1:
            result = result + pairs[s[i-1]]*pow(26, len(s) - i)
            print(result)
            i -= 1
        return(result)