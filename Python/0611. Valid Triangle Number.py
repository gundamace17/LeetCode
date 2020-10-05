# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 09:54:45 2020

@author: gunda
"""

def triangleNumber(nums):
    nums.sort()
    count = 0
    for i in range(len(nums)-2):
        k = i+2
        for j in range(i+1, len(nums)-1):
            while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
            count += max(0, k-j-1)
            
    print(count)
    return count

# Algorithm:
# 1. Sort the input list
# 2. Check the valid triangle side lengths (a, b, c),
#    in which only a + b > c should be checked.
# 3. Once nums[i] + nums[j] > nums[k] fails, add max(0, k-j-1) to the count
