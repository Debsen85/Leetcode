#
# @lc app=leetcode id=1099 lang=python3
#
# [1099] Two Sum Less Than K
#

# @lc code=start
from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r, answer = 0, len(nums) - 1, -1
        while l < r:
            s = nums[l] + nums[r]
            if s < k:
                answer = max(answer, s)
                l += 1
            else:
                r -= 1
        return answer
            
# @lc code=end

