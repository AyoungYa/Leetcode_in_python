"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
__author__ = 'Yang'


class Solution:
    # @return an integer
    def romanToInt(self, s):
        s = list(s)
        inList = []
        for ele in s:
            inList.append(self.change(ele))

        if len(inList) == 1:
            return inList[0]
        elif len(inList) == 0:
            return 0

        result = 0
        i = 1
        t = 0
        while i < len(inList):
            if inList[i - 1] >= inList[i]:
                result += inList[i - 1]
                i += 1

            else:
                result += inList[i] - inList[i - 1]
                i += 2

        if inList[-1] <= inList[-2]:
            return result + inList[-1]
        return result






    def change(self, cha):
        result = 0
        if cha == 'I':      result = 1
        elif cha == 'V':    result = 5
        elif cha == 'X':    result = 10
        elif cha == 'L':    result = 50
        elif cha == 'C':    result = 100
        elif cha == 'D':    result = 500
        elif cha == 'M':    result = 1000
        else:               result = 0

        return result


if __name__ == "__main__":
    a = "MCMXCVI"
    b = "MDCXCV"
    s = Solution()
    print s.romanToInt(a)