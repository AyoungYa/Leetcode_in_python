"""
Given an unsorted array of integers, find the length of the longest
consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
__author__ = 'Yang'

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num = sorted(list(set(num)))
        print num
        longth = longest = 1
        if len(num) <= 1:
            return len(num)

        else:
            for i in xrange(len(num) - 1):
                if num[i] + 1 == num[i + 1]:
                    longth += 1

                else:
                    longest = max(longest, longth)
                    longth = 1
            return max(longest, longth)

if __name__ == "__main__":
    num = [100, 4, 200, 1, 3, 2]
    num1 = [0, -1]
    num2 = [0, 0]
    s = Solution()
    print s.longestConsecutive(num2)

