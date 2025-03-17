#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r, c = 0, 0, 0
        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
                c += 1
            r += 1
        return c
# @lc code=end

