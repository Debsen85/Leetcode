#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r, f = 0, 1, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                if f < 2:
                    l += 1
                    nums[l] = nums[r]
                f += 1
            else:
                l += 1
                f = 1
                nums[l] = nums[r]
            r += 1
        return (l + 1)
# @lc code=end

