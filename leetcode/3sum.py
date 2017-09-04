"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note:
    1.Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
    2.The solution set must not contain duplicate triplets.

For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
__author__ = "Yang"

import time

#博士
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        numset = list(set(num))
        numset.sort()
        result = []
        numtimes = {}
        twosum = {}
        for i in numset:
            numtimes[i] = num.count(i)
        for i in range(len(numset)):
            if numtimes[numset[i]] > 1 and numset[i] + numset[i] >= 0:
                twosum.setdefault(numset[i] + numset[i], []).append([numset[i], numset[i]])
            for j in range(i + 1, len(numset)):
                if numset[i] + numset[j] >= 0:
                    twosum.setdefault(numset[i] + numset[j], []).append([numset[i], numset[j]])
        for i in numset:
            if i <= 0:
                if -i in twosum:
                    templist = twosum[-i]
                    for tl in templist[::-1]:
                        if i <= tl[0] and tl[0] <= tl[1]:
                            r = [i, tl[0], tl[1]]
                            t1 = r.count(i)
                            t2 = r.count(tl[0])
                            t3 = r.count(tl[1])
                            if numtimes[i] >= t1 and numtimes[tl[0]] >= t2 and numtimes[tl[1]] >= t3:
                                result.append(r)
                        elif tl[0] < i:
                            break
        return result

#网上
class Solution1:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        res = []
        sortnum = sorted(num)
        length = len(sortnum)
        # make sure a < b < c
        for i in xrange(length-2):
            a = sortnum[i]
            # remove duplicate a
            if i >= 1 and a == sortnum[i-1]:
                continue
            j = i + 1
            k = length - 1
            while j < k:
                b = sortnum[j]
                c = sortnum[k]
                if b + c == -a:
                    res.append([a,b,c])
                    # remove duplicate b,c
                    while j < k:
                        j += 1
                        k -= 1
                        if sortnum[j] != b or sortnum[k] != c:
                            break
                elif b + c > -a:
                    # remove duplicate c
                    while j < k:
                        k -= 1
                        if sortnum[k] != c:
                            break
                else:
                    # remove duplicate b
                    while j < k:
                        j += 1
                        if sortnum[j] != b:
                            break
        return res

#我
class Solution2:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        length = len(num)
        if length < 3:
            return []
        elif length == 3:
            if not sum(num): return [sorted(num)]
            else: return  []

        num.sort()
        result = []
        index = 0
        while(index <= length-3 and num[index] <= 0):
            c = num.count(num[index])
            # result.extend(self.twoSum(num[index+1: ], num[index]))
            noAnds = -num[index]
            indexlow = index + c - 2
            indexhig = length - 1
            while indexlow < indexhig:
                low = num[indexlow]
                high = num[indexhig]
                a = low + high
                if a == noAnds:
                    result.append([num[index], low, high])
                    while indexlow < indexhig:
                        indexlow += 1
                        indexhig -= 1
                        if num[indexlow] != low or num[indexhig] != high:
                            break
                elif a < noAnds:
                    while indexlow < indexhig:
                        indexlow += 1
                        if num[indexlow] != low:
                            break
                elif a > noAnds:
                    while indexlow < indexhig:
                        indexhig -= 1
                        if num[indexhig] != high:
                            break
            index += c
        return result



if __name__ == "__main__":
    num = [-1, 0, 1, 2, -1, -4]
    num1 = [0, 0, 0]
    num2 = [0,7,-4,-7,0,14,-6,-4,-12,11,4,9,7,4,-10,8,10,5,4,14,6,0,-9,5,6,6,-11,1,-8,-1,2,-1,13,5,-1,-2,4,9,9,-1,-3,-1,-7,11,10,-2,-4,5,10,-15,-4,-6,-8,2,14,13,-7,11,-9,-8,-13,0,-1,-15,-10,13,-2,1,-1,-15,7,3,-9,7,-1,-14,-10,2,6,8,-6,-12,-13,1,-3,8,-9,-2,4,-2,-3,6,5,11,6,11,10,12,-11,-14]
    num3 = [9,14,0,-8,10,0,2,9,-8,13,-3,1,10,-13,4,3,-3,-11,8,-13,-4,-6,5,-10,-14,0,3,-9,-9,-7,-11,8,-8,-4,-15,9,11,3,3,-11,-7,7,5,-12,1,-14,-1,13,-9,-8,7,2,-6,-11,-1,-5,-4,-13,-7,2,-13,-2,-5,-6,9,-12,10,-2,-2,-10,2,6,4,14,2,-10,-15,-14,10,-9,-15,-6,0,-6,-2,14,-3,9,8,-3,-12,10,2,-9,11,-3,-6,-2,10,7,3,-11,-10,-8,-12,-1]
    num4 = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]

    start_time = time.clock()
    s = Solution()
    # b = s.threeSum(num3)
    for i in xrange(1):
        a = s.threeSum(num4)
    end_time = time.clock()
    print a
    print end_time - start_time
