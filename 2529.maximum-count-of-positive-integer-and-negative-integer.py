#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0 or nums[-1] < 0: return len(nums)
        n, p = 0, 0
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= 0:
                r = m - 1
                n = m
            else:
                l = m + 1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= 0:
                l = m + 1
                p = len(nums) - 1 - m
            else:
                r = m - 1
        return max(n, p)
# @lc code=end

