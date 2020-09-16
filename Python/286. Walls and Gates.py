# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:32:00 2020

@author: gunda
"""

class Solution:
    def wallsAndGates(self, rooms):
        if not rooms:
            return
        m = len(rooms)
        n = len(rooms[0])
        root = []
        
        for i in range(m):
            for j in range(n):
                if not rooms[i][j]:
                    root.append([i, j])
                    
        level = 1
        while root:
            print(rooms)
            queue = []
            while root:
                x, y = root.pop()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    x1 = x + dx
                    y1 = y + dy
                    if 0 <= x1 < m and 0 <= y1 < n and rooms[x1][y1] == 2147483647:
                        rooms[x1][y1] = level
                        queue.append([x1, y1])
            root = queue
            level += 1
        
        print(rooms)

solution = Solution()
solution.wallsAndGates([[2147483647,-1,0,2147483647],
                        [2147483647,2147483647,2147483647,-1],
                        [2147483647,-1,2147483647,-1],
                        [0,-1,2147483647,2147483647]])