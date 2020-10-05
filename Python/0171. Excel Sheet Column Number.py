# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:15:35 2020

@author: gunda
"""

class Solution:
    def titleToNumber(self, s):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Create a A to Z string
        pairs = {}  # Empty dictionary for storing the value corresponding to each letter
        for num in range(len(letters)):
            pairs[letters[num]] = (num + 1)
        print(pairs)
    
        result = 0 # Initialize the result value
        i = len(s) 
        while i >= 1:
            result = result + pairs[s[i-1]]*pow(26, len(s) - i) # like a decimal system, this case is like 26 system
            print(result)
            i -= 1
        return(result)
