#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        def reverse(s, e):
            i = s
            j = e

            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)   
# @lc code=end