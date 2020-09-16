# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:11:41 2020

@author: gunda
"""

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        islands = 0
        
        def land_track(row, col):
            grid[row][col] = '#'
            if row < m-1 and grid[row+1][col] == '1': # Move down
                land_track(row+1, col)
            if row > 0 and grid[row-1][col] == '1': # Move up
                land_track(row-1, col)
            if col < n-1 and grid[row][col+1] == '1': # Move right
                land_track(row, col+1)
            if col > 0 and grid[row][col-1] == '1': # Move left
                land_track(row, col-1)
            return
        
        for row in range(m):
            for col in range(n):
                print(grid)
                if grid[row][col] == '1':
                    islands += 1
                    land_track(row, col)
        print(islands)
        return islands
        
solution = Solution()
solution.numIslands([["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]])