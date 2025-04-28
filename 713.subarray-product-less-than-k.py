#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left, right, answer, total = 0, 0, 0, 1
        while right < len(nums):
            total *= nums[right]
            while total >= k:
                total //= nums[left]
                left += 1
            answer += right - left + 1
            right += 1
        return answer
# @lc code=end

