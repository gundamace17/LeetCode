# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:39:54 2020

@author: gunda
"""

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        self.R = len(image)
        self.C = len(image[0])
        oldColor = image[sr][sc]
        if newColor == oldColor:
            return image
        
        def DFS(row, col):
            if image[row][col] == oldColor:
                image[row][col] = newColor
                if row > 0: DFS(row-1, col)
                if row < self.R-1: DFS(row+1, col)
                if col > 0: DFS(row, col-1)
                if col < self.C-1: DFS(row, col+1)
                
        DFS(sr, sc)
            
        print(image)
        return image
        
            
solution = Solution()
solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
