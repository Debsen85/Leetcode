#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#

# @lc code=start
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = False
        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                if flag:
                    return False
                flag = True
                if index == 0 or nums[index - 1] <= nums[index + 1]:
                    nums[index] = nums[index + 1]
                else:
                    nums[index + 1] = nums[index]
        return True
# @lc code=end

