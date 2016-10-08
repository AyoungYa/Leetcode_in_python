#! /usr/bin/python
#! -*- encoding: utf-8 -*-
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Subscribe to see which companies asked this question

"""

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if len(num) <= 3:
            return sum(num)

        num.sort()
        min_sum = sum(num[0 : 3])
        min_diff = abs(min_sum - target)
        for i in range(0, len(num) - 2):
            cur = num[i]
            three_sum = self.twoSumClosest(num[i+1: len(num)], target - cur) + cur
            if min_diff > abs(three_sum - target):
                min_diff = abs(three_sum - target)
                min_sum = three_sum
        return min_sum



    # num为排序好的数组，从中去两个值加起来最接近target
    # 返回与目标值最近的两个数加和：a+b
    def twoSumClosest(self, num, target):
        if len(num) < 2:
            raise ValueError
        left_index = 0
        right_index = len(num) - 1
        sum_result = num[left_index] + num[right_index]
        min_distance = abs(sum_result - target)
        min_value = sum_result

        while left_index < right_index:
            sum_result = num[left_index] + num[right_index]
            difference = sum_result - target
            distance = abs(difference)
            if min_distance > distance:
                min_distance = distance
                min_value = sum_result

            # if min_distance == 0:
            #     return min_difference

            if difference > 0:
                right_index -= 1
            elif difference < 0:
                left_index += 1
            else:
                return  min_value

        return min_value


if __name__ == "__main__":
    a = [-1, 2, 1, -4]
    target = 1

    s = Solution()
    print s.threeSumClosest(a, target)