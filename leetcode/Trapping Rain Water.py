"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""
__author__ = 'Yang'
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        length = len(A)

        if length <= 2:
            return 0
        else:
            maxValueIndex = A.index(max(A))
            if maxValueIndex == 0:
                A.reverse()
                return self.trapLast(A)
            elif maxValueIndex == length - 1:
                return self.trapLast(A)
            else:
                A1 = A[0: maxValueIndex + 1]
                A2 = A[maxValueIndex: length]
                A2.reverse()
                return self.trapLast(A1) + self.trapLast(A2)

    # @param A, the last element of A, is the biggest
    # @return an integer
    def trapLast(self, A):
        length = len(A)
        if length <= 2:
            return 0
        else:
            stack = []
            water = 0
            for ele in A:
                if not stack:
                    stack.append(ele)
                elif len(stack) == 1:
                    if ele >= stack[0]:
                        stack[0] = ele
                    else:
                        stack.append(ele)
                else:
                    if ele < stack[0]:
                        stack.append(ele)
                    else:
                        miniboard = stack.pop(0)
                        while stack:
                            water += miniboard - stack.pop()
                        stack = [ele]
            return water




if __name__ == "__main__":
    A = [0,1,0,2,1,0,1,3,2,1,2,1]
    A1 = [2, 0, 2]
    s = Solution()
    # print s.trap(A1)
    print s.trapLast(A1)
    # print s.trapLast([1, 2, 1, 2, 3])
    # print s.trap([0, 1, 0, 2, 1, 0, 3])

