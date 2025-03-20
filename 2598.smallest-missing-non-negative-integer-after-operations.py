#
# @lc app=leetcode id=2598 lang=python3
#
# [2598] Smallest Missing Non-negative Integer After Operations
#

# @lc code=start
from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        for index in range(len(nums)):
            if nums[index] < 0:
                if -value <= nums[index] <= -1:
                    nums[index] = value + nums[index]
                else:
                    multiplier = (-nums[index] // value)
                    if -nums[index] % value:
                        multiplier += 1
                    nums[index] += (multiplier * value)
            elif nums[index] >= value:
                nums[index] %= value

        nums.sort()

        l, r = 0, 1

        while r < len(nums):
            if nums[r] == nums[l]:
                nums[r] += (r - l) * value
            else:
                l = r
            r += 1

        nums.sort()

        value = 0

        for num in nums:
            if num != value:
                return value
            value += 1

        return value
# @lc code=end

