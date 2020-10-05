# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:46:12 2020

@author: gunda
"""
from collections import deque
class Solution:
    def updateMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        root = deque()
        
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    root.append([i, j])
                else:
                    matrix[i][j] = float('inf')
        print(root)
                    
        while root:
            x, y = root.popleft()
            level = matrix[x][y] + 1
            print(root)
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x,y-1)]:
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > level:
                    matrix[nx][ny] = level
                    root.append((nx, ny))
        
        print(matrix)
        
solution = Solution()
solution.updateMatrix([[0,0,0],
                       [0,1,0],
                       [1,1,1]])
