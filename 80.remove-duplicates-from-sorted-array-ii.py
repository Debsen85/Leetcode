#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R, K = 0, 1, 1
        while R < len(nums):
            if nums[L] == nums[R]:
                if K < 2:
                    L += 1
                    nums[L] = nums[R]
                K += 1
            else:
                K = 1
                L += 1
                nums[L] = nums[R]
            R += 1
        return (L + 1)
# @lc code=end

