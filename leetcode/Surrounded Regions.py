#! -*- encoding: utf-8 -*-
"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""
__author__ = 'Yang'


class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        row = len(board) #行
        column = len(board[0]) #列

        notFlip = []
        if row >2 and column > 2:
            for i in xrange(column):
                if board[0][i] == 'O':
                    notFlip.append([0, i])
                if board[row-1][i] == 'O':
                    notFlip.append([row-1, i])

            for i in xrange(row):
                if board[i][0] == 'O':
                    notFlip.append([i, 0])
                if board[i][column-1] == 'O':
                    notFlip.append([i, column-1])
            print 'bianjiedian', notFlip

            for ele in notFlip:
                for surrond in self.surrondPoints(board, ele):
                    if board[surrond[0]][surrond[1]] == 'O' and surrond not in notFlip:
                        notFlip.append(surrond)

            for i in xrange(len(board)):
                for j in xrange(len(board[0])):
                    if board[i][j] == 'O' and [i, j] not in notFlip:
                        board[i].replace(board[i][j], 'X')

    # @param board, a 2D array
    # @point, a point in board
    # return a list of points surrond point
    def surrondPoints(self, board, point):
        minusRow = point[0] - 1
        addRow = point[0] + 1
        minusColumn = point[1] - 1
        addColumn = point[1] + 1
        sur = []
        if 0 <= minusRow:
            sur.append([minusRow, point[1]])
        if addRow < len(board[0]):
            sur.append([addRow, point[1]])
        if 0 <= minusColumn:
            sur.append([point[0], minusColumn])
        if addColumn < len(board[0]):
            sur.append([point[0], addColumn])
        print point, 'surrondpoints :--', sur
        return sur


if __name__ == '__main__':
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    board2 = [
        ['X', 'X'],
        ['X', 'O']
    ]
    board3 = ["XXXXXXXOX","XXXXXXOXX","XXXXXXXXX","XXXXXXOXX","XXOXXXOXX","XXXOXXXXX","XXXXXXXXX","XXXXXXXXX","XOXXXXOXO"]

    # p = [1, 2]
    # a = s.surrondPoints(board, p)
    s = Solution()
    s.solve(board3)

    for i in xrange(len(board3)):
        s = ''
        for e in board3[i]:
            s += e + '  '
        s += '\r\t'
        print s
        
