# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:04:09 2020

@author: gunda
"""

class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        
        def helper():
            multi = 0
            sub = []
            while self.i < len(s):
                char = s[self.i]
                self.i += 1
                
                if char.isdigit():
                    multi = multi*10 + int(char)
                   
                elif char == '[':      
                    sub += multi * helper()
                    multi = 0
                    
                elif char == ']':
                    return sub
                
                else:
                    sub.append(char)
                print(multi)
                print(sub)
            
            return "".join(sub)
        return helper()
    
solution = Solution()
solution.decodeString("3[a2[bc]]")