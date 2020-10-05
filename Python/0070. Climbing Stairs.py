# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:06:06 2020

@author: gunda
"""

def climbStairs(n):
    dp = [None] * (n+1)
    dp[0] = dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[n])
    return dp[n]
