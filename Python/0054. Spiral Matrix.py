# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:32:43 2020

@author: gunda
"""

def spiralOrder(matrix):
    # If there is no element in the input, return []
    if not matrix or not matrix[0]:
        return []
    
    # Setting up the left, right, top and bottom boundary as ls, rs, ts, bs
    # Use counter to see if the elements we've appended is in the result
    ls, rs = 0, len(matrix[0])
    ts, bs = 0, len(matrix)
    result = []
    count = 0
    
    # Use ls, rs, ts and bs to push the pointer inwards
    # If the count is equal to the number of elements in the input matrix,
    # break the while loop
    while (ls < rs or ts < bs):
        # Collecting elements from the left to the right
        for n in range(ls, rs):
            result.append(matrix[ts][n])
            count += 1
        ts += 1
        if count == len(matrix[0]) * (len(matrix)):
            break
        
        # Collecting elements from the top to the bottom
        for m in range(ts, bs):
            result.append(matrix[m][rs-1])
            count += 1
        rs -= 1
        if count == len(matrix[0]) * (len(matrix)):
            break
        
        # Collecting elements from the right to the left
        for n in reversed(range(ls, rs)):
            result.append(matrix[bs-1][n])
            count += 1
        bs -= 1
        if count == len(matrix[0]) * (len(matrix)):
            break
        
        # Collecting elements from the bottom to the top 
        for m in reversed(range(ts, bs)):
            result.append(matrix[m][ls])
            count += 1
        ls += 1
        if count == len(matrix[0]) * (len(matrix)):
            break
    
    print(int(len(matrix[0])) * int(len(matrix)))
    print(count)    
    print(result)
    return result
