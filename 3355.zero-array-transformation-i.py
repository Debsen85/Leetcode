#
# @lc app=leetcode id=3355 lang=python3
#
# [3355] Zero Array Transformation I
#

# @lc code=start
from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        difference = [0 for _ in range(len(nums))]
        for l, r in queries:
            difference[l] += 1
            if r + 1 < len(nums):
                difference[r + 1] -= 1
        if difference[0] < nums[0]: return False
        for i in range(1, len(nums)):
            difference[i] += difference[i - 1]
            if difference[i] < nums[i]: return False
        return True
# @lc code=end

