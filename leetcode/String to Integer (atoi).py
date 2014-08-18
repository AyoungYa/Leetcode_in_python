"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask
yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible
to gather all the input requirements up front.
"""
__author__ = 'Yang'

class Solution:
    # @return an integer
    def atoi(self, strs):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if strs.isspace():
            return 0
        else:
            strnospace = strs.strip()
            print strnospace

            begin = 1
            symbol = 1
            canUsech = ['+', '-'] + [str(c) for c in xrange(10)]
            dig = 0

            for i in xrange(len(strnospace)):
                if strnospace[i] not in canUsech:

                    break

                elif strnospace[i] in ('+', '-'):
                    if begin:
                        if strnospace[i] == '+':
                            begin = 0
                            continue
                        else:
                            begin = 0
                            symbol *= -1
                    else:
                        break
                else:
                    dig *= 10
                    dig += int(strnospace[i])
                    begin = 0

            return max(INT_MIN, min(symbol * dig, INT_MAX))

if __name__ == "__main__":
    strs = '+-2'
    strs1 = "2147483648"
    str2 = "  -0012a42"
    s = Solution()
    print s.atoi(str2)



