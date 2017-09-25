# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 02:41:17 2017

@author: surya
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num^((2**len(bin(num)[2:]))-1)
        