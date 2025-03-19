#
# @lc app=leetcode id=3191 lang=python3
#
# [3191] Minimum Operations to Make Binary Array Elements Equal to One I
#

# @lc code=start
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        j, answer = 0, 0
        while j < len(nums):
            while j < len(nums) and nums[j] != 0:
                j += 1
            if j == len(nums):
                return answer
            if j < len(nums) and j + 1 < len(nums) and j + 2 < len(nums):
                answer += 1
                nums[j] = 1 
                nums[j + 1] = 1 if nums[j + 1] == 0 else 0
                nums[j + 2] = 1 if nums[j + 2] == 0 else 0
                j += 1
                if nums[j] == 1:
                    j += 1
                    if nums[j] == 1:
                        j += 1
            else:
                return -1
        return answer
# @lc code=end

