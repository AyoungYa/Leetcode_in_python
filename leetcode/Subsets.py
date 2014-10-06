"""
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
__author__ = 'Yang'


class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        result = [[]]
        if not S:
            return result
        else:
            S = sorted(list(set(S)))
            pre = []
            for ele in S:
                result.append([ele])
                pre.append([ele])

            length = len(S)
            for eleResult in result:
                if eleResult:
                    temp = []
                    for e in eleResult:
                        temp.append(e)

                    if len(temp) < length:
                        lastEleIndex = S.index(temp[-1])
                        while lastEleIndex < length - 1:
                            result.append(temp + [S[lastEleIndex + 1]])
                            lastEleIndex += 1
            return result

    # def times(self, n, k):
    #     temp1 = temp2 = 1
    #     result = 1
    #     if not k or n < k:
    #         pass
    #     else:
    #         if n:
    #             i = 0
    #             if k > n / 2:
    #                 k = n - k
    #
    #             while i < k:
    #                 temp1 *= (n - i)
    #                 temp2 *= (k - i)
    #                 i += 1
    #             result = temp1 / temp2
    #         else:
    #             result = 0
    #
    #     return result


if __name__ == "__main__":
    sc = Solution()
    s = [1, 2, 3, 4]
    print sc.subsets(s)