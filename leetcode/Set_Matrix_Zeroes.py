"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
__author__ = 'Yang'

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        col = len(matrix[0])
        zeroC = []
        for ele in matrix:
            if 0 in ele:
                while 0 in ele:
                    zIndex = ele.index(0)
                    zeroC.append(zIndex)
                    ele[zIndex] = 1
                matrix[matrix.index(ele)] = [0] * col
            else:
                continue

        zeroC = sorted(set(zeroC))
        for i in xrange(len(matrix)):
            if matrix[i] != [0] * col:
                for j in zeroC:
                    matrix[i][j] = 0


if __name__ == "__main__":
    ma = [[1]]
    s = Solution()
    s.setZeroes(ma)
    print ma



