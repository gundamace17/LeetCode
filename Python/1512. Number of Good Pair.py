# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:53:29 2020

@author: gunda
"""

def numIdenticalPairs(nums):
    nums.sort() # Sort the input array
    result = 0 
    i = 0
    
    # Use while loop to iterate the values and skip the duplicates
    while i < len(nums):
        count = 0 # count for one element
        count += nums.count(nums[i]) # Calculate how many duplicates are there
        
        # Assume we get (1, 1, 1, 1, 1) as duplicates
        # The number of pairs would be 4+3+2+1 = 10
        # The formula is (4+1)*4*0.5 as we calculate the area of a trapezoid
        # As shown below:
        result += count*(count-1)*0.5
        i += count # Move the cursor directly to the next non-duplicate element
        
    print(result)
    return(int(result))

numIdenticalPairs([4, 4, 2, 2])