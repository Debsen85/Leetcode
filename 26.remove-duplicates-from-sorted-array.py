#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 1
        while R < len(nums):
            if nums[L] != nums[R]:
                L += 1
                nums[L] = nums[R]
            R += 1
        return (L + 1)
# @lc code=end

