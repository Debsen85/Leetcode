#
# @lc app=leetcode id=1402 lang=python3
#
# [1402] Reducing Dishes
#

# @lc code=start
from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        dp = [[-1] * (len(satisfaction) + 1) for _ in range(len(satisfaction))]
        def backtrack(index, multiplier):
            if index == len(satisfaction):
                return 0
            if dp[index][multiplier] != -1:
                return dp[index][multiplier]
            result = max(multiplier * satisfaction[index] + backtrack(index + 1, multiplier + 1), backtrack(index + 1, multiplier))
            dp[index][multiplier] = result
            return result
        return backtrack(0, 1)
# @lc code=end

