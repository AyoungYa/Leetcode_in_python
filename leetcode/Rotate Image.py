"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
__author__ = 'Yang'

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        print 'function running'
        return self.rotateFunction(matrix)


    def rotateFunction(self, matrix, m = 0): # m means have rotated circles
        n = len(matrix)
        for m in xrange(n / 2):
            if n-2*m <= 1:
                return matrix
            else:

                for i in xrange(m, n - 1 - m):
                    temp = matrix[m][i]
                    matrix[m][i] = matrix[n - i - 1][m]
                    matrix[n - i - 1][m] = matrix[n - 1 - m][n - 1 - i]
                    matrix[n - 1 - m][n - 1 - i] = matrix[i][n - 1 - m]
                    matrix[i][n - 1 - m] = temp
        return matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    matrix5 = [[1,  2,  3,  4,  5],
               [6,  7,  8,  9,  10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]
    for ele in matrix5:
        print ele
    s = Solution()
    for ele in s.rotate(matrix5):
        print ele
