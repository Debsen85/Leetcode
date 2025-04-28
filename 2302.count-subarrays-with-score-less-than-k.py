#
# @lc app=leetcode id=2302 lang=python3
#
# [2302] Count Subarrays With Score Less Than K
#

# @lc code=start
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left, right, answer, total = 0, 0, 0, 0
        while right < len(nums):
            total += nums[right]
            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            answer += right - left + 1
            right += 1
        return answer
# @lc code=end

