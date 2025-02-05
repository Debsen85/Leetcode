#
# @lc app=leetcode id=1800 lang=python3
#
# [1800] Maximum Ascending Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        total = nums[0]
        answer = nums[0]
        index = 1
        while index < len(nums):
            if nums[index] > nums[index - 1]:
                total += nums[index]
            else:
                total = nums[index]
            answer = max(answer, total)
            index += 1
        return answer
# @lc code=end

