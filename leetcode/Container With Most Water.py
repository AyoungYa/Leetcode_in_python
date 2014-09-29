"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two
lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""
__author__ = 'Yang'

class Solution:
    # @return an integer
    def maxArea(self, height):
        length = len(height)
        if length <= 1:
            return 0
        elif length == 2:
            return min(height)
        else:
            ma = max(height)
            maIndex = height.index(ma)
            if maIndex == 0:
                height.reverse()
                return self.area(height)
            elif maIndex == length - 1:
                return self.area(height)
            else:
                prePart = height[: maIndex + 1]
                nextPart = height[maIndex: ]
                nextPart.reverse()
                print 'Area Left----', self.area(prePart)
                print 'Area Rigth---', self.area(nextPart)
                print 'Total--------', self.special(height)
                return max(self.area(prePart), self.area(nextPart), self.special(height))

    # @height's max is the last one
    # @return an integer
    def area(self, height):
        length = len(height)
        if length <= 1:
            return 0
        else:
            heist = height[0]
            result = min(heist, height[-1]) * (length - 1)
            for i in xrange(length):
                if height[i] < heist:
                    continue
                else:
                    heist = height[i]
                    result = max(result, min(heist, height[-1]) * (length - i - 1))
            return result


    def special(self, height):
        result = 0
        length = len(height)
        if length >= 2:
            i = 0; j = length - 1
            left = height[0]
            right = height[-1]
            result = min(right, left) * (j - i)
            while i < j:
                if left < right:
                    if height[i] > left:
                        left = height[i]
                        tempArea = min(right, left) * (j - i)
                        result = max(result, tempArea)
                    else:
                        while height[i] <= left and i < length:
                            i += 1

                else:
                    if height[j] > right:
                        right = height[j]
                        tempArea = min(right, left) * (j - i)
                        result = max(result, tempArea)
                    else:
                        while height[j] <= right and j >= 0:
                            j -= 1
        return result



if __name__ == "__main__":
    a = [1, 2, 4, 6, 5, 4]
    a2 = [2, 3, 10, 5, 7, 8, 9]
    a3 = [75,21,3,152,13,107,163,166,32,160,41,131,7,67,56,5,153,176,29,139,61,149,176,142,64,75,170,156,73,48,148,101,70,103,53,83,11,168,1,195,81,43,126,88,62,134,45,167,63,26,107,124,128,83,67,192,158,189,149,184,37,49,85,107,152,90,143,115,58,144,62,139,139,189,180,153,75,177,121,138,4,28,15,132,63,82,124,174,23,25,110,60,74,147,120,179,37,63,94,47]
    a4 = [159,157,139,51,98,71,4,125,48,125,64,4,105,79,136,169,113,13,95,88,190,5,148,17,152,20,196,141,35,42,188,147,199,127,198,49,150,154,175,199,80,191,3,137,22,92,58,87,57,153,175,199,110,75,16,62,96,12,3,83,55,144,30,6,23,28,56,174,183,183,173,15,126,128,104,148,172,163,35,181,68,162,181,179,37,197,193,85,10,197,169,17,141,199,175,164,180,183,90,115]

    s = Solution()
    print s.maxArea(a4)
