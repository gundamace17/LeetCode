# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:57:31 2020

@author: gunda
"""

def findMedianSortedArrays(nums1, nums2):
    merged = nums1 + nums2
    merged.sort()
    mid = len(merged) // 2
    print(mid)
    if len(merged) % 2 == 0:
        print((merged[mid-1] + merged[mid]) * 0.5)
        return (merged[mid-1] + merged[mid]) * 0.5
    else:
        print(merged[mid])
        return merged[mid]
    
    
# Algorithm:
# Join the two lists together and sort the merged list
# Find the middle element of the list
# Define the mid as len(merged) // 2
# If len(merged) is odd, the mid is equal to merged[mid]
# If len(merged) is even, the mid is equal to (merged[mid-1] + merged[mid])-0.5