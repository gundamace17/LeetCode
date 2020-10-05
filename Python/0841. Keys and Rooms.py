# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 11:33:32 2020

@author: gunda
"""

class Solution:
    def canVisitAllRooms(self, rooms):
        seen = [False]*len(rooms)
        seen[0] = True
        stack = [0]
        
        while stack:
            keys = stack.pop()
            for key in rooms[keys]:
                if not seen[key]:
                    seen[key] = True
                    stack.append(key)
        return all(seen)
    
solution = Solution()
solution.canVisitAllRooms([[1],[2],[3],[]])
