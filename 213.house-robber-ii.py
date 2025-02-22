#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        cache = [[-1] * 2 for _ in range(len(nums))]
        def backtracking(index, flag):
            if index >= len(nums) or (flag and index == len(nums) - 1):
                return 0
            if cache[index][flag] != -1:
                return cache[index][flag]
            cache[index][flag] = max(nums[index] + backtracking(index + 2, flag or index == 0), backtracking(index + 1, flag))
            return cache[index][flag]
        return max(backtracking(0, True), backtracking(1, False))
# @lc code=end

