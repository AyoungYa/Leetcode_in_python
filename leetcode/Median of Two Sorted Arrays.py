#! encoding: utf-8
"""
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""
__author__ = 'Yang'

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        C = [0] * ((m + n) / 2 + 1)
        tx = (m + n) / 2

        # 如果（m + n）为奇数，则只要查找第tx + 1个数即可，如果(m + n)为偶数,则要查找tx, tx + 1这两个元素
        i = j = th = 0
        while th < tx + 1:
            if i < m and j < n:
                if A[i] <= B[j]:
                    C[th] = A[i]
                    th += 1
                    i += 1
                else:
                    C[th] = B[j]
                    th += 1
                    j += 1
            elif i < m and j >= n:
                C[th] = A[i]
                th += 1
                i += 1
            else:
                C[th] = B[j]
                th += 1
                j += 1

        if (m + n) % 2:
            return C[-1]
        else:
            return (C[-1] + C[-2]) / 2.0


if __name__ == "__main__":
    A = [1, 3, 5, 7, 8]
    B = [2, 3, 4, 6, 9]
    s = Solution()
    print s.findMedianSortedArrays(A, A)
