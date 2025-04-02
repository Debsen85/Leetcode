#
# @lc app=leetcode id=2291 lang=python3
#
# [2291] Maximum Profit From Trading Stocks
#

# @lc code=start
from typing import List

class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        dp = [[-1 for _ in range(budget + 1)] for _ in range(len(present))]
        def backtracking(index, total):
            if index == len(present) or total < 0:
                return 0
            if dp[index][total] != - 1:
                return dp[index][total]
            res1, res2 = 0, 0
            res1 = backtracking(index + 1, total)
            if total - present[index] >= 0:
                res2 = future[index] - present[index] + backtracking(index + 1, total - present[index])
            dp[index][total] = max(res1, res2)
            return dp[index][total]
        return backtracking(0, budget)
# @lc code=end

