#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        dp = {}
        def backtracking(index, current):
            if index == len(nums):
                return current == total // 2
            if (index, current) in dp:
                return dp[(index, current)]
            dp[(index, current)] = backtracking(index + 1, current) or backtracking(index + 1, current + nums[index])
            return dp[(index, current)]
        return backtracking(0, 0)
# @lc code=end

