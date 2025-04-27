#
# @lc app=leetcode id=3392 lang=python3
#
# [3392] Count Subarrays of Length Three With a Condition
#

# @lc code=start
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l, r, answer = 0, 2, 0
        while r < len(nums):
            if (nums[l] + nums[r]) * 2 == nums[l + 1]:
                answer += 1
            l += 1
            r += 1
        return answer 
# @lc code=end

