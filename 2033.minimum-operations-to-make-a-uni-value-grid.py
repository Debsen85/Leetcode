#
# @lc app=leetcode id=2033 lang=python3
#
# [2033] Minimum Operations to Make a Uni-Value Grid
#

# @lc code=start
from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [val for row in grid for val in row]
        nums.sort()
        median = nums[len(nums) // 2]
        operations = 0
        for num in nums:
            if abs(num - median) % x:
                return -1
            operations += abs(num - median) // x
        return operations
# @lc code=end

