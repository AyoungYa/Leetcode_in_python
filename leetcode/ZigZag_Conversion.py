#! -*- coding: utf-8 -*-
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
__author__ = 'Yang'


class Solution:
    # @return a string
    def convert(self, s, nRows):
        k = 0
        state = 1
        i = 0
        dic = {}
        rs = ''
        if not s:
            return ""
        else:
            if  nRows in (1, 0) or nRows >= len(s) :
                return s
            elif 2 <= nRows < len(s):
                for n in xrange(nRows):
                    dic[n] = ''

                while(k < len(s) and s):
                    if i == nRows and state == 1:
                        state *= -1
                        i -= 1
                      
                    elif i == 0 and state == -1:
                        state *= -1
                        i += 1              
                      
                    elif state == 1 and i < nRows:
                        dic[i] += s[k]
                        i += 1  # 31
                        k += 1
                    elif state == -1 and i > 0:
                        i -= 1
                        dic[i] += s[k]
                        k += 1

                for n in xrange(nRows):
                    print dic[n]
                    rs += dic[n]

                return rs


if __name__  == "__main__":
    s = "twckwuyvbihajbmhmodminftgpdcbquupwflqfiunpuwtigfwjtgzzcfof\
         jpydjnzqysvgmiyifrrlwpwpyvqadefmvfshsrxsltbxbziiqbvosufqpw\
         sucyjyfbhauesgzvfdwnloojejdkzugsrksakzbrzxwudxpjaoyocpxhyc\
         rxwzrpllpwlsnkqlevjwejkfxmuwvsyopxpjmbuexfwksoywkhsqqevqtpoohpd"
    ss = ""
    sc = Solution()
    print sc.convert(s, 4)




