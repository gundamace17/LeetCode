# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:24:58 2020

@author: gunda
"""

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        self.m = len(board)
        self.n = len(board[0])
        boarder = []
        
        # Collecting all the 'O' on the boarder
        for i in range(self.m):
            if board[i][0] == 'O':
                boarder.append([i, 0])
            if board[i][self.n-1] == 'O':
                boarder.append([i, self.n-1])
        for j in range(self.n):
            if board[0][j] == 'O':
                boarder.append([0, j])
            if board[self.m-1][j] == 'O':
                boarder.append([self.m-1, j])
                
        for row, col in boarder:
            self.BFS(board, row, col)
            
        for row in range(self.m):
            for col in range(self.n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'E':
                    board[row][col] = 'O'
        print(board)
                
    def BFS(self, board, row, col):
        from collections import deque
        queue = deque([[row, col]])
        while queue:
            [row, col] = queue.popleft()
            if board[row][col] != 'O':
                continue
            board[row][col] = 'E'
            
            if col < self.n-1: queue.append([row, col+1])
            if col > 0: queue.append([row, col-1])
            if row < self.m-1: queue.append([row+1, col])
            if row > 0: queue.append([row-1, col])
            
solution = Solution()
solution.solve([["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]])
            