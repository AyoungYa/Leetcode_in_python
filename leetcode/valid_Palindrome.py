#! -*- encoding: utf-8 -*-
__author__ = 'Yang'

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        judge = True
        ss = s.lower()
        front = 0
        back = len(ss) - 1
        if not s:
            judge = False
        else:
            while(front <= back):
                if self.isNumorChar(ss[front]) and self.isNumorChar(ss[back]):
                    if ss[front] == ss[back]:
                        front += 1
                        back -= 1
                        judge = True
                    else:
                        judge = False
                        return judge
                elif self.isNumorChar(ss[front]) and (not self.isNumorChar(ss[back])):
                    back -= 1
                elif (not self.isNumorChar(ss[front])) and self.isNumorChar(ss[back]):
                    front += 1
                else:
                    front += 1
                    back -= 1
        return  judge

    def isNumorChar(self, s):
        s_ascii = ord(s)
        judge = False
        if s_ascii in xrange(48, 58) or s_ascii in xrange(97, 123):
            judge = True
        else:
            judge = False
        return judge


if __name__ == "__main__":
    strs = "A man, a plan, a canal: Panama"
    strs2 = "race a car"
    s = Solution()
    print s.isPalindrome(strs)


