# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:14:06 2017

@author: surya
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        g=[]
        for i in list(s.split(' ')):
            g.append(i[::-1])
            #g.append(''.join(reversed(i)))
        return (' '.join(g))