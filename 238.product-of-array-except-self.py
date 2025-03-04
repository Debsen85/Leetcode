#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        countZero = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                countZero += 1
        for i in range(len(nums)):
            if countZero:
                if nums[i] == 0:
                    nums[i] = product if countZero == 1 else 0
                else:
                    nums[i] = 0
            else:
                nums[i] = product // nums[i]
        return nums
# @lc code=end