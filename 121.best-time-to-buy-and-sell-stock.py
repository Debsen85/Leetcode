#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nextGreater = prices[:]
        greatest = -1
        for index in reversed(range(len(prices))):
            if greatest == -1:
                greatest = prices[index]
            else:
                if greatest < prices[index]:
                    greatest = prices[index]
                else:
                    nextGreater[index] = greatest
        return max([val1 - val2 for val1, val2 in zip(nextGreater, prices)])
# @lc code=end

