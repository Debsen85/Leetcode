#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for index in range(len(nums) - 2, -1, -1):
            if index + nums[index] >= goal:
                goal = index
        return goal == 0
# @lc code=end

