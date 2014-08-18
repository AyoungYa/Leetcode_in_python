"""
Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
    1 All numbers (including target) will be positive integers.
    2 Elements in a combination(a1, a2, ..., ak)must be in non-descending order.
    3 The solution set must not contain duplicate combinations.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
"""
__author__ = 'Yang'

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        result = []
        if not candidates:
            return []
        else:
            if target in candidates:
                result.append([target])
                times = candidates.index(target)
            else:
                for ele in candidates[::-1]:
                    if ele < candidates:
                        times = candidates.index(ele) + 1
                        break

            while times: # times = len(candidates[: x] where candidates[x] >= target and candidates[x - 1] < x
                stack = [candidates[times - 1]]
                temp = target - candidates[times - 1]
                i = times
                while min(candidates) <= temp:
                    temp -= candidates[i -1]
                    stack.append(candidates[i - 1])

                    if temp == 0:
                        # stack.append(candidates[i])
                        result.append(sorted(stack))
                        i -= 1
                        stack = [candidates[i - 1]]

                    elif 0 < temp < min(candidates):
                        i -= 1
                        temp += stack.pop()

                    else:
                        continue
                times -= 1

            return result


    def combinationInteration(self, candidates, target):
        candidates = sorted(candidates)
        result = []
        if not candidates:
            return []
        elif len(candidates) == 1:
            if candidates[0] == target:
                return [target]
            else:
                return []

        else:
            if target in candidates:
                times = candidates.index(target)
                result.append([target])
                result.append(self.combinationInteration(candidates[: candidates.index(target)],
                                                         target))
            elif target < min(candidates):
                return []

            else:
                result.append([candidates[-1]])
                result.append(self.combinationInteration(candidates, target - candidates[-1]))

            return result

    # def method(self, candidates, target):
    #     result = []
    #     if not candidates:
    #         return result
    #     elif len(candidates) == 1:
    #         if candidates[0] > target:
    #             return result
    #         else:
    def nightWrite(self, candidates, target):
        candidates = sorted(candidates, reverse = True)
        result = []
        i = 0
        if target in candidates:
            result.append([target])
            candidates = candidates[candidates.index(target) + 1: ]

        while i < len(candidates):
            stack = [candidates[i]]
            j = i
            tar = target - candidates[i]

            while j < len(candidates):
                if tar - candidates[j] == 0:
                    stack.append(candidates[j])
                    result.append(sorted(stack))
                    stack = [candidates[i]]
                    j += 1
                elif tar - candidates[j] > 0:
                    stack.append(candidates[j])
                    tar -= candidates[j]
                else:
                    if j + 1 < len(candidates):
                        j += 1
                    else:
                        temp = stack.pop()
                        if not stack:
                            break
                        else:
                            tar += temp
                            tempIndex = candidates.index(temp)
                            if tempIndex < len(candidates) - 1:
                                stack.append(candidates[tempIndex + 1])
                                j = tempIndex + 1
                                tar -= candidates[tempIndex + 1]
                            else:
                                break

            i += 1

        return result



if __name__ == "__main__":
    candidates = [2, 3, 6, 7, 8]
    can = [1, 2]
    can1 = [2, 3, 7]
    s = Solution()
    # print s.nightWrite(candidates, 8)
    # print s.nightWrite(can, 4)
    print s.nightWrite(can1, 18)










