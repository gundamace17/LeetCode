# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:16:39 2020

@author: gunda
"""

from collections import defaultdict
def topKFrequent(words, k):
    collection = defaultdict(int)
    
    for word in words:
        collection[word] += 1
        
    result = [[k, v] for k, v in collection.items()]
    result.sort()
    result.sort(key = lambda x: x[1], reverse = True)
    
    print([item[0] for item in result][:k])    
    return [item[0] for item in result][:k]

# Algorithm:
# 1. Create a defaultdict for counting elements in the list
# 2. Take each key, value pair into result list[list[k, v]] 
# 3. Sort the result for the alphabetical order
# 4. Sort by the numbers of the key in reverse order

topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
