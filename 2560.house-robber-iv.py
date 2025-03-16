#
# @lc app=leetcode id=2560 lang=python3
#
# [2560] House Robber IV
#

# @lc code=start
from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def isItValid(value):
            i = 0
            c = 0
            while i < len(nums):
                if nums[i] <= value:
                    c += 1
                    i += 2
                else:
                    i += 1
                if c == k:
                    return True
            return c == k
        
        l, r = min(nums), max(nums)
        result = 0
        while l <= r:
            m = (l + r) // 2
            if isItValid(m):
                result = m
                r = m - 1
            else:
                l = m + 1
        return result

# @lc code=end

