# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 01:13:38 2017

@author: surya
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves.count('U')-moves.count('D')==0 and moves.count('L')-moves.count('R')==0:
            return True
        else:
            return False
        