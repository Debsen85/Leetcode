#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index in range(len(prices) - 1):
            if prices[index + 1] - prices[index] > 0:
                profit += prices[index + 1] - prices[index]
        return profit
# @lc code=end

