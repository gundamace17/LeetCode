# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:17:26 2020

@author: gunda
"""
import math
def numSquares(n):
    dp = [_ for _ in range(n+1)]
    perfect_square = [1]
    
    for i in range(1, n+1):
        if int(math.sqrt(i))**2 == i:
            dp[i] = 1
            perfect_square.append(i)
        else:
            for j in perfect_square:
                dp[i] = min(dp[i], dp[i-j] + 1)
    
    print(dp[n])
    return dp[n]

# Algirithm:
# 1. Create a list dp from 0 to n**2
# 2. Create a list [1] to collect all the perfect square numbers
# 3. To check every numer in dp:
#        if i is a perfect square number:
#            Only 1 number is needed and
#            append the perfect square to perfect_square
#        if i is not a perfect square number:
#            Subtract each number in perfect_square
#            and the remaining is also a number for which
#            we can know how many perfect square numbers
#            are needed based on the previous elements in dp
#            And replace the dp[i] by the min number

#            ex. n = 13
#            The largest perfect square number less than 13 is 9 and
#            13 - 9 = 4. We already know how many perfect squares to
#            form 4 etc.