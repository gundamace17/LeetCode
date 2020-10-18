# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:24:09 2020

@author: gunda
"""

class Solution:
    def sortedSquares(self, A):
        
        for i in range(len(A)):
            A[i] = (A[i])**2
            
        A.sort()
        return A
    
sol = Solution();
sol.sortedSquares([-7,-3,2,3,11])
