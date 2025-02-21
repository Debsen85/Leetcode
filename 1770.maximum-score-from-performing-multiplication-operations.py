#
# @lc app=leetcode id=1770 lang=python3
#
# [1770] Maximum Score from Performing Multiplication Operations
#

# @lc code=start
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        cache = [[-(10 ** 9)] * len(multipliers) for _ in range(len(nums))]
        def backtracking(i, j, k):
            if i > j or k == len(multipliers):
                return 0
            if cache[i][k] != -(10 ** 9):
                return cache[i][k]
            cache[i][k] = max(cache[i][k], max(nums[j] * multipliers[k] + backtracking(i, j - 1, k + 1), nums[i] * multipliers[k] + backtracking(i + 1, j, k + 1)))
            return cache[i][k]
        return backtracking(0, len(nums) - 1, 0)
        
# @lc code=end

