# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 13:46:50 2017

@author: surya
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        g=[]
        for i in range(0,len(words)):
            if set(words[i]).intersection(set("qwertyuiopQWERTYUIOP")) == set(words[i]) or set(words[i]).intersection(set("asdfghjklASDFGHJKL")) ==set(words[i]) or   set(words[i]).intersection(set("zxcvbnmZXCVBNM")) == set(words[i]):
                g.append(words[i])
        return g
        