"""
Determine whether an integer is a palindrome. Do this without extra space.
ome hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""
__author__ = 'Yang'


class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x == 0:
            return True
        elif x < 0:
            return False
        else:
            i = 1
            bits = 1
            while True:
                if x / i and x / (i * 10):
                    bits += 1
                    i *= 10
                elif x / i and not x / (i * 10):
                    break
            # print bits
            i = 1
            while i <= (bits >> 1):
                a = 10 ** (bits - 2 * i + 1)
                if x / a != x % 10:
                    return False
                else:
                    x = x % a
                    x = x / 10
                i += 1
            return True

    def method2(self, x):
        xRe = 0
        x1 = x
        if x == 0:
            return True
        elif x < 0:
            return False
        else:
            i = 1
            bits = 1
            while True:
                if x / i and x / (i * 10):
                    bits += 1
                    i *= 10
                elif x / i and not x / (i * 10):
                    break
            i = 1
            print bits
            while i <= bits >> 1:
                xRe = xRe * 10 + x % 10
                x  /= 10
                i += 1

            print x1 / (10 ** (bits - i + 1))
            return xRe == x1 / (10 ** (bits - i + 1))

    def method3(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            x1 = x
            xre = 0
            while x1:
                xre = xre * 10 + x1 % 10
                x1 /= 10

            return xre == x




if __name__ == "__main__":
    x = 243
    x1 = 343
    x2 = 2345678
    x3 = 23455432
    x4 = 1661441661
    x5 = 2147483647

    s =Solution()
    # print s.isPalindrome(x4)
    # print s.method2(1688448861)
    print s.method3(x4)