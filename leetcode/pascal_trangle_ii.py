#! -*- encoding: utf-8 -*-
"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution:
    def getRow(self, rowIndex):
        ans = [1]
        if not rowIndex:
            return ans
        elif rowIndex == 1:
            return [1, 1]
        else:
            ans = [1]

            for i in xrange(1, rowIndex):
                ans.append(ans[i-1] * (rowIndex-i+1)/i)

            ans.append(1)
            return ans

if __name__ == "__main__":
    s = Solution()
    print s.getRow(3)

