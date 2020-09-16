# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 20:24:16 2020

@author: gunda
"""

def removeNthFromEnd(head, n):
    first = second = head
    first = first.next
    
    for i in range(n):
        second = second.next
    
    while second.next != None:
        second = second.next
        first = first.next
        
    return head
        