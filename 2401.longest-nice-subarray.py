#
# @lc app=leetcode id=2401 lang=python3
#
# [2401] Longest Nice Subarray
#

# @lc code=start
from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l, r, curr, answer = 0, 0, 0, 0
        while r < len(nums):
            while curr & nums[r] != 0:
                curr ^= nums[l]
                l += 1
            curr |= nums[r]
            answer = max(answer, r - l + 1)
            r += 1
        return answer
# @lc code=end

