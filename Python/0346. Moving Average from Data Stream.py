# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 12:33:00 2020

@author: gunda
"""

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = []

    def next(self, val):
        self.queue.append(val)
        # Calculate the sum of the moving window
        window_sum = sum(self.queue[-self.size:])
        print(window_sum / min(len(self.queue), self.size))
        return window_sum / min(len(self.queue), self.size)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

obj = MovingAverage(3)
obj.next(1)
obj.next(10)
obj.next(3)
obj.next(5)
