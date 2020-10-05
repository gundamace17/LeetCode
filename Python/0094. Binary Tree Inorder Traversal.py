# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:38:16 2020

@author: gunda
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        
        orderedList = []
        stack = [root]
        
        while stack:
            top = stack[-1]
            if top.left:
                stack.append(top.left)
                top.left = None
                continue
            else:
                orderedList.append(top.val)
                stack.pop()
                
            if top.right:
                stack.append(top.right)
                top.right = None
        return orderedList
