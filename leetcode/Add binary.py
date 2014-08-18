"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""
__author__ = 'Yang'
from string import atoi

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        length_a = len(a)
        length_b = len(b)
        result = ""
        index = 1
        carry = 0

        while(index <= max(length_a, length_b)):
            if(index <= length_a): a_single = a[length_a-index]
            else: a_single = '0'

            if(index <= length_b): b_single = b[length_b-index]
            else: b_single = '0'

            added = atoi(a_single) + atoi(b_single) + carry

            if not added:
                single_result = 0
                carry = 0
            elif added == 1:
                single_result = 1
                carry = 0
            elif added == 2:
                single_result = 0
                carry = 1
            else:
                single_result = 1
                carry = 1
            index += 1
            str_single = "%i" % single_result
            result  = str_single + result
        if carry:
            # str_carry = "%i" % carry
            str_carry = str(carry)
        return str_carry + result

if __name__ == "__main__":
    s = Solution()
    a = "11"
    b = "1"
    print s.addBinary(a, b)
