"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock
before you buy again).
"""

__author__ = 'Yang'

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profitNeibor = []
        if len(prices) <= 1:
            return 0
        else:
            for i in xrange(len(prices) - 1):
                profitNeibor.append(prices[i + 1] - prices[i])

            ma = max(profitNeibor)
            mi = min(profitNeibor)
            if ma <= 0:
                return 0
            elif mi >= 0:
                return sum(profitNeibor)
            else: # ma >=0 and mi <= 0
                proPoNe = self.poNe(profitNeibor)
                maOnce = self.maxpro(proPoNe)

                return max(maOnce, self.twiceProfit(proPoNe))



    # put the profitNeibor to like [+ - + - + - +]
    def poNe(self, profitNeibor):
        if not len(profitNeibor):
            return []
        else:
            poned = []
            while profitNeibor:
                if profitNeibor[0] <= 0:
                    profitNeibor.remove(profitNeibor[0])
                elif profitNeibor[-1] <= 0:
                    profitNeibor.pop()
                else:
                    break

            temp = profitNeibor[0]
            for i in xrange(len(profitNeibor) - 1):
                if profitNeibor[i] * profitNeibor[i + 1] > 0 or \
                   (profitNeibor[i] * profitNeibor[i + 1] == 0 and profitNeibor[i] + profitNeibor[i + 1] > 0):
                    temp += profitNeibor[i + 1]

                else:
                    poned.append(temp)
                    temp = profitNeibor[i + 1]
            poned.append(temp)
            return poned



    # the sublist of proPoNe which the sums is the biggest
    def maxpro(self, proPoNe):
        if not proPoNe:
            return 0

        temp = maxProfit = 0
        for ele in proPoNe:
            if ele >= 0:
                temp += ele
                maxProfit = max(maxProfit, temp)
            else:
                temp += ele
                if temp < 0:
                    temp = 0
        return maxProfit

    # proPoNe likes '+ - + - + - +'
    def twiceProfit(self, proPoNe):
        length = len(proPoNe)
        result = 0
        if length <= 3:
            for ele in proPoNe:
                if ele > 0:
                    result += ele
            return result
        else:
            mi = min(proPoNe)
            miIndex = proPoNe.index(mi)
            a = self.maxpro(proPoNe[: miIndex]) + self.maxpro(proPoNe[miIndex + 1: ])
            return max(a, self.twiceProfit(proPoNe[: miIndex]), self.twiceProfit(proPoNe[miIndex + 1: ]))



if __name__ == "__main__":
    prices = [1, 8, 2, 9, 7, 13]
    a = [-1, -2, 0, 3, 5, 0, -4, 5, -7, 0]
    b= [8,6,4,3,3,2,3,5,8,3,8,2,6]
    c= [6, -5, 5, -6, 4]

    s = Solution()
    # print b
    print s.maxProfit(b)
    # print s.twiceProfit(c)
    # print s.poNe(a)
    # print a

