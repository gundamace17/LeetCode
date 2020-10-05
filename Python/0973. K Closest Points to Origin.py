# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:00:23 2020

@author: gunda
"""

class Solution:
    def kClosest(self, points, K):
        print(points)
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        print(points)
        return points[:K]
    
solution = Solution()
solution.kClosest([[3,3],[5,-1],[-2,4]], 2)
