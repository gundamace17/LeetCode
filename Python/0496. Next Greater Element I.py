# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:08:45 2020

@author: gunda
"""

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = []
        dic = {}
        stack = []
        
        for num2 in nums2:
            while stack and num2 > stack[-1]:
                dic[stack.pop()] = num2
            stack.append(num2)
            
        for num1 in nums1:
            if num1 in dic:
                res.append(dic[num1])
            else:
                res.append(-1)
        
        print(res)
        return res
        
solution = Solution()
solution.nextGreaterElement([4,1,2,7], [1,3,7,5,6,2,8,4])
