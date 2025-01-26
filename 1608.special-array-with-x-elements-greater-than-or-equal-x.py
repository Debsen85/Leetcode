#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        n = len(nums)

        nums.sort()

        i, j = 1, 0

        while i < (n + 1):

            while j < n and i > nums[j]:
                j += 1
            
            if i == n - j:
                return i
            
            i += 1

        return -1
        
# @lc code=end

