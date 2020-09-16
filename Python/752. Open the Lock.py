# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 08:58:24 2020

@author: gunda
"""

class Solution:
    def openLock(self, deadends, target):
        if '0000' in deadends: return -1
        if target == '0000': return 0
        
        from collections import deque
        queue = deque()
        seen = {}
        queue.append(['0000', 0])
        
        while queue:
            node, depth = queue.popleft()
            neighbors = []
            for i in range(4):
                neighbors.append([node[:i] + str((int(node[i]) + 1)%10) + node[i+1:], depth + 1])
                neighbors.append([node[:i] + str((int(node[i]) - 1)%10) + node[i+1:], depth + 1])
                
            for [num, depth] in neighbors:
                if num in deadends or num in seen:
                    continue
                seen[num] = True
                
                if num == target:
                    print(depth)
                    return depth
                queue.append([num, depth])
        print(-1)
        return -1
        
solution = Solution()
solution.openLock(["0201","0101","0102","1212","2002"], "0202")