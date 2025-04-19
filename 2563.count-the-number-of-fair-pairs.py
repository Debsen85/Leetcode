#
# @lc app=leetcode id=2563 lang=python3
#
# [2563] Count the Number of Fair Pairs
#

# @lc code=start
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.search(nums, upper + 1) - self.search(nums, lower)
    
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        c = 0
        while l < r:
            t = nums[l] + nums[r]
            if t < target:
                c += r - l
                l += 1
            else:
                r -= 1
        return c
        
# @lc code=end

