#! --encoding: utf-8 --
"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""
__author__ = 'Yang'

import copy

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        maxPoint = 0        #返回某条直线能穿过的最多点的个数
        cannotUsePoints = {} #已经组成过直线的点
        points = list(points)
        length = len(points)
        if length <= 2:
            return length
        else:
            for point in points:
                allVector = []
                stacVector = {}
                canUsePoint = []
                #求取尚未与point组成直线的点，结果存在canUsePoints中
                canUsePoint = copy.deepcopy(points)
                for pli in cannotUsePoints.values():
                    if point in pli:
                        canUsePoint = list(set(canUsePoint).difference(set(cannotUsePoints)))
                    #对上步得到的点进行向量的计算，并存在allVector中，中间的每一个元素对应于canUsePoints中的
                #每一个元素与最后一个元素的向量
                if len(canUsePoint) <= 2:
                    return max(maxPoint, len(canUsePoint))
                else:
                    for anpoint in canUsePoint:
                        allVector.append(self.getVector(point, anpoint))
                    #统计allVector中大小相同的向量的个数，结果存在stacVector中，并保存在cannotUsePoints中，
                #返回最大值maxPoint
                for i in range(len(allVector)):
                    if allVector[i] in stacVector.keys():
                        stacVector[allVector[i]].append(canUsePoint[i])
                    else:
                        stacVector[allVector[i]] = [point, canUsePoint[i]]
                    maxPoint = max(maxPoint, len(stacVector[allVector[i]]))
                cannotUsePoints[point] = stacVector.values()
            return maxPoint

    def getVector(self, a, b):
        pa = Point(a[0], a[1])
        pb = Point(b[0], b[1])
        xV = pb.x - pa.x
        yV = pb.y - pa.y
        if xV == 0 and yV != 0:
            vec = (0, 1)
        elif xV == 0 and yV == 0:
            vec = (0, 0)
        else:
            vec = (1, float(yV)/xV)

        return vec


    def maxPoints2(self, points):
        numbers = {}
        maxp = 2

        if len(points) <= maxp:
            return len(points)

        for ele in points:
            if ele not in numbers.keys():
                numbers[ele] = points.count(ele)

        pointsset = list(set(points))
        length = len(pointsset)

        for i in xrange(length - 1):
            if length - i <= maxp:
                return maxp
            else:
                vecs = {}
                for j in xrange(i + 1, length):
                    vec = self.getVector(pointsset[i], pointsset[j])
                    if vec not in vecs:
                        vecs[vec] = 1 * numbers[pointsset[j]]
                    else:
                        vecs[vec] += 1 * numbers[pointsset[j]]
                tempmax = max(list(vecs.itervalues())) + 1
                maxp = max(maxp, tempmax * numbers[pointsset[i]])
        return maxp
























        # noNeed = []
        # maxs = 2
        # number = len(points)
        # if number <= 2:
        #     return number
        #
        # else:
        #     for i in xrange(number - 1):
        #         if points[i] in noNeed:
        #             continue
        #         else:
        #             if number - i <= maxs:
        #                 return maxs
        #
        #             else:
        #                 vecs = []
        #                 for j in xrange(i + 1, number):
        #                     vecs.append(self.getVector(points[i], points[j]))
        #                 vecs = sorted(vecs)
        #                 times = vecs.count((0, 0))
        #                 if times:
        #                     noNeed.append(points[i])
        #
        #                 amax = atimes = 1
        #                 for k in xrange(len(vecs) - 1):
        #                     if vecs[k] == vecs[k + 1] and vecs[k] != (0, 0):
        #                         atimes += 1
        #                     else:
        #                         amax = max(atimes, amax)
        #                         atimes = 1
        #                 maxs = max(maxs, (times + 1) * (max(amax, atimes) + 1))
        #     return maxs













if __name__ == "__main__":

    A = [(-54, -297), (-36, -222), (3, -2), (30, 53), (-5, 1), (-36, -222), (0, 2), (1, 3), (6, -47),
         (0, 4), (2, 3), (5, 0), (48, 128), (24, 28), (0, -5), (48, 128), (-12, -122), (-54, -297),
         (-42, -247), (-5, 0), (2, 4), (0, 0), (54, 153), (-30, -197), (4, 5), (4, 3), (-42, -247),
         (6, -47), (-60, -322), (-4, -2), (-18, -147), (6, -47), (60, 178), (30, 53), (-5, 3),
         (-42, -247), (2, -2), (12, -22), (24, 28), (0, -72), (3, -4), (-60, -322), (48, 128),
         (0, -72), (-5, 3), (5, 5), (-24, -172), (-48, -272), (36, 78), (-3, 3)]
    A1 = [(0, 0), (-1, -1), (2, 2)]
    A2 = [(0, 0), (-1, -1), (0, 0)]

    s = Solution()
    print s.maxPoints2(A2)