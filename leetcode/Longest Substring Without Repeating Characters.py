"""
Given a string, find the length of the longest substring without repeating characters. For example,
the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.
"""
__author__ = 'Yang'

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 0:
            return len(s)
        else:
            dic = {}
            for i in xrange(len(s)):
                if s[i] not in dic:
                    dic[s[i]] = [i]
                else:
                    dic[s[i]].append(i)

            longest = 0
            st = 0
            for i in xrange(len(s)):
                if i == dic[s[i]][0]:
                    continue
                else:
                    nowIndex = dic[s[i]].index(i)
                    pre = dic[s[i]][nowIndex - 1]
                    if pre < st:
                        continue
                    else:
                        longest = max(longest, i - st)
                        st = pre + 1
            return max(longest, len(s) - st)


if __name__ == "__main__":
    s = "abcabcbb"
    s1 = 'fdjagkhjkdfg'
    sclass = Solution()
    print sclass.lengthOfLongestSubstring(s)

