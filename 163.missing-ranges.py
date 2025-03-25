#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#

# @lc code=start
from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        answer = []

        if nums[0] != lower:
            answer.append([lower, nums[0] - 1])

        for index in range(1, len(nums)):
            if nums[index] - nums[index - 1] > 1:
                answer.append([nums[index - 1] + 1, nums[index] - 1])

        if nums[-1] != upper:
            answer.append([nums[-1] + 1, upper])

        return answer
# @lc code=end

