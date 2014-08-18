"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
__author__ = 'Yang'

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not word or len(board) * len(board[0][0]) < len(word):
            return False
        else:
            word = word.upper()
            stack = []
            for i in xrange(len(board)):
                for j in xrange(len(board[0])):
                    if board[i][j] == word[0]:
                        tempLocatedic = {}
                        stack.append([i, j])
                        k = 1
                        #判断该字母四周的字母是否为单词的下一个字母
                        while k < len(word):
                            temp = self.findLetter(board, stack[len(stack) - 1], word[k])
                            if temp:
                                tempLocatedic[k] = temp
                                for ele in temp:
                                    if ele not in stack:
                                        stack.append(ele)
                                        break







        def findLetter(self, board, point, cha):
            letterLocation = []
            if point[0] == 0:
                if point[1] > 0 and board[point[0]][point[1] - 1] == cha:
                    letterLocation.append([point[0], point[1] - 1])
                if point[1] < len(board[0]) - 1 and board[point[0]][point[1] + 1] == cha:
                    letterLocation.append([point[0], point[1] + 1])
                if len(board) > 1 and board[point[0] + 1][point[1]] == cha:
                    letterLocation.append([point[0] + 1, point[1]])

            elif 0 < point[0] < len(board) - 1:
                if board[point[0] - 1][point[1]] == cha:
                    letterLocation.append([point[0] - 1, point[1]])
                if board[point[0]][point[1] - 1] == cha:
                    letterLocation.append([point[0], point[1] - 1])
                if board[point[0]][point[1] + 1] == cha:
                    letterLocation.append([point[0], point[1] + 1])
                if board[point[0] + 1][point[1]] == cha:
                    letterLocation.append([point[0] + 1, point[1]])
            else:
                if point[1] > 0 and board[point[0]][point[1] - 1] == cha:
                    letterLocation.append([point[0], point[1] - 1])

                if point[1] < len(board[0]) - 1 and board[point[0]][point[1] + 1] == cha:
                    letterLocation.append([point[0], point[1] + 1])

                if len(board) > 1 and board[point[0] - 1][point[1]] == cha:
                    letterLocation.append([point[0] - 1, point[1]])
            return letterLocation


    # def find_around(self, board, point, cha):
    #     chas = []
    #     if point[0] - 1 >= 0:
    #         chas.append(board[point[0]-1][0][point[1]])
    #     if point[0] + 1 < len(board):
    #         chas.append(board[point[0]+1][0][point[1]])
    #         if point[1] -1 >= 0:
    #             chas.append(board[point[0][0][point[1]-1]])
    #     if point[1] + 1 < len(board[0][0]):
    #         chas.append(board[point[0][0][point[1]+1]])






