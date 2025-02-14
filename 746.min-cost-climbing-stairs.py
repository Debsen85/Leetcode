#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from typing import List

class Solution:
    def backtrack(self, cost, index, cache):
        if index >= len(cost):
            return 0
        if index in cache:
            return cache[index]
        cache[index] = cost[index] + min(self.backtrack(cost, index + 1, cache), self.backtrack(cost, index + 2, cache))
        return cache[index]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        return min(self.backtrack(cost, 0, cache), self.backtrack(cost, 1, cache))
# @lc code=end

