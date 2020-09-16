# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 21:41:55 2020

@author: gunda
"""

def maxArea(height):
    ls = 0 # Setting the left cursor
    rs = len(height) - 1 # Setting the right cursor
    volume_max = 0 # Initialize the max volume
    
    # Move the cursors
    # Defining the total max volume
    # and move the cursor where the height[cursor] is smaller
    # Take the maximum of the volume between the old volume and the new one
    while ls < rs:
        volume_max = max(volume_max, (rs - ls) * min(height[ls], height[rs]))
        
        if height[ls] < height[rs]:
            ls += 1
        else:
            rs -= 1
            
    print(volume_max)
    return(volume_max)

maxArea([1,11,6,2,5,4,8,3,7,11])