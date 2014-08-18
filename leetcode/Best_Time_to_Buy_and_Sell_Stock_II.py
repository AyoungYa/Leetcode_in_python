"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions
as you like (ie, buy one and sell one share of the stock multiple times). However, you
may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
__author__ = 'Yang'
import time

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

            if max(profitNeibor) <= 0:
                return 0
            else:
                maxProfit = 0
                for ele in profitNeibor:
                    if ele > 0:
                        maxProfit += ele

                return maxProfit


if __name__ == "__main__":
    prices = [1, 8, 2, 9, 7, 13]
    s = Solution()
    st = time.clock()
    print s.maxProfit(prices)
    et = time.clock()

    print et - st