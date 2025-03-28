#
# @lc app=leetcode id=3392 lang=python3
#
# [3392] Count Subarrays of Length Three With a Condition
#

# @lc code=start
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l, r, ans = 0, 2, 0
        while r < len(nums):
            if (2 * (nums[r] + nums[l])) == (nums[l + 1]):
                ans += 1
            r += 1
            l += 1
        return ans
# @lc code=end

