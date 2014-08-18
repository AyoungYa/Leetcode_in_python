"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""
__author__ = 'Yang'

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        if not digits:
            return [1]
        elif len(digits) == 1:
            if digits[0] + 1 == 10:
                return [1, 0]
            else:
                return [digits[0] + 1]
        else:
            last = digits[-1] + 1
            if last == 10:
                digits[-1] = 0
                carry = 1
            else:
                digits[-1] = last
                carry = 0

            for i in xrange(len(digits) - 2, 0, -1):
                last = digits[i] + carry
                if last == 10:
                    digits[i] = 0
                    carry = 1
                else:
                    carry = 0
                    digits[i] = last

            last = digits[0] + carry
            if last == 10:
                digits[0] = 0
                digits.insert(0, 1)
            else:
                digits[0] = last
            return digits

if __name__ == "__main__":
    digits = [9, 9, 9]
    dig = [9]
    s = Solution()
    print s.plusOne(dig)

