#! -*-encoding: utf-8 -*-
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?
"""

__author__ = 'Yang'


class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        #满足Fibonacci数列的规则，可直接利用Fibonacci完成。
       if n < 2:
            return 1
        else:
            answer = 0
            beforeOne = beforeTwo = 1
            for i in xrange(2, n + 1):
                answer = beforeOne + beforeTwo
                beforeTwo = beforeOne
                beforeOne = answer
            return answer

if __name__ == "__main__":
    s = Solution()
    print s.climbStairs(3)
