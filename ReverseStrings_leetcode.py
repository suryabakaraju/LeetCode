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
        k=[]
        for i in list(s.split(' ')):
            for j in range(0,len(i)):
                g.insert(0,i[j])
            k.append(''.join(g))
            g=[]
        return (' '.join(k))
        