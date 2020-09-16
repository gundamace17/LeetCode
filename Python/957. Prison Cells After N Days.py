# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:08:34 2020

@author: gunda
"""

class Solution:
    def prisonAfterNDays(self, cells, N):
        if not N:
            return cells
        seen = []
        while N:
            res = [0] * len(cells)
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    res[i] = 1
            cells = res
            if res in seen:
                break
            else:
                seen.append(res)
        print(seen)
        n = N % len(seen)
        if n == 0:
            print(seen[-1])
            return seen[-1]
        else:
            print(seen[n-1])
            return(seen[n-1])
    
solution = Solution()
solution.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000)