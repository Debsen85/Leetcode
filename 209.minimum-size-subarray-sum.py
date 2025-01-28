#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = len(nums) + 1
        L, R = 0, 0
        total = 0
        
        while R < len(nums):
            total += nums[R]
            while total >= target:
                if total >= target:
                    answer = min(answer, R - L + 1)
                total -= nums[L]
                L += 1
            R += 1

        return answer if answer != len(nums) + 1 else 0
        
# @lc code=end

