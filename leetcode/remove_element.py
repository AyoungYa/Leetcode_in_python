#! -*- encoding: utf-8 -*-
__author__ = 'Yang'

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        newlenght = len(A)
        while(A.count(elem)):
            A.remove(elem)
            newlenght -= 1
        return newlenght