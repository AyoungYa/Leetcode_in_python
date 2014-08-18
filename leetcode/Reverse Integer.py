"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
Have you thought about this?

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of
1000000003 overflows. How should you handle such cases?

Throw an exception? Good, but what if throwing an exception is not an option? You would then have to re-design the
function (ie, add an extra parameter).
"""
__Author__ = 'Yang'


class Solution:
    # @return an integer
    def reverseInteger(self, x):
        pone = ''
        stack = ''
        if x == 0:
            return 0
        elif x < 0:
            pone = '-'
            astr = list(str(x)[1: ])
        else:
            astr = list(str(x))

        while astr:
                stack += astr.pop()
        if pone:
            return -1 * int(stack)
        else:
            return int(stack)

if __name__ == '__main__':
    A = 123
    s = Solution()
    print s.reverseInteger(A)

