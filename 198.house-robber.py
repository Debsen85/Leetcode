#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def backtracking(index):
            if index >= len(nums):
                return 0
            if cache[index] != -1:
                return cache[index]
            cache[index] = max(nums[index] + backtracking(index + 2), backtracking(index + 1))
            return cache[index]
        return backtracking(0)
        
# @lc code=end

