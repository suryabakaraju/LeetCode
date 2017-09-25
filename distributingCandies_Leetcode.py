# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:14:06 2017

@author: surya
"""

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if len(candies)/2 < len(set(candies)):
            return len(candies)/2
            
        else:
            return len(set(candies))
            
        #print(len(can)/2 if len(can)/2<len(set(can)) else len(set(can)))
            