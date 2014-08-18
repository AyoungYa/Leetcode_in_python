#! encoding: utf-8
"""
Given n non-negative integers representing the histogram's bar height where the
width of each bar is 1, find the area of largest rectangle in the histogram.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""
__author__ = 'Yang'
import time
import sys
sys.setrecursionlimit(100000)

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height): #递归实现
        length = len(height)
        if length == 0: return 0
        elif length == 1: return height[0]
        elif length == 2: return max(min(height) * 2, max(height))
        else:
            mini = min(height)
            miniIndex = height.index(mini)
            area = mini * length
            leftArea = self.largestRectangleArea(height[: miniIndex])
            rightArea = self.largestRectangleArea(height[miniIndex + 1: ])
            return max(area, leftArea, rightArea)

    def noRecursion(self, height):
        length = len(height)
        if length == 0: return 0
        elif length == 1: return height[0]
        elif length == 2: return max(min(height) * 2, max(height))
        else:
            mini = min(height)
            maxArea = max(mini * length, max(height))
            queue = [[0, length]]
            while queue:
                ele = queue[0]
                left =ele[0]
                right = ele[1]

                if left < right - 1:
                    minValue = min(height[left: right])
                    if mini == minValue:
                        continue
                    else:
                        minIndex = height[left: right].index(minValue) + left
                        if (minIndex - left) in (0, 1):
                            maxArea = max(maxArea, minValue * (right - left), height[left])
                        else:
                            maxArea = max(maxArea, minValue * (right - left))
                            queue.append([left, minIndex])
                        queue.append([minIndex + 1, right])

                elif left == right - 1:
                    maxArea = max(maxArea, height[left])

                queue.remove(ele)

            return maxArea



    def largestRectangleAreaNoRecursion(self, height):
        length = len(height)
        if length == 0: return 0
        elif length == 1: return height[0]
        elif length == 2: return max(min(height) * 2, max(height))
        else:
            mini = min(height)
            maxArea = max(mini * length, max(height))

            for i in xrange(length):
                p = height[i]
                if p > mini:
                    times = -1
                    u = d = i
                    while d >= 0 :
                        if height[d] >= p:
                            d -= 1
                            times += 1
                        else:
                            break
                    while u < length:
                        if height[u] >= p:
                            u += 1
                            times += 1
                        else: break
                    maxArea = max(maxArea, p * times)

            return maxArea


    def largestRectangleAreaNoRecursion1(self, height):
        area = 0
        stack = []
        length = len(height)
        if length == 0: return 0
        elif length == 1: return height[0]
        elif length == 2: return max(min(height) * 2, max(height))
        else:
            i = 0
            while i < length:
                if not stack or height[stack[len(stack) - 1]] < height[i]:
                    stack.append(i)
                    i += 1
                else:
                    start = stack.pop()
                    if not stack:
                        width = i
                    else:
                        width = i - stack[len(stack) - 1] - 1
                    area = max(area, height[start] * width)

            while stack:
                start = stack.pop()
                if stack:
                    width = length - stack[len(stack) - 1] - 1
                else:
                    width = length
                area = max(area, height[start] * width)

        return area




if __name__ == "__main__":
    height = [2, 1, 5, 6, 2, 3]
    height1 = [i for i in xrange(8893)]
    height3 = [1] * 30000
    s = Solution()
    sttime = time.clock()
    # print s.largestRectangleArea(height3)
    print s.largestRectangleAreaNoRecursion1(height3)
    # print s.noRecursion(height3)
    entime = time.clock()
    print entime - sttime

