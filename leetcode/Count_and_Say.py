#! -*- coding: utf-8 -*-
"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""
__author__ = 'Yang'

class Solution:
    # @return a string
    def countAndSay(self, n):
        result = '1'
        if not n:
            return ''
        else:
            while n - 1:
                result = self.doOnce(result)
                n -= 1
            return result

    def doOnce(self, nstr):
        result = ''
        if not nstr:
            return ''
        else:
            element = ''
            times = 0
            for ele in nstr:
                if not element:
                    element = ele
                    times = 1
                elif element == ele:
                    times += 1
                else:
                    result += str(times) + element
                    element = ele
                    times = 1
            if element:
                result += str(times) + element
            return result


if __name__ == "__main__":
    n = 1
    s = Solution()

    print s.countAndSay(n)