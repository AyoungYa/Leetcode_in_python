"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
__author__ = 'Yang'


class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if not n * k or n - k < 0:
            return []
        elif not n - k:
        return [[x for x in xrange(1, n + 1)]]
    else:
    queue = []
    for i in xrange(1, n - k + 2):
        queue.append([i])

    for i in xrange(2,  k + 1):
        while len(queue[0]) < i:
            temp = queue.pop(0)
            for m in xrange(temp[-1] + 1, n - k + i + 1):
                queue.append(temp + [m])

    return queue

if __name__ == "__main__":
    s = Solution()
    print s.combine(6, 3)