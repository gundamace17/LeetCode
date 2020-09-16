# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 09:58:46 2020

@author: gunda
"""

class Solution:
    def evalRPN(self, tokens):
        stack = []
        operators = {'+': lambda x, y: x + y, 
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: x / y}
        
        for i in range(len(tokens)):
            while len(stack) > 1 and tokens[i] in operators:
                k = int(stack.pop())
                j = int(stack.pop())
                sub_total = operators[tokens[i]](j, k)
                stack.append(sub_total)
                print(stack)
                break
            if tokens[i] not in operators:
                stack.append(tokens[i])
        
        print (int(stack[-1]))
        return int(stack[-1])
    
solution = Solution()
solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])