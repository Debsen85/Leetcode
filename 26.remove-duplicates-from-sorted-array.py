#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        c = 1
        while r < len(nums):
            if nums[l] != nums[r]:
                l += 1
                c += 1
                nums[l] = nums[r]
            r += 1
        return c
    # @lc code=end

